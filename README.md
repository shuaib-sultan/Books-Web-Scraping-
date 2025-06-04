# 📘 Books Scraper & Analyzer (v2)

## Overview
This is the second version of a Python-based web scraping project for the website [Books to Scrape](https://books.toscrape.com).  
In this version, we extract and store detailed information about each book and analyze it using **Pandas**.

---

## 🔍 Features
- Scrape multiple pages of books.
- Extract: title, image, detail link, star rating, tax prices, and descriptions.
- Store data into:
  - `allBooks.json`
  - `allBooks.csv`
- Save each book's description in a separate `.txt` file.
- Perform rating & price analysis using **Pandas**:
  - Total & average prices per rating.
  - Most and least expensive books.
  - Count of books by rating.

---

## 📦 Technologies Used
- `requests`
- `BeautifulSoup`
- `pandas`
- `json`
- `urllib.parse`
- `os`

---

## 📂 Project Structure
books-scraper-v2/
│
├── allBooks.json
├── allBooks.csv
├── Descriptions/
│ ├── Book_Title_1.txt
│ └── ...
├── rating_analysis.csv
├── bookScraping.py
└── analysis.py

---

## ▶️ How to Run

```bash
git clone https://github.com/your_username/books-scraper-v2.git
cd books-scraper-v2

pip install -r requirements.txt

python main.py  # to scrape
python analysis.py  # to analyze
```

## 🔮 Future Enhancements
- Add visual charts with matplotlib or seaborn.

- Add CLI options to select page ranges.

- Export HTML report of summaries.

- Add category-based scraping.

## 👨‍💻 Author
Shuaib Sultan
> On my way to becoming a master developer.