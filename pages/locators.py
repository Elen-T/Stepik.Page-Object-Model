from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #каждый селектор — это пара: как искать и что искатclassь.


class LoginPageLocators():
    LOGIN_FORM =(By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM =(By.CSS_SELECTOR, "#register_form")
    LOGIN_URL_KEY = 'login'


class ProductPageLocators():
    BUTTON_BASKETS =(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    #NAME_ITEM_IN_MESSAGE =(By.CSS_SELECTOR, ".alertinner > strong")
    #NAME_ITEM_IN_CART =(By.LINK_TEXT, "The shellcoder's handbook") #название товара в корзине
    NAME_ITEM_IN_MESSAGE =(By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    NAME_ITEM_IN_CART =(By.CSS_SELECTOR, ".product_main > h1")
    CART_VALUE=(By.CSS_SELECTOR, ".alertinner > p > strong") #стоимость корзины
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div.product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")