#добавление в корзину со страницы товара
import time

from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage


def test_guest_can_add_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_baskets()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.item_added_to_cart()
    page.basket_item_prices_is_correct()
