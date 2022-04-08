# Analysis of Vertebral Fragility Fractures (VFF)

Database available at: 10.5281/zenodo.6415420

TODO: Suplementary Materials and Database



\scriptsize\sffamily
\setlength{\tabcolsep}{1pt}
\renewcommand{\arraystretch}{0.2}
\centering
\begin{tabular}{cc}

\raisebox{-.53\height}{
\begin{tikzpicture}[font=\sffamily\scriptsize]

\begin{axis}[
width=0.45\textwidth,
height=0.6\textwidth,
title style={yshift=-0.25cm,},
ylabel style={yshift=-0.1cm},
yticklabel style={xshift=0cm, yshift=0cm},
/pgfplots/boxplot/box extend=0.8,
y axis line style = {opacity=5},
xticklabel={\pgfmathparse{\tick}\pgfmathprintnumber{\pgfmathresult}\%},
title style={align=center,yshift=0.1cm,top color=NavyBlue!40!white,bottom color=white,rounded corners},
title={\textbf{\accuracy}},
ylabel style={align=center, bottom color=white,top color=gray!30,rounded corners,yshift=0.15cm},
% xmin={64},
% xmax={95},
% xtick={65,70,75,80,85,90,95},
xmajorgrids,
ymajorgrids,
xminorgrids,
minor x tick num={1},
y tick style={line width=0.5pt},
minor x grid style={dotted,black},
ytick={1,...,25},
yticklabels={\textbf{SVMC20.0.csv},RandomForest20.0.csv,NBayes20.0.csv,\textbf{KNN20.0.csv},HistGradient20.0.csv,GradientBoosting20.0.csv,\textbf{ExtraTrees20.0.csv},DTree20.0.csv,\textbf{DAnalysisQuadratic20.0.csv}},
    boxplot/every box/.style={fill=gray!30,draw=black,solid},
boxplot/every whisker/.style={black,thick,solid},
boxplot/every median/.style={black, thick,solid},
boxplot/every mark/.append style={solid, fill=white},
boxplot/every average/.style={/tikz/mark=x, mark size=3.0},
]
%SVMC20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=50.2083,lower quartile=54.2708,upper quartile=63.9583,upper whisker=72.0833,median=59.0625,average=59.4562,sample size=100"}] coordinates {};
     %RandomForest20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=49.1667,lower quartile=57.2917,upper quartile=63.0208,upper whisker=71.4583,median=59.7917,average=59.7521,sample size=100"}] coordinates {};
     %NBayes20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=46.875,lower quartile=53.8542,upper quartile=60.2083,upper whisker=66.4583,median=56.875,average=56.95,sample size=100"}] coordinates {};
     %KNN20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=50,lower quartile=57.1875,upper quartile=62.5,upper whisker=67.9167,median=59.7917,average=59.725,sample size=100"}] coordinates {};
     %HistGradient20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=51.6667,lower quartile=59.4792,upper quartile=65.3125,upper whisker=73.75,median=61.6667,average=61.7125,sample size=100"}] coordinates {};
     %GradientBoosting20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=50.4167,lower quartile=57.9167,upper quartile=64.0625,upper whisker=72.9167,median=60.9375,average=60.6542,sample size=100"}] coordinates {};
     %ExtraTrees20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=49.5833,lower quartile=57.6042,upper quartile=63.3333,upper whisker=70.4167,median=60.8333,average=60.4375,sample size=100"}] coordinates {};
     %DTree20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=48.75,lower quartile=53.3333,upper quartile=57.0833,upper whisker=60.8333,median=55,average=54.9542,sample size=100"}] coordinates {};
     %DAnalysisQuadratic20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=50.625,lower quartile=59.5833,upper quartile=66.1458,upper whisker=73.9583,median=63.5417,average=62.6958,sample size=100"}] coordinates {};
     
     
\end{axis}


\end{tikzpicture}}

&




