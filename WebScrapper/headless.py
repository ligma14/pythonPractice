import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class WebScraper:
    def __init__(self, headless=True):
        # Configure options for the WebDriver
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Initialize WebDriver using WebDriver Manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def fetch_page(self, url):
        """Fetches a webpage by URL."""
        self.driver.get(url)

    def scrape_table(self, table_selector, cell_selector):
        try:
            table = self.driver.find_element(By.CSS_SELECTOR, table_selector)
            headers = [header.text for header in table.find_elements(By.TAG_NAME, "th")]
            rows = table.find_elements(By.TAG_NAME, "tr")

            table_data = []
            for row in rows[1:]:  # Skip the header row
                cells = row.find_elements(By.CSS_SELECTOR, cell_selector)
                row_data = {headers[i]: cells[i].text for i in range(len(cells))}
                table_data.append(row_data)

            return table_data
        except Exception as e:
            print(f"Error scraping table: {e}")
            return None

    def save_to_csv(self, data, filename):
        if data:
            try:
                with open(filename, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)
                print(f"Data successfully saved to {filename}")
            except Exception as e:
                print(f"Error saving data to CSV: {e}")
        else:
            print("No data to save.")

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    # Example usage
    url = "https://rfspager.app/pager"  # Replace with the actual URL containing a table
    table_selector = ".table-auto"  # Replace with the appropriate CSS selector for your table
    csv_filename = "scraped_data.csv"  # Output CSV file name
    cell_selector = "tr .py-3.px-3"  # Replace with the appropriate CSS selector for your table cells

    scraper = WebScraper(headless=True)
    scraper.fetch_page(url)
    
    # Scrape the table
    table_data = scraper.scrape_table(table_selector, cell_selector)
    if table_data:
        scraper.save_to_csv(table_data, csv_filename)

    scraper.close()
