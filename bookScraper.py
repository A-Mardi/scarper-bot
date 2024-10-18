from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv  
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

base_url = "https://books.toscrape.com/"
max_number = 3

def get_book(url):
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    book_data = []
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        book_data.append([title, price, availability])
    return book_data

