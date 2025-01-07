import requests

def fetch_product_data(product_id, url):
    base_url = "https://istyle.cz/ajaxcaptainhook/ajaxhook/productpagehook/"
    params = {
        "product_id": product_id,
        "url": url,
        "data[]": "firstload",
    }
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "cs-CZ,cs;q=0.9",
        "referer": url,
        "sec-ch-ua": '"Avast Secure Browser";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Avast/131.0.0.0",
        "x-requested-with": "XMLHttpRequest",
    }

    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()  # Vrátí data jako JSON
    except requests.RequestException as e:
        print(f"Error fetching product data: {e}")
        return 1

if __name__ == "__name__":
    
    product_id = 159045
    product_url = "https://istyle.cz/macbook-air-15-3-apple-m3-8jadrove-cpu-10jadrove-gpu-16gb-512gb-ssd-cz-vesmirne-sedy.html"

    data = fetch_product_data(product_id, product_url)
    if data:
        print(data)


