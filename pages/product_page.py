from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import ProductPageLocators
from pages.main_page import MainPage



class ProductPage(BasePage):
    def add_to_baskets (self):
        button_baskets= self.browser.find_element(*ProductPageLocators.BUTTON_BASKETS)
        button_baskets.click()

    def return_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.NAME_ITEM_IN_CART)
        return book_name.text

    def return_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        return book_price.text

    #Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром,
    # который вы действительно добавили.
    def item_added_to_cart (self, book_name):
        #text = ProductPageLocators.NAME_ITEM_IN_CART
        #assert text == ProductPageLocators.NAME_ITEM_IN_MESSAGE, "item not added to cart "
        added_product_name = self.browser.find_element(*ProductPageLocators.NAME_ITEM_IN_MESSAGE).text
        assert book_name == added_product_name, f"Product name does not match, should {book_name}, given {added_product_name}"

    #Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара
    def basket_item_prices_is_correct (self, book_price):
        cart_value = self.browser.find_element(*ProductPageLocators.CART_VALUE).text
        assert cart_value == book_price, f"Price does not match, should {book_price}, given {cart_value}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_is_disappeared(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "is not disappeared"


