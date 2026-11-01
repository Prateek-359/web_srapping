# Web Scraping Projects with Python

This repository contains my Python web-scraping practice projects using **Requests, BeautifulSoup, Pandas, and Matplotlib**.

## Projects

### 1. BeautifulSoup Local HTML Practice
- `home.html` contains sample course cards.
- `html_parser.py` reads the HTML file and extracts course names and prices using BeautifulSoup.

### 2. Flipkart Phones Under ₹25,000
- `flipkart_scraper.py` sends requests to Flipkart search pages.
- BeautifulSoup extracts product name, price, description, and review information.
- Pandas stores the scraped data in a DataFrame.
- The script also calculates the average phone price by brand.
- Output files:
  - `data/Flipkart_Phones_under_25000.csv`
  - `data/average_price_of_brands.csv`

### 3. IMDb Top 250 Movies
- `imdb_scraper.py` requests the IMDb Top 250 page.
- BeautifulSoup extracts movie name, year, duration, age rating, and IMDb rating.
- Pandas saves the result to:
  - `data/IMDB_top_250_movies.csv`

## Technologies Used

- Python
- Requests
- BeautifulSoup
- lxml
- Pandas
- Matplotlib
- CSV

## Project Structure

```text
web-scraping-project/
│
├── data/
│   ├── average_price_of_brands.csv
│   ├── Flipkart_Phones_under_25000.csv
│   └── IMDB_top_250_movies.csv
│
├── home.html
├── html_parser.py
├── flipkart_scraper.py
├── imdb_scraper.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd web-scraping-project
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Ubuntu/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Programs

### Local HTML parser

```bash
python html_parser.py
```

Expected output is similar to:

```text
Python for beginners costs 20$
Python Web Development costs 50$
Python Machine Learning costs 100$
```

### Flipkart scraper

```bash
python flipkart_scraper.py
```

This creates/updates the CSV files inside the `data` folder.

### IMDb scraper

```bash
python imdb_scraper.py
```

This creates/updates `data/IMDB_top_250_movies.csv`.

## Important Note

Websites can change their HTML structure, CSS classes, anti-bot protection, or access rules. Therefore, a scraper that works today may need changes later. Use scraping responsibly and follow the website's terms and applicable policies.

## What I Learned

- Sending HTTP requests with `requests`
- Parsing HTML using BeautifulSoup
- Finding elements with tags and CSS classes
- Extracting text from web pages
- Cleaning price data
- Creating Pandas DataFrames
- Grouping and calculating average prices
- Exporting data to CSV
- Working with web-scraping project files and Git/GitHub
