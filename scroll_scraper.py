import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import csv

async def scrape_quotes():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False, slow_mo=50)
        page = await browser.new_page()
        await page.goto("http://quotes.toscrape.com/scroll")

        height = 0
        while True:
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_timeout(1000)

            current_height = await page.evaluate("document.body.scrollHeight")
            if current_height == height:
                break
            height = current_height
        content = await page.content()
        await browser.close()

        soup = BeautifulSoup(content, "lxml")
        quotes = soup.find_all('div', class_="quote")

        with open("scrolled_quotes.csv", "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Quote, Author"])
            for quote in quotes:
                quote_text = quote.find('span', class_="text").get_text()
                quote_author = quote.find("small", class_= 'author').get_text()
                writer.writerow([quote_text, quote_author])
                
asyncio.run(scrape_quotes())

