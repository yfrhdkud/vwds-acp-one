import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

missingVs = ["N/a", "na", np.nan]
df = pd.read_csv("Penguins Data.csv",na_values=missingVs)

print(df.head(10))
print(df.isnull().sum())

plt.figure(figsize=(12,5))
sns.heatmap(df.isnull(), cbar = False, cmap = "viridis")
plt.show()

def fill_na():
    
    for col in df.select_dtypes(include=['object']):
        df[col] = df[col].fillna("Unknown")

    for col in df.select_dtypes(include=['float64', 'int64']):
        df[col] = df[col].interpolate(method='linear', limit_direction='both')

fill_na()  
print(df.head(10))