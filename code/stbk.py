import pandas as pd
import numpy as np

df = pd.read_csv("D:\proj\starbuck-store\data\directory.csv")

print("Dataset shape:", df.shape)
print("\nFirst few rows:")
print(df.head())
print("\nDataset info:")
df.info()

df = df[
    ["Store Name", "City", "Country", "Ownership Type", "Latitude", "Longitude"]
]

import pandas as pd

df = df.drop_duplicates()
print(f"\nDuplicates removed. New shape: {df.shape}")

print("\nMissing values before cleaning:")
print(df.isnull().sum())

text_cols = ["Store Name", "City", "Country", "Ownership Type"]
for col in text_cols:
    df[col] = df[col].astype(str).str.strip()

df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")

df = df.dropna(subset=["Store Name", "City", "Country", "Latitude", "Longitude"])

df = df[
    (df["Latitude"].between(-90, 90)) &
    (df["Longitude"].between(-180, 180))
]

df["Country"] = df["Country"].str.lower()
df["Ownership Type"] = df["Ownership Type"].str.lower()

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print(f"\nCleaned dataset shape: {df.shape}")
print("\nFinal cleaned data:")
print(df.head(10))

df.to_excel("D:\proj\starbuck-store\data\directory_cleaned.xlsx", index=False)
print("\nCleaned data saved to directory_cleaned.xlsx")