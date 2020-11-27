# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# Defining the UCB functions
def UpperConfidenceBound(preprocessed_data, width, height):
    # Initializing the variables for the algorithm
    genre_selected = []
    numbers_of_selections = [0]*width
    sums_of_rewards = [0]*width
    total_reward = 0
    # Looping through all the data
    for n in range(0, height):
        genre = 0 # Initializing the genre selected
        max_upper_bound = 0
        for i in range(0, width):
            if(numbers_of_selections[i] > 0):
                average_reward = sums_of_rewards[i]/numbers_of_selections[i]
                delta_i = math.sqrt(3/2*math.log(n+1)/numbers_of_selections[i])
                upper_bound = average_reward + delta_i
            else:
                upper_bound = 1e400 # Setting it to a vary high value
            if (upper_bound > max_upper_bound):
                max_upper_bound = upper_bound
                genre = i
        genre_selected.append(genre)
        numbers_of_selections[genre] += 1
        reward = preprocessed_data[n, genre]
        sums_of_rewards[genre] += reward
        total_reward += reward
    return genre_selected
    

# Getting the dataset
dataset = pd.read_csv("vgsales.csv")

# Getting the round related variables
genre = dataset['Genre'].values
platform = dataset['Platform'].values

# Converting the round related features into a 2d array
genre = np.array(genre).reshape(-1, 1)
platform = np.array(platform).reshape(-1, 1)

# Merging the 2 arrays
input_arr = np.concatenate((genre, platform), 1)

# Team PlayStation
list_of_play_station_genres = []
for current_element in input_arr:
    if current_element[1] == "PS3" or current_element[1] == "PS2" or current_element[1] == "PS4" or current_element[1] == "PS" or current_element[1] == "PSP":
        list_of_play_station_genres.append(current_element[0])

# Deriving the number of unique genres for playstation
set_of_uniq_genre_ps = set(list_of_play_station_genres)
num_of_uniq_genre_ps = len(set_of_uniq_genre_ps)

# Initializing the array
initial_preprocessed_ps_data = np.zeros((6235, num_of_uniq_genre_ps))

# Generating the preprocessing data (For PlayStation)
for i in range(0, 6235):
    j = 0 # Variable to keep track of index
    for gen in set_of_uniq_genre_ps:
        if list_of_play_station_genres[i] == gen:
            initial_preprocessed_ps_data[i, j] = 1
            break
        else:
            j += 1
            continue

# Initializing the final preprocessed data
final_preprocessed_ps_data = initial_preprocessed_ps_data

# Getting the final plots from the UCB algorithm
ps_plots = UpperConfidenceBound(final_preprocessed_ps_data, num_of_uniq_genre_ps, 6235)

# Team X-Box
list_of_X_box_genres = []
for current_element in input_arr:
    if current_element[1] == "X360" or current_element[1] == "XB" or current_element[1] == "XONE":
        list_of_X_box_genres.append(current_element[0])

# Deriving the number of unique genres for X_box
set_of_uniq_genre_x_box = set(list_of_X_box_genres)
num_of_uniq_genre_x_box = len(set_of_uniq_genre_x_box)

# Initializing the array
initial_preprocessed_x_box_data = np.zeros((2089, num_of_uniq_genre_ps))

# Generating the preprocessing data (For X-Box)
for i in range(0, 2089):
    j = 0 # Variable to keep track of index
    for gen in set_of_uniq_genre_x_box:
        if list_of_X_box_genres[i] == gen:
            initial_preprocessed_x_box_data[i, j] = 1
            break
        else:
            j += 1
            continue

# Initializing the final preprocessed data
final_preprocessed_x_box_data = initial_preprocessed_x_box_data

# Getting the final plots from the UCB algorithm
x_box_plots = UpperConfidenceBound(final_preprocessed_x_box_data, num_of_uniq_genre_x_box, 2089)

# Plotting the final results
plt.subplot(221)
plt.title("PlayStation")
plt.xlabel("Genre")
plt.ylabel("Selected Amounts")
plt.hist(ps_plots, align='left', color='blue', rwidth=0.8)
plt.subplot(223)
plt.xlabel("Genre\nX-Box")
plt.ylabel("Selected Amounts")
plt.hist(x_box_plots, align='left', color='green', rwidth=0.8)
plt.show() 