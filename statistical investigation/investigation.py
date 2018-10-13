#   Statistical investigation, MVE051, Dec. 2017
#   Author: Daniel Sonne Lehnberg, Undergraduate Physics-program at Gothenburg University.
#   Ported from MATLAB to Python, Aug. 2018.
#   Author: Daniel Sonne Lehnberg, https://www.doddy.se/

# Check the estimated total Earth magnetic field strength in your area at:
# https://www.ngdc.noaa.gov/geomag-web/?model=wmm#igrfwmm
# 
# Importing libraries
import numpy as np
import pandas as pd
import datetime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
import sklearn
from sklearn import linear_model

# Known background and constants, used in calculations
#       Magnetic field strength of the Earth (mG)
magEarth = 50.7327
#       Lower bound on the C-class used by Trafikverket (street light classification)
Cfive = 7.5
#       Upper bound --//--
Cnought = 50
#       Sample variable size
k = 1000

# Data import and processing
#       Importing measurement data from a csv to a pandas dataframe
df = pd.read_csv('example.csv', sep=';')
df.Bx = pd.to_numeric(df.Bx, errors='coerce')
df.By = pd.to_numeric(df.By, errors='coerce')
df.Bz = pd.to_numeric(df.Bz, errors='coerce')
df.I = pd.to_numeric(df.I, errors='coerce')

dfB = df.Bx.add(df.By, fill_value=0)
dfB = dfB.add(df.Bz, fill_value=0)
dfI = df.I

dfB = [Bs for Bs in dfB if str(Bs) != 'nan']
dfI = [Is for Is in dfI if str(Is) != 'nan']

# Making sure to sample dfB and dfI the same way
# also need to control for the background magnetic field
dfB = dfB[0:10000]
for i in range(10000):
    dfB[i]=dfB[i]-magEarth
dfI = dfI[0:10000]

print(len(dfB) , len(dfI))

# Regression and scatterplot
def slope_intercept(B_val, I_val):
    B = np.array(B_val)
    I = np.array(I_val)
    m = ( ( (np.mean(B)*np.mean(I)) - np.mean(B*I) ) / ((np.mean(B)*np.mean(B)) - np.mean(B*B)) )
    m = round(m,2)
    b = (np.mean(I)-np.mean(B)*m)
    b = round(b,2)

    return m,b
print('The slope intercept is ', slope_intercept(dfB, dfI))
m,b=slope_intercept(dfB, dfI)
regressLine = [(m*x)+b for x in dfB]

plt.scatter(dfB,dfI,color="red")
plt.plot(dfB,regressLine)
plt.ylabel("Luminance, lx")
plt.xlabel("Magnetic field strength, mG")
plt.title("Analysis using regression")
plt.show()

# RMSE
def rmse(I1,I_hat):
    I_actual = np.array(I1)
    I_predicted = np.array(I_hat)
    error = (I_actual-I_predicted)**2
    mean_error = round(np.mean(error))
    sq_error = (mean_error)**(1/2)
    return sq_error
print('Root mean squared error is ', rmse(dfI,regressLine))

# Pearson correlation coefficient
print('The Pearson correlation coefficient is ', np.corrcoef(dfB,dfI))