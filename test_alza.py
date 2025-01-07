import asyncio
from playwright.async_api import async_playwright
import time

# URL of the page
url = "https://www.alza.cz/macbook-air-15-m3-cz-2024?dq=10931503"

# XPath to the price element
xpath_price = '//div[@class="price-detail__price-box-wrapper js-price-detail__main-price-box-wrapper"]//span[@class="price-box__price"]'

async def get_price():
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Navigate to the URL
        await page.goto(url)
        await page.wait_for_timeout(2000)
        
        # Wait for the price element to load
        price_element = await page.wait_for_selector(xpath_price)

        # Extract the price text
        price = await price_element.inner_text()

        print(f"Price: {price}")

        # Close the browser
        await browser.close()

# Run the function
asyncio.run(get_price())
