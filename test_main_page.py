from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_baskets()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_text_message()





# def test_guest_can_go_to_login_page(browser):
#     link = " http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open() # открываем страницу
#     page.should_be_login_link()
#     page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open() # открываем страницу
#     page.should_be_login_link()
#     page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина




# def test_guest_can_go_to_login_page(browser):
#     browser.get(link)
#     go_to_login_page(browser)
#
# def go_to_login_page(browser):
#     login_link = browser.find_element_by_css_selector("#login_link")
#     login_link.click()
#
# from .pages.main_page import MainPage


