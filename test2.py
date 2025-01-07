import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Avast/131.0.0.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://istyle.cz/macbook-air-15-3-apple-m3-8jadrove-cpu-10jadrove-gpu-16gb-512gb-ssd-cz-vesmirne-sedy.html",
}

url = "https://istyle.cz/ajaxcaptainhook/ajaxhook/productpagehook/"
params = {
    "product_id": "159045",
    "url": "https://istyle.cz/macbook-air-15-3-apple-m3-8jadrove-cpu-10jadrove-gpu-16gb-512gb-ssd-cz-vesmirne-sedy.html",
    "data[]": "firstload",
}

response = requests.get(url, headers=headers, params=params)

print(response.status_code)
print(response)
data = response.json()
print(data["price"]["price"])