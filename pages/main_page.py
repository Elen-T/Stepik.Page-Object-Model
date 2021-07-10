from pages.base_page import BasePage
from pages.locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_baskets (self):
        button_baskets= self.browser.find_element(*MainPageLocators.VIEW_BASKET)
        button_baskets.click()

    # def go_to_login_page(self):
    #     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     link.click()
    #
    # def should_be_login_link(self):
    #     #assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"