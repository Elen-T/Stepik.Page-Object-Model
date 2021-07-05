from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_baskets (self):
        button_baskets= self.browser.find_element(*ProductPageLocators.BUTTON_BASKETS)
        button_baskets.click()

    #Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром,
    # который вы действительно добавили.
    def item_added_to_cart (self, product_name):
        #text = ProductPageLocators.NAME_ITEM_IN_CART
        #assert text == ProductPageLocators.NAME_ITEM_IN_MESSAGE, "item not added to cart "
        product_name = self.browser.find_element(*ProductPageLocators.NAME_ITEM_IN_CART).text
        added_product_name = self.browser.find_element(*ProductPageLocators.NAME_ITEM_IN_MESSAGE).text
        assert product_name == added_product_name, f"Product name does not match, should {product_name}, given {added_product_name}"

    #Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара
    def basket_item_prices_is_correct (self):
        cart_value = self.browser.find_element(*ProductPageLocators.CART_VALUE).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert cart_value ==  price_product, f"Price does not match, should {price_product}, given {cart_value}"




#Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.



