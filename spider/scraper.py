from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def scrape_single(config, price_xpath, xpath_cookies_button=None):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--start-maximized')
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    cookie_clicked: bool = False
    try:
        driver.get(config["url"])
        if xpath_cookies_button and not cookie_clicked:
                try:
                    wait = WebDriverWait(driver, 2)
                    cookie_button = wait.until(
                        EC.element_to_be_clickable((By.XPATH, xpath_cookies_button))
                    )
                    cookie_button.click()
                    cookie_clicked = True
                except Exception as e:
                    print(f"Failed to click cookies button: {e}")
        price = driver.find_element(By.XPATH, price_xpath).text
        config["price"] = price.replace(',-', '')
    except Exception as e:
        print(f"Error scraping {config['url']}: {e}")
        config["price"] = None
    finally:
        driver.quit()

    return config

def scrape_alza_parallel(configs, price_xpath):
    with ThreadPoolExecutor(max_workers=4) as executor:  # Můžeš upravit počet vláken
        results = list(executor.map(lambda c: scrape_single(c, price_xpath), configs))
    return results

def scrape_istyle_parallel(configs, price_xpath, xpath_cookies_button):
    with ThreadPoolExecutor(max_workers=3) as executor:  # Můžeš upravit počet vláken
        results = list(executor.map(lambda c: scrape_single(c, price_xpath, xpath_cookies_button), configs))
    return results

# if __name__ == "__main__":
#     updated_configs = scrape_alza_parallel(CONFIG_ALZA, XPATH_PRODUCT_PRICE_ALZA)
#     print(updated_configs)
