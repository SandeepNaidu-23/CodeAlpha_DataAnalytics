import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

data = []

for page in range(1, 51):

    url = base_url.format(page)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        availability = book.find(
            "p",
            class_="instock availability"
        ).text.strip()

        rating = book.p["class"][1]

        data.append([
            title,
            price,
            rating,
            availability
        ])

    print(f"Page {page} scraped")

df = pd.DataFrame(
    data,
    columns=[
        "Title",
        "Price",
        "Rating",
        "Availability"
    ]
)

df.to_csv("books_data.csv", index=False)

print("\nTotal Books Scraped:", len(df))
print("Dataset saved successfully!")