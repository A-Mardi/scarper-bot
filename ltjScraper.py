# London Tech Jobs Scraper for intern, coop, positions

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Initialize the WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
max_number = 7

# URL of the job listings page
base_url = "https://londontechjobs.ca/JobList.aspx?page={}&size=50&ord=1"

def get_jobs(url):
    driver.get(url)
    time.sleep(3)  # Let the page load; you can adjust or use explicit waits

    # Extract the job cards
    job_cards = driver.find_elements(By.CLASS_NAME, "gm-card")
    job_data = []

    # Loop through each job card
    for job_card in job_cards:
        try:
            # Get job title and check if it matches "intern", "co-op", or "coop"
            title_element = job_card.find_element(By.CLASS_NAME, "gm-card-title")
            title = title_element.text.lower()
            if "intern" in title or "co-op" in title or "coop" in title:
                
                # Extract other relevant details
                job_link = job_card.find_element(By.CLASS_NAME, "gm-card-link").get_attribute('href')
                company_name = job_card.find_element(By.CLASS_NAME, "gm-card-subtitle").text
                location = job_card.find_element(By.XPATH, './/i[@class="fa fa-map-marker"]/following-sibling::text()').strip()
                date_posted = job_card.find_element(By.CLASS_NAME, "gm-card-timestamp").text
                
                # Append job details to the list
                job_data.append([title, company_name, location, date_posted, job_link])

        except Exception as e:
            print(f"Error extracting job details: {e}")

    return job_data

def scrape_pages():
    page_number = 1
    all_jobs = []

    while True:
        print(f"Scraping page {page_number}")
        current_url = base_url.format(page_number)
        jobs = get_jobs(current_url)
        all_jobs.extend(jobs)
        
        if not jobs:
            print("No more jobs found. Ending scrape.")
            break
        if page_number >= max_number:
            print(f"Reached the maximum number of pages: {max_number}")
            break
        page_number += 1  # Move to the next page

    return all_jobs


def write_to_csv(job_data):
    with open('filteredJobs.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Company', 'Location', 'Date Posted', 'job_link'])
        for job in job_data:
            writer.writerow(job)

if __name__ == "__main__":
    all_jobs = scrape_pages() 
    write_to_csv(all_jobs)
    print("Scraping complete. Job data saved to 'filteredJobs.csv'")
