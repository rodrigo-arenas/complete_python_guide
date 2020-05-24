from Section_10_Quotes_Scraping.locators.quote_locators import QuoteLocators


class QuoteParser:
    """
     Given one of the specific quotes div, find put the data about the quote:
         - Content
         - Author
         - Tag
     """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}>'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT_LOCATOR
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR_LOCATOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuoteLocators.TAGS_LOCATOR
        return self.parent.select(locator)





