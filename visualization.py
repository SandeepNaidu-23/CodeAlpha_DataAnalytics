import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_data.csv")

# Clean price column
df["Price"] = (
    df["Price"]
    .str.replace("Â£", "", regex=False)
    .astype(float)
)

# Rating Distribution
plt.figure(figsize=(8, 5))

df["Rating"].value_counts().plot(kind="bar")

plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig("rating_distribution.png")

plt.show()

# Price Distribution
plt.figure(figsize=(8, 5))

plt.hist(df["Price"], bins=15)

plt.title("Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("price_distribution.png")

plt.show()

print("Charts created successfully!")