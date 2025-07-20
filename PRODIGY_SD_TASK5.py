#demo inputs:
# 1.Enter the URL of the website to scrape:
# > https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops

# Enter the fields and their CSS selectors:
# > title=.title
# > price=.price
# > rating=.ratings
# > done
#
# 2. Enter the URL of the website to scrape:
# > https://www.scrapethissite.com/pages/simple/

#  Enter the fields and their CSS selectors (e.g., title=.product_title)
#  Type 'done' when you're finished.

# > country=.country-name
# > capital=.country-capital
# > population=.country-population
# > area=.country-area
# > done
import requests
import time
import csv
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def is_bot_protected(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            print("✅ Site is accessible. No bot protection detected.")
            return False
        elif response.status_code in [403, 503]:
            print(f"🚫 Access blocked with status code: {response.status_code}.")
            return True
        elif "captcha" in response.text.lower():
            print("⚠️ CAPTCHA detected in response content.")
            return True
        else:
            print(f"⚠️ Received unusual status code: {response.status_code}")
            return True
    except requests.exceptions.RequestException as e:
        print(f"❌ Error connecting to the site: {e}")
        return True

def scrape_generic(url, field_map):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    print("🌐 Loading page...")
    driver.get(url)
    time.sleep(3)

    data = {}
    for field, selector in field_map.items():
        try:
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            data[field] = [el.text.strip() for el in elements]
        except Exception as e:
            print(f"❌ Could not find field '{field}': {e}")
            data[field] = []

    # Combine into rows
    combined = []
    row_count = max(len(values) for values in data.values())

    for i in range(row_count):
        row = {}
        for field, values in data.items():
            row[field] = values[i] if i < len(values) else ""
        combined.append(row)

    driver.quit()
    return combined

def export_to_csv(data, filename="scraped_data.csv"):
    if not data:
        print("⚠️ No data to write.")
        return

    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            for row in data:
                writer.writerow(row)

        print(f"\n✅ Data exported successfully to: {os.path.abspath(filename)}")
    except Exception as e:
        print(f"❌ Failed to write CSV: {e}")

def get_user_input():
    print("🔍 Web Scraping Assistant\n")
    url = input(" Enter the URL of the website to scrape:\n> ").strip()

    print("\n Enter the fields and their CSS selectors (e.g., title=.product_title)")
    print(" Type 'done' when you're finished.\n")

    field_map = {}
    while True:
        entry = input("> ").strip()
        if entry.lower() == "done":
            break
        if "=" in entry:
            field, selector = entry.split("=", 1)
            field_map[field.strip()] = selector.strip()
        else:
            print("❌ Invalid format. Use field=selector")

    return url, field_map

if __name__ == "__main__":
    url, fields = get_user_input()
    print(f"\n✅ URL to scrape: {url}")
    print(f"✅ Fields to extract: {fields}")

    print("\n🔍 Checking for bot protection...\n")
    blocked = is_bot_protected(url)

    if blocked:
        print("❌ Cannot continue. The site may be bot-protected.")
    else:
        print("🚀 Proceeding to scrape...\n")
        scraped_data = scrape_generic(url, fields)

        if not scraped_data:
            print("⚠️ No matching data found for the requested fields.")
        else:
            for i, item in enumerate(scraped_data, start=1):
                print(f"\n ~ Item {i}:")
                for key, value in item.items():
                    print(f"  {key.title()}: {value}")

            save = input("\n Do you want to save the data to a CSV file? (yes/no): ").strip().lower()
            if save in ["yes", "y"]:
                export_to_csv(scraped_data)
