from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ifit.com/login")

# test call to make sure we are on the correct page
def verify_title():
    # Get the title of the page
    title = driver.title

    # Verify the title
    expected_title = "Sign In with iFIT"
    if title == expected_title:
        print(f"We have received Title: '{title}'")
        print(f" Title verification successful!")
    else:
        print(f"Title verification failed. Expected '{expected_title}', but got '{title}'.")


if __name__ == "__main__":
    verify_title()
