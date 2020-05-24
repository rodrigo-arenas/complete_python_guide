import requests
from Section_10_Quotes_Scraping.pages.quotes_page import QuotesPage


page_content = requests.get('http://quotes.toscrape.com').content
page = QuotesPage(page_content)

for quote in page.quotes:
    print(quote.content)


