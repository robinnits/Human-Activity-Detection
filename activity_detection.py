import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

train_data = pd.read_csv("train.csv")  # Change filename if needed
test_data = pd.read_csv("test.csv")

y_train = train_data.iloc[:, -1]
X_train = train_data.iloc[:, :-1]
y_test = test_data.iloc[:, -1]
X_test = test_data.iloc[:, :-1]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
