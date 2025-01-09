from concurrent.futures import ThreadPoolExecutor
from playwright.sync_api import sync_playwright

def scrape_single(config, price_xpath):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--start-maximized",
            ]
        )
        
        page = browser.new_page()

        page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
        })

        page.goto(config['url'])

        try:            
            page.wait_for_selector(f"xpath={price_xpath}", timeout=5000)

            element = page.locator(f"xpath={price_xpath}")
            if element:
                price = element.inner_text()
                config['price'] = price.replace('\xa0', '').replace(',-', ''). replace(' ', '').replace('Kč', '')
            else:
                print("Price element not found.")
        except Exception as e:
            print(f"Error fetching price: {e}")
            config["price"] = None
        finally:
            browser.close()
        return config
    
def scrape_parallel(configs, price_xpath):   
    with ThreadPoolExecutor(max_workers=4) as executor:  # Můžeš upravit počet vláken
        results = list(executor.map(lambda c: scrape_single(c, price_xpath), configs))
    return results

# if __name__ == "__main__":
#     scraped_data_istyle = scrape_parallel(
#         CONFIG_ISTYLE,
#         XPATH_PRODUCT_PRICE_ISTYLE
#     )
    
#     scraped_data_alza = scrape_parallel(
#         CONFIG_ALZA,
#         XPATH_PRODUCT_PRICE_ALZA
#     )
    
#     print(scraped_data_istyle)
#     print(scraped_data_alza)