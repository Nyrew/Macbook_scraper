from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import json

# Nastavení webdriveru (používáme Chrome)
options = Options()
options.add_argument("--headless=new")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')
options.add_argument('--start-maximized')
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    

# Nastavení webdriveru s Chrome v headless režimu
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Otevři stránku
url = "https://www.alza.cz/macbook-air-15-m3-cz-2024?dq=10931503"
driver.get(url)

# Počkej, než se stránka načte (můžeš přizpůsobit čas)
#time.sleep(5)

# Získání informací z HTML pomocí tvého XPath
#product_name = driver.find_element(By.CLASS_NAME, "product-name").text
price = driver.find_element(By.XPATH, '//div[@class="price-detail__price-box-wrapper js-price-detail__main-price-box-wrapper"]//span[@class="price-box__price"]').text

# Vytvoření JSON
product_data = {
    "price": price
}

# Uložení dat jako JSON
json_data = json.dumps(product_data, ensure_ascii=False, indent=4)

print(json_data)

# Zavři prohlížeč
driver.quit()
