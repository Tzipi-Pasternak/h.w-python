import pandas as pd

df = pd.read_csv('cities.csv')
print(df.head())

print(df.isnull().sum())

for column in df.columns:
    if df[column].isnull().any():
        if pd.api.types.is_numeric_dtype(df[column]):
            mean_val = df[column].mean()
            df[column] = df[column].fillna(mean_val)
        else:
            df[column] = df[column].fillna("0")

df.drop_duplicates(inplace=True)

df.columns = df.columns.str.strip().str.replace('"', '').str.replace("'", '')

average_latitude = df.groupby('State')['Population'].mean()

max_city = df.loc[df['Population'].idxmax()]

min_city = df.loc[df['Population'].idxmin()]


df['Density'] = df['Population'] / df['Area']

print(df.head())

df.rename(columns={'Population': 'Population'}, inplace=True)
