import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class TestBooksToScrape(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.service = Service(executable_path="chromedriver.exe")
        cls.driver = webdriver.Chrome(service=cls.service)

    def test_page_title(self):
        self.driver.get("https://books.toscrape.com/")
        title = self.driver.title
        self.assertEqual(title, "Books to Scrape")

    def test_pagination(self):
        self.driver.get("https://books.toscrape.com/catalogue/page-2.html")
        self.assertEqual(self.driver.title, "Books to Scrape - page 2")

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
