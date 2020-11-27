# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Getting the dataset
dataset = pd.read_csv("vgsales.csv")

# Getting the problem specific datasets
us_sales = dataset['NA_Sales'].values
eu_sales = dataset['EU_Sales'].values
jp_sales = dataset['JP_Sales'].values
other_sales = dataset['Other_Sales'].values
platform = dataset['Platform'].values

# Converting these values into a 2d array
us_sales = np.array(us_sales).reshape(-1, 1)
eu_sales = np.array(eu_sales).reshape(-1, 1)
jp_sales = np.array(jp_sales).reshape(-1, 1)
other_sales = np.array(other_sales).reshape(-1, 1)
platform = np.array(platform).reshape(-1, 1)

# Concatenating all the values
input_arr = np.concatenate((us_sales, eu_sales, jp_sales, other_sales, platform), 1)

# Getting the console specific values
list_of_consoles = []
for current_element in input_arr:
    if current_element[-1] == "PS3" or current_element[-1] == "PS2" or current_element[-1] == "PS4" or current_element[-1] == "PS" or current_element[-1] == "PSP":
        list_of_consoles.append({"Console": "Play Station", "US": current_element[0], "EU": current_element[1], "JP": current_element[2], "Other": current_element[3]})
    elif current_element[-1] == "X360" or current_element[-1] == "XB" or current_element[-1] == "XONE":
        list_of_consoles.append({"Console": "X-Box", "US": current_element[0], "EU": current_element[1], "JP": current_element[2], "Other": current_element[3]})
        
# Play Station & X-Box Preprocess
array_to_be_plotted_ps = []
array_to_be_plotted_x_box = []
for i in range(0, len(list_of_consoles)):
    if list_of_consoles[i].get("Console") == "Play Station":
        array_to_be_plotted_ps.append([list_of_consoles[i].get("US"), list_of_consoles[i].get("EU"), list_of_consoles[i].get("JP"), list_of_consoles[i].get("Other")])
    else:
        array_to_be_plotted_x_box.append([list_of_consoles[i].get("US"), list_of_consoles[i].get("EU"), list_of_consoles[i].get("JP"), list_of_consoles[i].get("Other")])
        
# Converting the newly generated arrays to a 2d array
array_to_be_plotted_ps = np.array(array_to_be_plotted_ps).reshape(-1, 4)
array_to_be_plotted_x_box = np.array(array_to_be_plotted_x_box).reshape(-1, 4)

# Play Station

# Initializing the plots
us_ps = []
eu_ps = []
jp_ps = []
ot_ps = []

# Filling up the lists
for i in range(0, len(array_to_be_plotted_ps)-6185):
    us_ps.append(array_to_be_plotted_ps[i, 0])
    eu_ps.append(array_to_be_plotted_ps[i, 1])
    jp_ps.append(array_to_be_plotted_ps[i, 2])
    ot_ps.append(array_to_be_plotted_ps[i, 3])

# Test plotting Play Station
y = []
for i in range(0, len(array_to_be_plotted_ps)-6185):
    y.append(i)
plt.title("Play Station Sales")
plt.xlabel("Pass")
plt.ylabel("Sales (Millions)")
plt.scatter(y, us_ps, marker="X", label="US")
plt.scatter(y, eu_ps, marker="X", label="Europe")
plt.scatter(y, jp_ps, marker="X", label="Japan")
plt.scatter(y, ot_ps, marker="X", label="Others")
plt.legend()
plt.show() 

# X-Box

# Initializing the plots
us_x_box = []
eu_x_box = []
jp_x_box = []
ot_x_box = []

# Filling up the lists
for i in range(0, len(array_to_be_plotted_x_box)-1989):
    us_x_box.append(array_to_be_plotted_x_box[i, 0])
    eu_x_box.append(array_to_be_plotted_x_box[i, 1])
    jp_x_box.append(array_to_be_plotted_x_box[i, 2])
    ot_x_box.append(array_to_be_plotted_x_box[i, 3])

# Test plotting X-Box
z = []
for i in range(0, len(array_to_be_plotted_x_box)-1989):
    z.append(i)
plt.title("X-Box Sales")
plt.xlabel("Pass")
plt.ylabel("Sales (Millions)")
plt.scatter(z, us_x_box, marker="X", label="US")
plt.scatter(z, eu_x_box, marker="X", label="Europe")
plt.scatter(z, jp_x_box, marker="X", label="Japan")
plt.scatter(z, ot_x_box, marker="X", label="Others")
plt.legend()
plt.show() 
