import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("E:/programming/DataVisualizationProject/data/titanic.csv")


# Handle missing values
data['Age'].fillna(data['Age'].mean(), inplace=True)

# Create a visualization: Survival rate by gender
sns.countplot(data=data, x='Survived', hue='Sex')
plt.title('Survival Rate by Gender')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.savefig('../images/survival_by_gender.png')  # Save visualization
plt.show()
