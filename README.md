# ScraperBot

**ScraperBot** is a versatile Python script that scrapes book information from the [Books to Scrape](https://books.toscrape.com/) website. With minimal adjustments, it can be extended to scrape data from any website. The script utilizes Selenium for web automation and BeautifulSoup for parsing HTML, making it easy to extract various types of data.

## Features

- Scrapes book information, including titles and prices, from multiple pages.
- Saves the scraped data into a CSV file for convenient analysis.
- Easily customizable to adapt to different websites by modifying URL patterns and HTML elements.

## Prerequisites

- Python 3.x installed on your system.
- `chromedriver` corresponding to your Chrome version. [Download here](https://developer.chrome.com/docs/chromedriver/downloads).
- Required Python libraries:
  - Selenium
  - BeautifulSoup
  - Pandas

You can install the required libraries using the following command:

```bash
pip install selenium beautifulsoup4 Pandas
```

## Usage

1. Clone this repository or download the code files.
2. Ensure `chromedriver.exe` is in the same directory as the script or update the path in the code.
3. Run the script:

```bash
python bookScraper.py
```

4. The scraped book data will be saved to `ScrapedBooks.csv` in the same directory.

## Example Output

After running the script, the output will be saved in `ScrapedBooks.csv` and will contain data formatted as follows:

```
Title, Price, Availability
A Light in the Attic, 51.77, In Stock
Tipping the Velvet, 53.74, Out of Stock
...
```

## Extending to Other Websites

To adapt Scraper Bot for different websites:
- Modify the `base_url` to match the target site's URL structure.
- Change the variable and function names to something suitable
- Update the HTML elements in the `get_book` function to extract the desired data points.



## License

[MIT License](https://opensource.org/license/mit).
