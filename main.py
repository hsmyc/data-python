import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# from json  and sql
# pd.read_json() and pd.read_sql() respectively
# read the data without header
df_without_header = pd.read_csv('data.csv', header=None)

df_head = pd.read_csv('data.csv').head(5)  # read the first 5 rows of the data
df_tail = pd.read_csv('data.csv').tail(5)  # read the last 5 rows of the data
df = pd.read_csv('data.csv')
# get first column
df_first_column = df.iloc[:, 0]
# get second column
df_second_column = df.iloc[:, 1]
plt.scatter(df_first_column, df_second_column)
plt.show()


# print(df.dtypes)  # print the data types of the columns

# df.dropna()  # drop the rows with missing values
# df.fillna(0)  # fill the missing values with 0

# df.astype(str)  # convert the data types of the columns to string

# # create 10 equally spaced values between the min and max of the column
# np.linspace(min(df('column_name')), max(df('column_name')), 10)

# # group the data by the column name
# df.groupby('column_name')

# # sort the data by the column name
# df.sort_values('column_name')

# # find mean of the column
# df.mean()

# # pivot the data
# df.pivot(index='column_name', columns='column_name', values='column_name')

# # heatmap
# plt.imshow(df.corr(), cmap='hot', interpolation='nearest')
