# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Getting the dataset
dataset = pd.read_csv("vgsales.csv")

# Getting the necessary variables for the rounds
rank = dataset['Rank'].values
platform = dataset['Platform'].values

# Merging the two arrays
rank = np.array(rank).reshape(-1, 1)
platform = np.array(platform).reshape(-1, 1)
final_input = np.concatenate((rank, platform), 1)

# Getting the Play Station and the X-Box exclusives
list_of_consoles = []
for current_element in final_input:
    if current_element[1] == "PS3" or current_element[1] == "PS2" or current_element[1] == "PS4" or current_element[1] == "PS" or current_element[1] == "PSP":
        list_of_consoles.append({"Console": "Play Station", "Rank": current_element[0]})
    elif current_element[1] == "X360" or current_element[1] == "XB" or current_element[1] == "XONE":
        list_of_consoles.append({"Console": "X-Box", "Rank": current_element[0]})

# Extracting the values for each individual console
num_of_ps = 0
num_of_x_box = 0
list_of_ps_ranks = []
list_of_x_box_ranks = []

# Looping through all the consoles and their ranks
for console_dict in list_of_consoles:
    if (console_dict.get("Console") == "Play Station"):
        num_of_ps += 1
        list_of_ps_ranks.append(console_dict.get("Rank"))
    else:
        num_of_x_box += 1
        list_of_x_box_ranks.append(console_dict.get("Rank"))

# Adding up all the total score for the Play Station & X-Box
sum_of_ps_ranks = sum(list_of_ps_ranks)
sum_of_x_box_ranks = sum(list_of_x_box_ranks)

# Calculating the average score
avg_score_ps = sum_of_ps_ranks/num_of_ps
avg_score_x_box = sum_of_x_box_ranks/num_of_x_box

# Plotting the final results
plt.title("Console Vs Score Index")
plt.xlabel("Console Type")
plt.ylabel("Average Score\n(Σ(Scores)/num of consoles)")
plt.bar(["PlayStation", "X-Box"], [avg_score_ps, avg_score_x_box], color=["blue", "green"])
plt.show() 