\raisebox{-.53\height}{
\begin{tikzpicture}[font=\sffamily\scriptsize]
\begin{axis}[
width=0.45\textwidth,
height=0.6\textwidth,
title style={yshift=-0.25cm,},
xlabel style={yshift=-0.1cm},
% boxplot/draw direction=y,
xmajorgrids,
nodes near coords,
nodes near coords align={horizontal},
boxplot = {average = auto,every average/.style={/tikz/mark=x},},
yticklabels={,,},
/pgfplots/boxplot/box extend=0.8,
% xlabel = {\textbf{\precision (\%)}},
xticklabel={\pgfmathparse{\tick}\pgfmathprintnumber{\pgfmathresult}\%},
% title style={align=center,yshift=0.1cm,xshift=0.01cm,top color=blue!30!white,bottom color=white,rounded corners},
title style={align=center,yshift=0.1cm,top color=NavyBlue!40!white,bottom color=white,rounded corners},
title={\textbf{\precision}},
% ylabel style={align=center, bottom color=white,top color=gray!30,rounded corners,yshift=0.15cm},
% ylabel=\textbf{Classical} \\ \textbf{Machine Learning},
% xtick={1,3,...,12},
% xmin={55},
% xmax={95},
% xtick={45,55,65,75,85,95},
xmajorgrids,
ymajorgrids,
minor x tick num={1},
minor x tick style={line width=0.5pt},
xminorgrids,
minor x grid style={dotted,black},
ytick={1,...,25},
yticklabels={\textbf{SVMC20.0.csv},RandomForest20.0.csv,NBayes20.0.csv,\textbf{KNN20.0.csv},HistGradient20.0.csv,GradientBoosting20.0.csv,\textbf{ExtraTrees20.0.csv},DTree20.0.csv,\textbf{DAnalysisQuadratic20.0.csv}},
    boxplot/every box/.style={fill=gray!30,draw=black,solid},
boxplot/every whisker/.style={black,thick,solid},
boxplot/every median/.style={black, thick,solid},
boxplot/every mark/.append style={solid, fill=white},
boxplot/every average/.style={/tikz/mark=x, mark size=3.0},
]

     %SVMC20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=50.1044,lower quartile=52.6794,upper quartile=63.2404,upper whisker=78.7037,median=57.5064,average=59.2131,sample size=100"}] coordinates {};
     %RandomForest20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=49.4681,lower quartile=55.9333,upper quartile=60.8296,upper whisker=66.4286,median=58.3619,average=58.2689,sample size=100"}] coordinates {};
     %NBayes20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=48.2759,lower quartile=53.7983,upper quartile=64.299,upper whisker=76.3441,median=57.8499,average=61.3098,sample size=100"}] coordinates {};
     %KNN20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=50.8772,lower quartile=56.8417,upper quartile=62.9413,upper whisker=69.1964,median=60.0832,average=58.8858,sample size=100"}] coordinates {};
     %HistGradient20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=49.8947,lower quartile=55.966,upper quartile=61.3251,upper whisker=68.3486,median=58.2967,average=58.7358,sample size=100"}] coordinates {};
     %GradientBoosting20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=50.289,lower quartile=55.5556,upper quartile=61.3583,upper whisker=67.6596,median=57.9323,average=58.1818,sample size=100"}] coordinates {};
     %ExtraTrees20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=49.7653,lower quartile=56.077,upper quartile=61.3221,upper whisker=68.8259,median=59.3127,average=58.7127,sample size=100"}] coordinates {};
     %DTree20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=48.9209,lower quartile=52.9996,upper quartile=56.3073,upper whisker=59.7403,median=54.3516,average=54.4174,sample size=100"}] coordinates {};
     %DAnalysisQuadratic20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=49.0667,lower quartile=59.4806,upper quartile=68.7208,upper whisker=77.9006,median=64.8969,average=64.0957,sample size=100"}] coordinates {};
     

\end{axis}
\end{tikzpicture}}

\\


