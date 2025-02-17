import pandas as pd

test_x_path = "UCI HAR Dataset/test/X_test.txt"
test_y_path = "UCI HAR Dataset/test/y_test.txt"

X_test = pd.read_csv(test_x_path, sep='\s+', header=None)
y_test = pd.read_csv(test_y_path, sep='\s+', header=None)

test_data = pd.concat([X_test, y_test], axis=1)
test_data.to_csv("test.csv", index=False)
print("✅ test.csv saved successfully!")
