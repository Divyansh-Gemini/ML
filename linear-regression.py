import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import httpx

# ---------------------------------------- GET DATASET ----------------------------------------

# path of dataset
path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"

# function to download dataset
def download(url, filename):
    with httpx.Client() as client:
        response = client.get(url)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
        else:
            print(f"Failed to download {url}. Status code: {response.status_code}")

download(path, "dataset/FuelConsumption.csv")
path = "FuelConsumption.csv"

# getting data as Pandas DataFrame from CSV
df = pd.read_csv(path)

# ---------------------------------------- UNDERSTAND DATASET ----------------------------------------

# take a look at the dataset
print(df.head())

# summarize the data
print(df.describe())

# select some features to explore more
cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
print(cdf.head(9))

# plot each feature
# viz = cdf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
# viz.hist()
# plt.show()

# plot relationship of Fuel Consumption Comb against CO2 Emission
# plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS, color='blue')
# plt.xlabel("Fuel Consumption Comb")
# plt.ylabel("Emission")
# plt.show()

# plot relationship of Engine Size against CO2 Emission
# plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color='blue')
# plt.xlabel("Engine Size")
# plt.ylabel("Emission")
# plt.show()

# plot relationship of Cylinders against CO2 Emission
# plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS, color='blue')
# plt.xlabel("Cylinders")
# plt.ylabel("Emission")
# plt.show()

# ---------------------------------------- TRAIN-TEST SPLIT ----------------------------------------

# perform train-test split (8:2)
msk = np.random.rand(len(cdf)) < 0.8
train = cdf[msk]
test = cdf[~msk]

# plot relationship of engine size against CO2 Emission in train & test dataset in different color
# plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue')
# plt.scatter(test.ENGINESIZE, test.CO2EMISSIONS, color='red')
# plt.show()

# ---------------------------------------- MODELLING ----------------------------------------

# create linear regression model
from sklearn import linear_model
regr = linear_model.LinearRegression()

# get x & y variables for training
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])

# fit line of regression
regr.fit(train_x, train_y)

# print coefficient (slope) & intercept
print('Coefficient: ', regr.coef_)
print('Intercept: ', regr.intercept_)

# plot line of regression
# plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue')
# plt.plot(train_x, regr.coef_[0][0] * train_x + regr.intercept_[0], '-k')
# plt.xlabel('Engine Size')
# plt.ylabel('CO2 Emissions')
# plt.show()

# ---------------------------------------- EVALUATION ----------------------------------------
from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])      # actual y
test_y_ = regr.predict(test_x)                      # predicted y

print('MAE: ', format(np.mean(np.absolute(test_y_ - test_y)), '.2f'))
print('MSE: ' , format(np.mean(np.absolute(test_y_ - test_y) ** 2), '.2f'))
print('R2-Score: ', format(r2_score(test_y, test_y_), '.2f'))