\raisebox{-.53\height}{
\begin{tikzpicture}[font=\sffamily\scriptsize]
\begin{axis}[
width=0.45\textwidth,
height=0.6\textwidth,
title style={yshift=-0.25cm,},
ylabel style={yshift=-0.1cm},
% boxplot/draw direction=y,
nodes near coords,
nodes near coords align={horizontal},
xmajorgrids,
nodes near coords,
nodes near coords align={horizontal},
boxplot = {average = auto,every average/.style={/tikz/mark=x}},
/pgfplots/boxplot/box extend=0.8,
% yticklabels={,,},
xticklabel={\pgfmathparse{\tick}\pgfmathprintnumber{\pgfmathresult}\%},
% xlabel={\textbf{\sensitivity (\%)}},
% title style={align=center,yshift=0.1cm,xshift=0.01cm,top color=blue!30!white,bottom color=white,rounded corners},
title style={align=center,yshift=0.1cm,top color=NavyBlue!40!white,bottom color=white,rounded corners},
title={\textbf{\sensitivity}},
% ylabel style={align=center, bottom color=white,top color=gray!30,rounded corners,yshift=0.13cm},
% ylabel=\textbf{Classical} \\ \textbf{Machine Learning},
% xtick = {0,10,...,60},
% xmin={45},
% xmax = {95},
% xtick={35,45,55,65,75,85,95},
xmajorgrids,
ymajorgrids,
minor x tick num={1},
minor x tick style={line width=0.5pt},
xminorgrids,
minor x grid style={dotted,black},
ytick={1,...,25},
yticklabels={\textbf{SVMC20.0.csv},RandomForest20.0.csv,NBayes20.0.csv,\textbf{KNN20.0.csv},HistGradient20.0.csv,GradientBoosting20.0.csv,\textbf{ExtraTrees20.0.csv},DTree20.0.csv,\textbf{DAnalysisQuadratic20.0.csv}},
    boxplot/every box/.style={fill=gray!30,draw=black,solid},
boxplot/every whisker/.style={black,thick,solid},
boxplot/every median/.style={black, thick,solid},
boxplot/every mark/.append style={solid, fill=white},
boxplot/every average/.style={/tikz/mark=x, mark size=3.0},
]
%SVMC20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=34.1667,lower quartile=72.7083,upper quartile=98.75,upper whisker=100,median=89.375,average=81.2708,sample size=100"}] coordinates {};
     %RandomForest20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=51.25,lower quartile=64.5833,upper quartile=80.8333,upper whisker=99.1667,median=72.5,average=73.0042,sample size=100"}] coordinates {};
     %NBayes20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=6.6667,lower quartile=46.25,upper quartile=73.5417,upper whisker=97.5,median=61.0417,average=57.6917,sample size=100"}] coordinates {};
     %KNN20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=42.0833,lower quartile=56.0417,upper quartile=65.4167,upper whisker=79.1667,median=61.4583,average=59.8667,sample size=100"}] coordinates {};
     %HistGradient20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=61.25,lower quartile=79.5833,upper quartile=92.9167,upper whisker=99.5833,median=85,average=85.2042,sample size=100"}] coordinates {};
     %GradientBoosting20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=61.6667,lower quartile=73.3333,upper quartile=88.75,upper whisker=99.1667,median=80.625,average=81.1833,sample size=100"}] coordinates {};
     %ExtraTrees20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=50.8333,lower quartile=67.5,upper quartile=81.0417,upper whisker=97.0833,median=75,average=74.6833,sample size=100"}] coordinates {};
     %DTree20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=47.5,lower quartile=57.9167,upper quartile=66.6667,upper whisker=76.25,median=62.5,average=62.65,sample size=100"}] coordinates {};
     %DAnalysisQuadratic20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=42.9167,lower quartile=56.4583,upper quartile=70.625,upper whisker=91.25,median=62.5,average=64.7875,sample size=100"}] coordinates {};
     
 
\end{axis}

\end{tikzpicture}}
&

