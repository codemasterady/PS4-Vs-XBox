# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from collections import Counter


# Importing the dataset
dataset = pd.read_csv("vgsales.csv")

# Getting the round specific data
year = dataset['Year'].values
platform = dataset['Platform'].values


# Converting into 2d arrays
year = np.array(year).reshape(-1, 1)
platform = np.array(platform).reshape(-1, 1)
input_arr = np.concatenate((year, platform), 1)

# Creating a dictionary of playstations and X-Boxes
list_of_consoles = []
for current_element in input_arr:
    if current_element[1] == "PS3" or current_element[1] == "PS2" or current_element[1] == "PS4" or current_element[1] == "PS" or current_element[1] == "PSP":
        list_of_consoles.append({"Console": "Play Station", "Year": current_element[0]})
    elif current_element[1] == "X360" or current_element[1] == "XB" or current_element[1] == "XONE":
        list_of_consoles.append({"Console": "X-Box", "Year": current_element[0]})


# Getting all the variables for a plot
X_Box_plots = []
Play_Station_Plots = []
for curr2_element in list_of_consoles:
    if curr2_element.get("Console") == "X-Box":
        X_Box_plots.append(curr2_element.get("Year"))
    else:
        Play_Station_Plots.append(curr2_element.get("Year"))
    
# Calculating the number of values for each year
plt.subplot(221)
plt.title("Play Station")
plt.xlabel("Year")
plt.ylabel("Volume")
plt.hist(Play_Station_Plots, color='blue', rwidth=0.8, align='left')
plt.subplot(223)
plt.xlabel("Year\nX-Box")
plt.ylabel("Volume")
plt.hist(X_Box_plots, color='green', rwidth=0.8, align='left')
plt.show() 