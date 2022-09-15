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
#finding the differences betwween the first week of data and the last week of data and using it to find the forecasting for subsequent weeks
len(flows)
first_3_weeks_of_flow = flows[:21]
last_3_weeks_of_flow = flows[-21:]
print(first_3_weeks_of_flow)
print(last_3_weeks_of_flow)
#%%
#goal: using numpy to generate prediction variables
week1_prediction = np.mean(first_3_weeks_of_flow)
week2_prediction = np.mean(last_3_weeks_of_flow)
print(week1_prediction, ',', week2_prediction)
# %%
#%%
#findng the median values
med = np.median(flows)
medval_1 = week1_prediction - med
medval_2 = week2_prediction - med
print(medval_1, ',', medval_2)
# %%
