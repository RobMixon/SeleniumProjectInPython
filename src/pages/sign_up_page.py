from seleniumpagefactory.Pagefactory import PageFactory


# class SignUpPage(PageFactory):
#     def __init__(self, driver):
#         self.driver = driver
#
#
#     def verify_title(self):
#         title = self.driver.getTitle()
#         expected_title = "Sign In with iFIT"
#
#         if title == expected_title:
#             print(f"We have received Title: '{title}'")
#             print(f" Title verification successful!")
#         else:
#             print(f"Title verification failed. Expected '{expected_title}', but got '{title}'.")
#
class SignUpPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
    'user_name': ('CSS', "#username input"),
    'password': ('CSS', '#password input'),
    'login_btn': ('ID', 'login-btn')
    }

    def select_username(self):
        self.user_name.set_text('demouser\n')

    def select_password(self):
        self.password.set_text('testingisfun99\n')

    def click_login(self):
        self.login_btn.click()

