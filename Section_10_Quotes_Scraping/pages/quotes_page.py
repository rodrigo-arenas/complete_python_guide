from bs4 import BeautifulSoup
from Section_10_Quotes_Scraping.locators.quotes_page_locators import QuotesPageLocators
from Section_10_Quotes_Scraping.parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        return [QuoteParser(e) for e in self.soup.select(QuotesPageLocators.QUOTE)]



