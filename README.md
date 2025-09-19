# Dynamic Infinite Scroll Scraper using Playwright

This project demonstrates an advanced scraping technique for handling modern, JavaScript-driven websites. The script automates a real browser to scrape all content from a page that uses "infinite scrolling" to load new items.

## Core Technologies
- **Python 3**
- **Playwright:** The primary engine for browser automation. It launches, controls, and instructs a real browser (headless or not) to perform user actions.
- **Asyncio:** The script is built using Python's native asynchronous framework, allowing for modern and efficient execution.
- **BeautifulSoup4:** Used after the browser automation is complete to parse the final, fully-rendered HTML for data extraction.

## Key Features & Challenges Solved
- **Browser Automation:** Successfully launches and controls a headless browser, proving the ability to handle sites that `requests` cannot.
- **Infinite Scroll Logic:** The core of this script is a loop that repeatedly scrolls to the bottom of the page. It intelligently detects when all content has been loaded by comparing the page's scroll height before and after the scroll action, ensuring a complete scrape without getting stuck in a loop.
- **Dynamic Content Handling:** This script is specifically designed to scrape content that is loaded dynamically by JavaScript and is not present in the initial page source.
