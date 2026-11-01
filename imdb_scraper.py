import pandas as pd
import requests
from bs4 import BeautifulSoup


URL = "https://www.imdb.com/chart/top/?ref_=hm_nv_menu"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/144.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.5",
}


def scrape_imdb_top_250():
    response = requests.get(URL, headers=HEADERS, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    box = soup.find(
        "ul",
        class_="ipc-metadata-list ipc-metadata-list--dividers-none "
        "sc-d24d5d37-0 hDHQeM alt_item_colors compact-list-view "
        "ipc-metadata-list--base",
    )

    if box is None:
        raise RuntimeError("IMDb movie list container was not found.")

    movie_names = []
    metadata = []
    ratings = []

    for item in box.find_all("li"):
        title = item.find("h3", class_="ipc-title__text")
        rating = item.find("span", class_="ipc-rating-star--rating")
        meta = item.find(
            "div",
            class_="sc-a55f6282-5 bhUIDq cli-title-metadata",
        )

        if not title or not rating or not meta:
            continue

        spans = meta.find_all(
            "span",
            class_="sc-a55f6282-6 iMumIM cli-title-metadata-item",
        )

        if len(spans) < 3:
            continue

        movie_names.append(title.get_text(strip=True))
        metadata.append(
            (
                spans[0].get_text(strip=True),
                spans[1].get_text(strip=True),
                spans[2].get_text(strip=True),
            )
        )
        ratings.append(rating.get_text(strip=True))

    df = pd.DataFrame(
        {
            "Movie_name": movie_names,
            "Release_date_Time_Rating": metadata,
            "Ratings": ratings,
        }
    )

    df.insert(0, "Rank", range(1, len(df) + 1))
    return df


def main():
    df = scrape_imdb_top_250()
    df.to_csv("data/IMDB_top_250_movies.csv", index=False)

    print(df.head())
    print(f"\nMovies scraped: {len(df)}")


if __name__ == "__main__":
    main()
