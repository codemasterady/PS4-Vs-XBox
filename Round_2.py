# Importing the libraires
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Getting the dataset
dataset = pd.read_csv("vgsales.csv")

# Getting the problem specific datasets
platform = dataset['Platform'].values

# Convering to a 2d array
platform = np.array(platform.reshape(-1, 1))

# Getting the num of consoled for each category
num_of_playstations = 0
num_of_xbox = 0
for current_element in platform:
    if current_element == "PS3" or current_element== "PS2" or current_element == "PS4" or current_element == "PS" or current_element == "PSP":
        num_of_playstations += 1
    elif current_element == "X360" or current_element == "XB" or current_element == "XONE":
        num_of_xbox +=1
        
# The Final Output
plt.bar(["Play Station", "X-Box"],height=[num_of_playstations, num_of_xbox], color=['blue', 'green'])
