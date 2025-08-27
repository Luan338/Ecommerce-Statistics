# Library Imports: pandas, numpy, matplotlib, seaborn
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;
import seaborn as sns;

# Import Data Source: Ecommerce Statistics.csv
df = pd.read_csv('ecommerce_estatistica.csv');

# 01) Data Reading and Cleaning
print('Initial view of the data (head):');
print(df.head());
print('\n');

print('Dataframe Information (info):');
print(df.info());
print('\n');

print('Count missing values by column:');
print(df.isnull().sum());
print('\n');

print(f"\nDataFrame {df.shape[0]} lines and {df.shape[1]} columns.")
# ////////////////////////////////////////////////////////////////////////////////////////////////

# 02) Detailed Analysis


