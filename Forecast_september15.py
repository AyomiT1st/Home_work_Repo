#%%
import numpy as np

filename =('https://raw.githubusercontent.com/HAS-Tools-Fall2022'
           '/Course-Materials22/main/data/verde_river_daily_flow_cfs.csv')
flows = np.loadtxt(
    filename, # The location of the text file
    delimiter=',', # character which splits data into groups
    usecols=1 # Just take column 1, which is the flows
)
print(flows)

#%%
#finding the differences betwweeb=n the first week of data and the last week of data and using it to find the forecasting for subsequent weeks
len(flows)
first_day = flows[0]
last_day = flows[-1]
total_change = last_day - first_day
print(total_change)
#%%
#goal: using numpy to generate prediction variables
week1_prediction = np.mean(flows) - total_change
week2_prediction = np.mean(flows) - 2*total_change
week3_prediction = np.mean(flows) - 3*total_change
print(week1_prediction, ',', week2_prediction, ',', week3_prediction)
# %%
