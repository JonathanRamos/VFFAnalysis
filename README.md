# Analysis of Vertebral Fragility Fractures (VFF)

Database available at: 10.5281/zenodo.6415420

TODO: Suplementary Materials and Database



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


\end{tikzpicture}


