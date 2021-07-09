from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_CONTAINER),\
            'Basket is not empty'

    def should_be_empty_basket_text_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            'Basket is empty'
