from .pages.product_page import ProductPage
import time
import pytest

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, link):
	page = ProductPage(browser, link)
	page.open()

	# есть кнопка добавления
	page.should_be_add_btn()

	# жмём её
	page.add_btn_click()
	page.solve_quiz_and_get_code()
	time.sleep(2)
	# есть сообщение об успешном добавлении
	page.should_be_success_add_alert()

    # смотрим на название добавленной в корзину книги
	page.is_book_name_added_and_equal2_name( page.get_product_name() )

	# смотрим на ценник добавленный в корзину
	#page.is_price_in_cart_and_equal2_price( page.get_product_price() )

