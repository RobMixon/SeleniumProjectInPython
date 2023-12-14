from seleniumpagefactory.Pagefactory import PageFactory


def check_page_loaded(): None


class Homepage(PageFactory):
        def __init__(self, driver):
            self.driver = driver
            
        locators = {}
            