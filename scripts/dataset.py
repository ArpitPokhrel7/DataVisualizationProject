import pandas as pd

# URL for Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# Load the dataset into a DataFrame
titanic_data = pd.read_csv(url)

# Save it locally (optional)
titanic_data.to_csv("titanic.csv", index=False)

print(titanic_data.head())  # Display the first few rows
