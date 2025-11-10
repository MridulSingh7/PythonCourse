import numpy as np
import pandas as pd

np.random.seed(42)

years = np.random.uniform(0.5,10,100).round(2)
salaries = (30000 + years*6000 + np.random.normal(0,4000,size=100)).round(2)

data_frame = pd.DataFrame({
    "YearsExperience":years,
    "Salary":salaries
})

data_frame.to_csv("experience_salary.csv", index=False)
print("data saved in file experience_salary.csv")



'''
day2 :
learned generating dataset from numpy and saving them into csv using pandas

1. np.random.uniform(start,end,amount_of_data) : random data generation -> uniform generation between start, end, total generation
2.normal -> follows gaussian distribution, generates random numbers following gaussian distribution..

created a dataframe -> to describe how to dataset will be genreated in tabular form
'''