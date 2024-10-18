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

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
max_number = 3

def get_book(url):
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    book_data = []
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text[2:].strip()
        availability = book.find('p', class_='instock availability').text.strip()
        book_data.append([title, price, availability])
    return book_data

def scrape_pages():
    page_number = 1
    all_books = []
    while True:
        print(f"Scraping page {page_number}")
        current_url = base_url.format(page_number)
        books = get_book(current_url)
        all_books.extend(books)

        if len(books) == 0:
            print("No more books found.")
            break
        if page_number >= max_number:
            print(f"Reached the maximum number of pages: {max_number}")
            break
        page_number += 1    
    return all_books

def display_books(book_data):
    for book in book_data:
        title, price, availability = book
        print(f"Title: {title}\nPrice: {price}\nAvailability: {availability}\n")

def write_to_csv(book_data):
    with open('scrapedBooks.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Availability'])
        for book in book_data:
            writer.writerow(book)

if __name__ == "__main__":
    all_books = scrape_pages() 
    display_books(all_books)
    write_to_csv(all_books)
driver.quit()
