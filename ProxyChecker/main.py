import requests
from bs4 import BeautifulSoup
import concurrent.futures
import csv

class ProxyChecker:
    def __init__(self, url, all_proxies_file='all_proxies.csv', available_proxies_file='available_proxies.csv'):
        self.url = url
        self.proxies = []
        self.all_proxies_file = all_proxies_file
        self.available_proxies_file = available_proxies_file

    def parse_proxies(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
            if len(columns) >= 2:
                ip = columns[0].text.strip()
                port = columns[1].text.strip()
                self.proxies.append(f"{ip}:{port}")

    def check_proxy(self, proxy):
        try:
            response = requests.get('https://httpbin.org/ip', proxies={'http': proxy, 'https': proxy}, timeout=5)
            return proxy, response.status_code == 200, "Available" if response.status_code == 200 else f"Status code: {response.status_code}"
        except requests.RequestException as e:
            return proxy, False, str(e)

    def check_proxies(self):
        all_results = []
        available_proxies = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(self.check_proxy, self.proxies)
            for result in results:
                all_results.append(result)
                if result[1]:
                    available_proxies.append(result[0])

        self._save_to_csv(all_results, self.all_proxies_file)
        self._save_to_csv([(proxy,) for proxy in available_proxies], self.available_proxies_file)
        return available_proxies

    def _save_to_csv(self, data, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if filename == self.all_proxies_file:
                writer.writerow(['Proxy', 'Available', 'Message'])
            else:
                writer.writerow(['Proxy'])
            writer.writerows(data)

    def run(self):
        self.parse_proxies()
        return self.check_proxies()

# Usage example:
checker = ProxyChecker('https://free-proxy-list.net')
available_proxies = checker.run()
print(f"Available proxies: {available_proxies}")