import requests

#url = "https://web-scraper-ihnl.onrender.com/test-selenium"
url = "https://docker-scraper-573o.onrender.com/scrape" # docker - render
#url = "http://localhost:8000/scrape" # docker - local

try:
    response = requests.post(url)
    response.raise_for_status()  # Vyvolá chybu, pokud HTTP status není 200
    data = response.json()
    print("Response from Render Selenium endpoint:")
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Error connecting to Selenium endpoint: {e}")