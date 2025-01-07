import requests
import json

# URL požadavku
#url = "https://istyle.cz/ajaxcaptainhook/ajaxhook/productpagehook/"
url = "https://istyle.cz/ajaxcaptainhook/ajaxhook/productpagehook/?product_id=168053&url=https%3A%2F%2Fistyle.cz%2Fmacbook-air-15-3-apple-m3-8jadrove-cpu-10jadrove-gpu-24gb-512gb-ssd-cz-vesmirne-sedy.html&data%5B%5D=firstload"

# Parametry dotazu
params = {
    "product_id": "159045",
    "url": "https://istyle.cz/macbook-air-15-3-apple-m3-8jadrove-cpu-10jadrove-gpu-16gb-512gb-ssd-cz-vesmirne-sedy.html",
    "data[]": "firstload"
}

# Hlavičky požadavku
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": "https://istyle.cz/macbook-air-15-3-apple-m3-8jadrove-cpu-10jadrove-gpu-16gb-512gb-ssd-cz-vesmirne-sedy.html",
    "DNT": "1"  # Do Not Track
}

# Cookies
cookies = {
    "_fw_crm_v": "021b3a11-ffb4-4903-a0bc-67ea5f9a3885",
    "PHPSESSID": "rh5uvupg1caei4b0kgtdmjksa6",
    "form_key": "331GnQhBvbbczBlZ",
    "_ga": "GA1.1.509111399.1735309433",
    # Přidejte další cookies podle potřeby...
}

# Odeslání požadavku
response = requests.get(url) #, headers=headers, params=params, cookies=cookies)

# Kontrola odpovědi
if response.status_code == 200:
    data = response.json()
    # Přístup k ceně
    print(data["price"]["price"])
    #print(json.dumps(data, indent=4, ensure_ascii=False))  # Formátovaný výstup s podporou českých znaků
else:
    print(f"Error: {response.status_code}, Response: {response.text}")