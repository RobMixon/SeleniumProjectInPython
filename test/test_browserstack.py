from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from src.pages.homepage import Homepage
from src.pages.sign_up_page import SignUpPage

def test_login():
    # options = Options()
    # # options.add_argument("--headless") # Runs Chrome in headless mode.
    # options.add_argument('--no-sandbox')  # # Bypass OS security model
    # options.add_argument('disable-infobars')
    # options.add_argument("--disable-extensions")
    # options.add_argument("--start-fullscreen")
    # options.add_argument('--disable-gpu')

    # driver = webdriver.Firefox()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://ifit.com/login")

    sign_up_page = SignUpPage(driver)

    sign_up_page.select_username()
    sign_up_page.select_password()
    sign_up_page.click_login()



