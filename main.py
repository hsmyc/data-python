import pandas as pd

# from json  and sql
# pd.read_json() and pd.read_sql() respectively
# read the data without header
df_without_header = pd.read_csv('data.csv', header=None)

df_head = pd.read_csv('data.csv').head(5)  # read the first 5 rows of the data
df_tail = pd.read_csv('data.csv').tail(5)  # read the last 5 rows of the data
df = pd.read_csv('data.csv')
print(df.dtypes)  # print the data types of the columns
