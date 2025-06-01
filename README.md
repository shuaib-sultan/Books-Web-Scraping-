# Books Web Scraping Project 📚

## About the Project
This project is a web scraping script built using **Python**, which scrapes data from [Books to Scrape](https://books.toscrape.com), extracts relevant information about each book (title, image URL, detail page link, and rating), and performs data analysis using **Pandas**.

The extracted data is saved into:
- `allBooks.csv`
- `allBooks.json`

And then filtered into:
- `five_rate.csv`: books with a rating of 5 stars.
- `under_three_rate.csv`: books with a rating less than 3 stars.

---

## Features
- Scrape multiple pages (50 total) of books.
- Extract book title, rating, cover image, and link.
- Save the data in CSV and JSON formats.
- Analyze ratings using Pandas.
- Filter and export highly-rated and low-rated books.

---

## Technologies Used
- `requests`
- `BeautifulSoup`
- `pandas`
- `json`
- `urllib.parse`

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/your_username/books-scraper.git
cd books-scraper

# Install dependencies
pip install -r requirements.txt

# Run the script
python main.py
```
## Future Improvements
- Add graphical analysis using matplotlib or seaborn.

- Handle price and availability data (if available).

- Export a summary report of ratings.
## 👨‍💻 Author
shuaib-sultan >in my way to master Developer
> this my first project with this organizetion .