\raisebox{-.53\height}{
\begin{tikzpicture}[font=\sffamily\scriptsize]
\begin{axis}[
width=0.45\textwidth,
height=0.6\textwidth,
title style={yshift=-0.25cm,},
xlabel style={yshift=-0.1cm},
% boxplot/draw direction=y,
nodes near coords, nodes near coords align={horizontal},
boxplot = {average = auto,every average/.style={/tikz/mark=x},},
  /pgfplots/boxplot/box extend=0.8,
xmajorgrids,
        legend style={at={(0.5,-0.2)}, anchor=north, legend columns=-1},
y axis line style = {opacity=5},
xticklabel={\pgfmathparse{\tick}\pgfmathprintnumber{\pgfmathresult}\%},
% xlabel={\textbf{\specificity (\%)}},
% title style={align=center,yshift=0.1cm,xshift=0.01cm,top color=blue!30!white,bottom color=white,rounded corners},
title style={align=center,yshift=0.1cm,top color=NavyBlue!40!white,bottom color=white,rounded corners},
title={\textbf{\specificity}},
% ylabel style={align=center, bottom color=white,top color=gray!30,rounded corners,yshift=0.15cm},
% ylabel=\textbf{Classical} \\ \textbf{Machine Learning},
% xtick = {0,2,...,16},
% xmin={55},
% xmax = {95},
% xtick={55,65,75,85,95,105},
xmajorgrids,
ymajorgrids,
minor x tick num={1},
minor x tick style={line width=0.5pt},
xminorgrids,
minor x grid style={dotted,black},
ytick={1,...,25},
yticklabels={\textbf{SVMC20.0.csv},RandomForest20.0.csv,NBayes20.0.csv,\textbf{KNN20.0.csv},HistGradient20.0.csv,GradientBoosting20.0.csv,\textbf{ExtraTrees20.0.csv},DTree20.0.csv,\textbf{DAnalysisQuadratic20.0.csv}},
    boxplot/every box/.style={fill=gray!30,draw=black,solid},
boxplot/every whisker/.style={black,thick,solid},
boxplot/every median/.style={black, thick,solid},
boxplot/every mark/.append style={solid, fill=white},
boxplot/every average/.style={/tikz/mark=x, mark size=3.0},
]

     %SVMC20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=0.41667,lower quartile=13.3333,upper quartile=60.625,upper whisker=99.1667,median=34.1667,average=37.6417,sample size=100"}] coordinates {};
     %RandomForest20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=12.5,lower quartile=39.1667,upper quartile=57.7083,upper whisker=70.8333,median=50.8333,average=46.5,sample size=100"}] coordinates {};
     %NBayes20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=3.3333,lower quartile=40.625,upper quartile=72.9167,upper whisker=100,median=57.5,average=56.2083,sample size=100"}] coordinates {};
     %KNN20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=41.25,lower quartile=53.9583,upper quartile=65,upper whisker=77.5,median=59.5833,average=59.5833,sample size=100"}] coordinates {};
     %HistGradient20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=0.83333,lower quartile=27.5,upper quartile=49.7917,upper whisker=74.1667,median=40.2083,average=38.2208,sample size=100"}] coordinates {};
     %GradientBoosting20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=7.0833,lower quartile=33.125,upper quartile=50.8333,upper whisker=73.3333,median=41.4583,average=40.125,sample size=100"}] coordinates {};
     %ExtraTrees20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=23.3333,lower quartile=42.2917,upper quartile=56.25,upper whisker=73.3333,median=50,average=46.1917,sample size=100"}] coordinates {};
     %DTree20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=33.75,lower quartile=44.375,upper quartile=51.6667,upper whisker=62.5,median=48.125,average=47.2583,sample size=100"}] coordinates {};
     %DAnalysisQuadratic20.0.csv
      \addplot [black, fill=red!80, boxplot prepared={lower whisker=20,lower quartile=52.7083,upper quartile=74.5833,upper whisker=91.25,median=67.5,average=60.6042,sample size=100"}] coordinates {};
     
     
\end{axis}

\end{tikzpicture}}




\end{tabular}


