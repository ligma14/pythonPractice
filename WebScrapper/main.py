import requests, csv
from bs4 import BeautifulSoup
from typing import List, Dict, Optional

class WebScraper:
    def __init__(self, headers: Optional[Dict[str, str]] = None):
        self.headers = headers or {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def fetch_page(self, url: str) -> Optional[BeautifulSoup]:
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raises HTTPError, if one occurred
            return BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"General error occurred: {req_err}")
        return None
    
    def scrape_table(self, soup: BeautifulSoup, selector: str) -> List[Dict[str, str]]:
        table_data = []
        try:
            table = soup.select_one(selector)
            if table is None:
                print(f"Table not found with selector: {selector}")
                return table_data
            
            headers = [header.get_text(strip=True) for header in table.find_all('th')]
            for row in table.find_all('tr'):
                cells = row.find_all('td')
                if cells:
                    table_data.append({headers[i]: cell.get_text(strip=True) for i, cell in enumerate(cells)})
        except Exception as e:
            print(f"Error while scraping table: {e}")
        return table_data

    def save_to_csv(self, data: List[Dict[str, str]], filename: str):
        if not data:
            print("No data available to save.")
            return
        
        try:
            keys = data[0].keys()
            with open(filename, 'w', newline='', encoding='utf-8') as output_file:
                dict_writer = csv.DictWriter(output_file, fieldnames=keys)
                dict_writer.writeheader()
                dict_writer.writerows(data)
            print(f"Data successfully saved to {filename}")
        except IOError as io_err:
            print(f"File I/O error occurred: {io_err}")
        except Exception as e:
            print(f"Error while saving data to CSV: {e}")

def main():
    # Prompt user for input
    url = input("Enter the URL of the webpage to scrape: ")
    selector = input("Enter the CSS selector for the table to scrape: ")
    output_file = input("Enter the output CSV file name: ")

    # Create the scraper object
    scraper = WebScraper()
    
    # Fetch and scrape the page
    soup = scraper.fetch_page(url)
    if soup:
        table_data = scraper.scrape_table(soup, selector)
        
        # Save the scraped data to CSV
        scraper.save_to_csv(table_data, output_file)

if __name__ == "__main__":
    main()
