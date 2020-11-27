# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Common Data Preprocessing
dataset = pd.read_csv('vgsales.csv')

# Getting the Round Specific values (Publisher Vs Console)
publisher = dataset['Publisher'].values
console = dataset['Platform'].values

# Splitting the data into viable histograms

# Calculating the number of unique values
console_set = set(console)
num_of_unique_consoles = len(console_set) # 31 Unique Consoles


# Plotting the results
# 4, 5, 6, 11, 12, 13, 15, 16
plt.xlabel("Console\nBlue: Play Station\nGreen: X-Box")
plt.ylabel("Probability Density Of Volume")
plt.hist(console, bins=[4, 5], align='left', rwidth=0.8, color='green')
plt.hist(console, bins=[5, 6], align='left', rwidth=0.8, color='blue')
plt.hist(console, bins=[6, 7], align='left', rwidth=0.8, color='blue')
plt.hist(console, bins=[10, 11], align='left', rwidth=0.8, color='blue')
plt.hist(console, bins=[12, 13], align='left', rwidth=0.8, color='blue')
plt.hist(console, bins=[13, 14], align='left', rwidth=0.8, color='green')
plt.hist(console, bins=[16, 17], align='left', rwidth=0.8, color='blue')
plt.hist(console, bins=[17, 18], align='left', rwidth=0.8, color='green')

# Deriving a more personalized result
publishers_set = set(publisher)
num_of_unique_publishers = len(publishers_set)

# Deducing publisher specific results
combined_arr = np.concatenate((publisher.reshape(-1, 1), console.reshape(-1, 1)), 1)
# Initializing the total variables
num_of_XBOX = 0
num_of_PS = 0
# Getting a dictionary of Publisher & Console
list_of_pub_con = []
for i in range(0, len(publisher)):
    if combined_arr[i, 1] == 'X360':
        num_of_XBOX += 1
        list_of_pub_con.append({"Publisher": combined_arr[i, 0], "Console": "XBOX"})
    elif combined_arr[i, 1] == 'PS3':
        num_of_PS += 1
        list_of_pub_con.append({"Publisher": combined_arr[i, 0], "Console": "PS"})
    elif combined_arr[i, 1] == 'PS2':
        num_of_PS += 1
        list_of_pub_con.append({"Publisher": combined_arr[i, 0], "Console": "PS"})
    elif combined_arr[i, 1] == 'PS4':
        num_of_PS += 1
        list_of_pub_con.append({"Publisher": combined_arr[i, 0], "Console": "PS"})
    elif combined_arr[i, 1] == 'PS':
        num_of_PS += 1
        list_of_pub_con.append({"Publisher": combined_arr[i, 0], "Console": "PS"})
    elif combined_arr[i, 1] == 'XB':
        num_of_XBOX += 1
        list_of_pub_con.append({"Publisher": combined_arr[i, 0], "Console": "XBOX"})
    elif combined_arr[i, 1] == 'PSP':
        num_of_PS += 1
    elif combined_arr[i, 1] == 'XONE':
        num_of_XBOX += 1
        list_of_pub_con.append({"Publisher": combined_arr[i, 0], "Console": "XBOX"})
        
# Extracting publisher with console
final_publisher_console_relation_list = []
for target_publisher in publishers_set:
    num_of_xbox = 0
    num_of_ps = 0
    for inner_dict in list_of_pub_con:
        if inner_dict.get("Publisher") == target_publisher:
            curr_console = inner_dict.get("Console")
            if curr_console == "XBOX":
                num_of_xbox +=1
            else:
                num_of_ps +=1
    if num_of_xbox == 0 and num_of_ps == 0:
        continue
    else:
        final_publisher_console_relation_list.append({"Publisher": target_publisher, "Console_XBOX": num_of_xbox, "Console_PS": num_of_ps})
            
# Making the final list of values
publisher_display = []
consoleXBOX_display = []
consolePS_display = []
for x in final_publisher_console_relation_list:
    publisher_display.append(x.get("Publisher"))
    consoleXBOX_display.append(x.get("Console_XBOX"))
    consolePS_display.append(x.get("Console_PS"))

# Note: 140 Publishers use either XBOX or Playstation
# Converting list to array
publisher_display = np.array(publisher_display).reshape(-1, 1)
consoleXBOX_display = np.array(consoleXBOX_display).reshape(-1, 1)
consolePS_display = np.array(consolePS_display).reshape(-1, 1)

# Merging the list
final_arr = np.concatenate((publisher_display, consoleXBOX_display, consolePS_display), 1)  

# Getting the top 5
final_list = final_arr[:200]

# Plotting the top 5
final_list_publis = final_list[:, 0]
final_list_x_box = final_list[:, 1]
final_list_ps= final_list[:, 2]
plt.plot(final_list_publis, final_list_x_box, color='green', label='X-Box')
plt.plot(final_list_publis, final_list_ps, color='blue', label='Play Station')
plt.legend()
plt.show() 
    


