#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Ivar
"""
import multiprocessing
from collections import OrderedDict

from multiprocessing import Pool, Manager, Process, Lock
#from sourcecode.src.vx.pclas.Description import Description

import cv2 as cv2
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.twodim_base import mask_indices
import pandas as pd
import os
from skimage.feature.texture import local_binary_pattern
import time
import sys
import random
import pandas as pd
import csv
import nrrd
from multiprocessing import cpu_count, Pool

import logging
import radiomics
from radiomics.featureextractor import RadiomicsFeatureExtractor
import shutil
import threading

threading.current_thread().name = 'Main'



from  Util import *
import SimpleITK as sitk

from skimage import exposure

# File variables
ROOT = 'E:\Datasets\DatasetBalanced'
INPUTCSV = os.path.join(ROOT, 'ExtractFeatures.csv')
OUTPUTCSV = 'E:/Datasets/DatasetBalanced/Features/Features.csv'
TEMP_DIR = os.path.join(ROOT, '_TEMP') 
REMOVE_TEMP_DIR = False  # Remove temporary directory when results have been successfully stored into 1 file

LOG = os.path.join(ROOT,  'log.txt')  # Location of output log file

rLogger = radiomics.logger
logHandler = logging.FileHandler(filename=LOG, mode='a')
logHandler.setLevel(logging.INFO)
logHandler.setFormatter(logging.Formatter('%(levelname)-.1s: (%(threadName)s) %(name)s: %(message)s'))
rLogger.addHandler(logHandler)

HEADERS = None  # headers of all extracted features


NUM_OF_WORKERS = cpu_count() - 1  # Number of processors to use, keep one processor free for other work
if NUM_OF_WORKERS < 1:  # in case only one processor is available, ensure that it is used
  NUM_OF_WORKERS = 1


def run(case):
  global ROOT, TEMP_DIR
  ptLogger = logging.getLogger('radiomics.batch')

  feature_vector = OrderedDict(case)

  try:
    # set thread name to patient name
    threading.current_thread().name = case['ID']

    filename = r'features_' + str(case['Reader']) + '_' + str(case['ID']) + '.csv'
    output_filename = os.path.join(ROOT, TEMP_DIR, filename)

    if os.path.isfile(output_filename):
      # Output already generated, load result (prevents re-extraction in case of interrupted process)
      with open(output_filename, 'w') as outputFile:
        reader = csv.reader(outputFile)
        headers = reader.rows[0]
        values = reader.rows[1]
        feature_vector = OrderedDict(zip(headers, values))

      ptLogger.info('ID %s read by %s already processed...', case['ID'], case['Reader'])

    else:
        t = datetime.now()

        ID = case['ID']  # Required
        imageFilepath = case['Image']  # Required
        maskFilepath = case['Mask']  # Required
        label = case.get('Label', None)  # Optional

        base = os.path.basename(imageFilepath)
        base = os.path.splitext(base)
        imgoname = base[0]

        # imagefi = os.path.join(inputdir, imagedir, targetSet, imageName)
        pathou = os.path.join(os.path.dirname(maskFilepath), imgoname + '.nrrd')

        inputImage = cv2.imread(imageFilepath, cv2.IMREAD_GRAYSCALE)
        mask = sitk.ReadImage(pathou)
        mask2 = sitk.GetArrayFromImage(mask)


        radiusl = [10]
        vect = []
        vect_names = []
        for radius in radiusl:
            nPoints = 10 * radius
            lbp = local_binary_pattern(inputImage, nPoints, radius, method='uniform')
            xnBins = int(lbp.max() + 1)
            histogram, _ = np.histogram(lbp[np.where(mask2 == True) ], bins=xnBins, range=(0, xnBins))
            aux = histogram.tolist()
            vect += aux
            vect_names += ["LBP_r"+str(radius)+"_"+str(i+1) for i in range(len(aux))]

        # Instantiate Radiomics Feature extractor

        extractor = RadiomicsFeatureExtractor()

        extractor.enableImageTypes(
            Original={},
            Wavelet={},
            LoG={'sigma':[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6.0]},
            LBP2D={}
            )

        extractor.disableAllFeatures()
        extractor.enableFeatureClassByName('firstorder') #19
        extractor.enableFeatureClassByName('glcm') #24
        extractor.enableFeatureClassByName('glrlm') #16   
        extractor.enableFeatureClassByName('glszm') #16
        extractor.enableFeatureClassByName('ngtdm') #5
        extractor.enableFeatureClassByName('gldm') #14
        # extractor.enableFeatureClassByName('lbp')#14


        image = sitk.ReadImage(imageFilepath, sitk.sitkFloat32)
        mask3 = sitk.ReadImage(pathou)

        # Extract features
        resultsPyRad =  extractor.execute(image, mask3, True)

        features_names = []
        features_values = []        
        for k,v in resultsPyRad.items():
            k = k.replace('-', '_')
            if k.startswith('original') or k.startswith('wavelet') or k.startswith('log') or k.startswith('lbp') or k.startswith('logarithm')  or k.startswith('exponential') or k.startswith('squareroot') or k.startswith('gradient'): 
                if not  k.endswith('Id'):
                    features_names.append(k)
                    v = "{:.8f}".format(v)
                    features_values.append(v)




        feature_vector.update(zip(['ID']+vect_names+features_names+['Label'], [ID]+vect+features_values+[label]))

        # Store results in temporary separate files to prevent write conflicts
        # This allows for the extraction to be interrupted. Upon restarting, already processed cases are found in the
        # TEMP_DIR directory and loaded instead of re-extracted
        with open(output_filename, 'w') as outputFile:
            writer = csv.DictWriter(outputFile, fieldnames=list(feature_vector.keys()), lineterminator='\n')
            writer.writeheader()
            writer.writerow(feature_vector)

        # Display message

        delta_t = datetime.now() - t

        ptLogger.info('ID %s read by %s processed in %s', case['ID'], case['Reader'], delta_t)

  except Exception:
    ptLogger.error('Feature extraction failed!', exc_info=True)

  return feature_vector

def _writeResults(featureVector):
  global HEADERS, OUTPUTCSV

  # Use the lock to prevent write access conflicts
  try:
    with open(OUTPUTCSV, 'a') as outputFile:
      writer = csv.writer(outputFile, lineterminator='\n')
      if HEADERS is None:
        HEADERS = list(featureVector.keys())
        writer.writerow(HEADERS)

      row = []
      for h in HEADERS:
        row.append(featureVector.get(h, "N/A"))
      writer.writerow(row)
  except Exception:
    logging.getLogger('radiomics.batch').error('Error writing the results!', exc_info=True)

if __name__ == "__main__":
    logger = logging.getLogger('radiomics.batch')

    # Ensure the entire extraction is handled on 1 thread
    #####################################################

    sitk.ProcessObject_SetGlobalDefaultNumberOfThreads(1)

    # Set up the pool processing
    ############################

    logger.info('pyradiomics version: %s', radiomics.__version__)
    logger.info('Loading CSV...')
    # Extract List of cases
    cases = []
    try:
        with open(INPUTCSV, 'r') as inFile:
            cr = csv.DictReader(inFile, lineterminator='\n')
            cases = []
            for row_idx, row in enumerate(cr, start=1):
                # If not included, add a "Patient" and "Reader" column.
                if 'ID' not in row:
                    row['ID'] = row_idx
                if 'Reader' not in row:
                    row['Reader'] = row_idx
                cases.append(row)

    except Exception:
        print('CSV READ FAILED', exc_info=True)
    
    
    logger.info('Loaded %d jobs', len(cases))

    # Make output directory if necessary
    if not os.path.isdir(os.path.join(ROOT, TEMP_DIR)):
        logger.info('Creating temporary output directory %s', os.path.join(ROOT, TEMP_DIR))
        os.mkdir(os.path.join(ROOT, TEMP_DIR))

    # Start parallel processing
    ###########################

    # for case in cases:
    #   ID = case['ID']  # Required
    #   print(ID)
    #   imageFilepath = case['Image']  # Required
    #   maskFilepath = case['Mask']  # Required
    #   label = case.get('Label', None)  # Optional
    #   base = os.path.basename(imageFilepath)
    #   base = os.path.splitext(base)
    #   imgoname = base[0]

    #   # imagefi = os.path.join(inputdir, imagedir, targetSet, imageName)
    #   pathou = os.path.join(os.path.dirname(maskFilepath), imgoname + '.nrrd')

    #   image  = cv2.imread(maskFilepath, cv2.IMREAD_GRAYSCALE)
    #   im_size = image.shape
    #   mask = np.zeros(im_size, dtype=int)
    #   mask[np.where(image != 0)] = 1

    #   sitk.WriteImage(sitk.GetImageFromArray(mask), pathou, True)

    logger.info('Starting parralel pool with %d workers out of %d CPUs', NUM_OF_WORKERS, cpu_count())
    # Running the Pool
    pool = Pool(NUM_OF_WORKERS)
    results = pool.map(run, cases)


    try:
        # Store all results into 1 file
        with open(OUTPUTCSV, mode='w') as outputFile:
            writer = csv.DictWriter(outputFile,
                                    fieldnames=list(results[0].keys()),
                                    restval='',
                                    extrasaction='raise',  # raise error when a case contains more headers than first case
                                    lineterminator='\n')
            writer.writeheader()
            writer.writerows(results)

            if REMOVE_TEMP_DIR:
                logger.info('Removing temporary directory %s (contains individual case results files)',
                        os.path.join(ROOT, TEMP_DIR))
                shutil.rmtree(os.path.join(ROOT, TEMP_DIR))
    except Exception:
        logger.error('Error storing results into single file!', exc_info=True)
  
