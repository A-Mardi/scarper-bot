import unittest
from unittest.mock import patch 
from bs4 import BeautifulSoup
from bookScraper import get_book

class TestBookScraper(unittest.TestCase):
    def setUp(self):
        self.mock_html = """ 
        <html>
            <body>
                <article class='product_pod'>
                    <h3><a title="Test Book Title"></a></h3>
                    <p class='price_color'>£@20.00</p>
                    <p class='instock availability'>In stock</p>
                </article>
            </body>
        </html> 
        """
    @patch('bookScraper.driver')
    def test_get_book(self, mock_driver):
        mock_driver.page_source = self.mock_html
        soup = BeautifulSoup(mock_driver.page_source, 'html.parser')
        books = soup.find_all('article', class_='product_pod')

        self.assertEqual(len(books), 1)
        title = books[0].h3.a['title']
        price = books[0].find('p', class_='price_color').text[2:].strip()
        availability = books[0].find('p', class_='instock availability').text.strip()

        self.assertEqual(title, "Test Book Title")
        self.assertEqual(price, "20.00")
        self.assertEqual(availability, "In stock")


if __name__ == "__main__":
    unittest.main()
