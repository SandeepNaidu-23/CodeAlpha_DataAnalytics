import pandas as pd

# Load dataset
df = pd.read_csv("books_data.csv")

print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)

print("\nShape of Dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nRating Distribution:")
print(df["Rating"].value_counts())

print("\nAvailability Distribution:")
print(df["Availability"].value_counts())

print("\nUnique Ratings:")
print(df["Rating"].unique())