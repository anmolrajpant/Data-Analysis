import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
from sklearn.preprocessing import LabelEncoder
from math import *

#Importing CSV file to Python
file = pd.read_csv("bank_campaign.csv", sep=';')

#Trasfering variable Yes to 1 and No to 0 in Y(2a)
column_var = ['housing', 'default', 'loan', 'y']
label_enc = LabelEncoder()
for i in column_var:
    file[i] = label_enc.fit_transform(file[i])
print(file)

#Transfering variable job, deucation, marital, contact, month and poutcome to ordinal number(2b)
column_var = ['job', 'education', 'marital', 'contact', 'month', 'poutcome']
label_enc = LabelEncoder()
for i in column_var:
    file[i] = label_enc.fit_transform(file[i])
print(file)

#New age_category based on age(2c)
age_group = [17, 19, 25, 30, 35, 40, 49, 59, 69, 79, 100]
group_names = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
file["age_category"] = pd.cut(file["age"], age_group, labels = group_names)
print(file)

#Convert seconds to minutes(2d)
file_minute = file["duration"]/60
print(file_minute)
#Create new durations_minutes based on duration
file.insert(12, "duration_minutes", file_minute)
print(file.head())

#Statistics of Sum, Mean, SD, Skewness and Kurtosis of Duration
print("Sum:")
print(file["duration"].sum())

print(file["duration"].mean())

print(file["duration"].std())

print(file["duration"].skew())

print(file["duration"].kurt())

#Calculate and show Correlation with Graph
sort = file.corr().sort_values('age', ascending=False)
print(sort)

sea.set(style = "ticks")
plt.figure(figsize = (12,8))
corr = file.corr()
sea.heatmap(corr, cmap='PuBuGn', linewidths=0.8, xticklabels = corr.columns, yticklabels = corr.columns)
plt.show()

first_client = file.iloc[22222].tolist()
print(first_client)

second_client = file.iloc[33333].tolist()
print(second_client)

result = zip(first_client, second_client)
final_result = list(result)
print(final_result)

#Euclidean Distance
print(sqrt(sum(pow(x-y, 2) for x, y in zip(first_client, second_client))))
#Manhattan Distance
print(sum(abs(x-y) for x, y in zip(first_client, second_client)))
# print(file.head())

#Show histogram plot of Balance and Frequency
file["education"].hist(bins = 50)
plt.xlabel("education")
plt.ylabel("frequency")
plt.title("Education Frequency in DataSet")
plt.legend("Education")
plt.show()

file["housing"].hist(bins = 50)
plt.xlabel("housing")
plt.ylabel("frequency")
plt.title("Housing Frequency in DataSet")
plt.legend("Housing")
plt.show()

updatedFile = pd.read_csv("bank_campaign.csv", sep = ';')
print(updatedFile)

updatedFile = updatedFile[updatedFile.y=='yes']
print(updatedFile)

print(updatedFile['job'].value_counts())

#Show Bar Graph of Total number of Clients with term deposite
plt.style.use('ggplot')
plt.figure(figsize = (10, 8))
updatedFile['job'].value_counts().plot(kind = 'bar')
plt.title("Jobs of The Subscribed Customers")
plt.ylabel("Number")
plt.xlabel("Job Types")
plt.figure(figsize = (10, 8))
plt.show()  