import requests
import time
from config import CONFIG_ISTYLE

def scrape_istyle(configs: list) -> list:
    for config in configs:
        response = requests.get(config["url"])

        if response.status_code == 200:
            data = response.json()

            print(data["price"]["price"])
            
        elif response.status_code == 503:
            print("Server busy...")
            time.sleep(5)
            response = requests.get(config["url"])
            if response.status_code == 200:
                data = response.json()
                print(data["price"]["price"])
            else:
                return

        else:
            print(f"Error: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    scrape_istyle(CONFIG_ISTYLE)