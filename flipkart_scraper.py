import pandas as pd
import requests
from bs4 import BeautifulSoup


BASE_URL = (
    "https://www.flipkart.com/search?q=phones+under+25000"
    "&sid=tyy%2C4io&as=on&as-show=on"
    "&otracker=AS_QueryStore_OrganicAutoSuggest_1_16_na_na_na"
    "&otracker1=AS_QueryStore_OrganicAutoSuggest_1_16_na_na_na"
    "&as-pos=1&as-type=HISTORY"
    "&suggestionId=phones+under+25000%7CMobiles"
    "&requestId=693a630d-17b7-4c50-bded-869134edd8ef"
    "&page={page}"
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/144.0.0.0 Safari/537.36"
    )
}

OUTPUT_DIR = "data"


def scrape_flipkart(start_page=2, end_page=9):
    product_names = []
    prices = []
    descriptions = []
    reviews = []

    for page in range(start_page, end_page + 1):
        url = BASE_URL.format(page=page)
        response = requests.get(url, headers=HEADERS, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")
        box = soup.find("div", class_="QSCKDh dLgFEE")

        if box is None:
            print(f"Could not find product container on page {page}.")
            continue

        names = box.find_all("div", class_="RG5Slk")
        prices_on_page = box.find_all("div", class_="hZ3P6w DeU9vF")
        descriptions_on_page = box.find_all("ul", class_="HwRTzP")
        reviews_on_page = box.find_all("div", class_="MKiFS6")

        product_names.extend(item.get_text(strip=True) for item in names)
        prices.extend(item.get_text(strip=True) for item in prices_on_page)
        descriptions.extend(item.get_text(" ", strip=True) for item in descriptions_on_page)
        reviews.extend(item.get_text(strip=True) for item in reviews_on_page)

    row_count = min(
        len(product_names),
        len(prices),
        len(descriptions),
        len(reviews),
    )

    df = pd.DataFrame(
        {
            "Product name": product_names[:row_count],
            "Price": prices[:row_count],
            "Description": descriptions[:row_count],
            "Review": reviews[:row_count],
        }
    )

    if not df.empty:
        df["Price"] = (
            df["Price"]
            .str.replace("₹", "", regex=False)
            .str.replace(",", "", regex=False)
            .astype(int)
        )
        df["Brand"] = df["Product name"].str.split().str[0]

    return df


def main():
    df = scrape_flipkart()

    average_price_by_brand = (
        df.groupby("Brand")["Price"].mean().sort_values(ascending=True).round(2)
    )

    df.to_csv(f"{OUTPUT_DIR}/Flipkart_Phones_under_25000.csv", index=False)
    average_price_by_brand.to_csv(
        f"{OUTPUT_DIR}/average_price_of_brands.csv",
        header=["Average Price"],
    )

    print(df.head())
    print("\nAverage price by brand:")
    print(average_price_by_brand)


if __name__ == "__main__":
    main()
