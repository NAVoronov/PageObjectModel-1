from .pages.product_page import ProductPage
import pytest

def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page (browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()
	page.go_to_login_page()

@pytest.mark.skip #xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
	#Открываем страницу товара 
	lnk = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
	page = ProductPage(browser, lnk)
	page.open()
	
	#Добавляем товар в корзину 
	page.add_btn_click()
	
	#Проверяем, что нет сообщения об успехе с помощью is_not_element_present
	page.should_not_be_success_message() 

@pytest.mark.skip #xfail
def test_guest_cant_see_success_message(browser): 
	#Открываем страницу товара 
	lnk = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
	page = ProductPage(browser, lnk)
	page.open()

	#Проверяем, что нет сообщения об успехе с помощью is_not_element_present
	page.should_not_be_success_message()  

@pytest.mark.skip #xfail
def test_message_disappeared_after_adding_product_to_basket(browser): 
#Открываем страницу товара
	lnk = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
	page = ProductPage(browser, lnk)
	page.open()

	#Добавляем товар в корзину
	page.add_btn_click()
	
	#Проверяем, что нет сообщения об успехе с помощью is_disappeared
	page.should_DISSAPEAR()

