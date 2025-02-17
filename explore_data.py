import pandas as pd

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

print("Train Data Shape:", train.shape)
print("Test Data Shape:", test.shape)

print(train.head())
print(test.head())
