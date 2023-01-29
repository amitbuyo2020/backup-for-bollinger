import pandas as pd
technologies = {
            "Spark": [22000,'30days',1000.0],
            "PySpark" : [25000,'50days',2300.0],
            "Hadoop" : [23000,'55days',1500.0]
}
df = pd.DataFrame(technologies)
# print(df)

# Use getitem ([]) to iterate over columns
# for df["Spark","PySpark" ]in df:
#     print(df["Spark"])
#     print(df["PySpark"])

# for (index, Spark, PySpark) in enumerate(df):
#     print(index, df[Spark, PySpark].values)

# for Spark in df.iteritems():
#     # print('{name}: {value}'.format(name=name, value=values[0]))
#     print(df["Spark"])

# for ind, df["Spark"] in enumerate(df.columns):
#     print(df["Spark"])

# for i, row in df.iterrows():                     # Initialize for loop
    # print('Index', i, '- Column Spark:', row['Spark'], '- PySpark:', row['PySpark'])
    # print('Index', i, '- Column Spark:', row['Spark'])
# Index 0 - Column x1: a - Column x2: w
# Index 1 - Column x1: b - Column x2: x
# Index 2 - Column x1: c - Column x2: y
# Index 3 - Column x1: d - Column x2: z


df = pd.DataFrame({'A': [1, 2, None, 4, None], 'B': [6, None, 8, 9, None]})

# Find the last non-NaN value of column 'A' before any non-NaN value in column 'B'
first_valid_index=df['B'].first_valid_index()
last_val = df['A'].iloc[first_valid_index-1] if first_valid_index is not None else None
print(last_val)


# Find the last non-NaN value of column 'A' before any non-NaN value in column 'B'
# first_valid_index=df['B'].first_valid_index()
# last_val = df.at[first_valid_index-1,'A'] if first_valid_index is not None else None
# print(last_val)