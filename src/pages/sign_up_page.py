from seleniumpagefactory.Pagefactory import PageFactory

class SignUpPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15          
        self.highlight = True    
        self.mobile_test = False    

    locators = {
    'user_name': ('ID', "1-email"),
    'password': ('NAME', 'password'),
    'login_btn': ('CLASS_NAME', 'auth0-lock-submit')
    }

    def select_username(self):
        self.user_name.set_text('steve\n')       

    def select_password(self):
        self.password.set_text('carell\n')

    def click_login(self):
        self.login_btn.click()

