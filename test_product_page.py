from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
	lnk = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	lnk = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	#lnk = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
	page = ProductPage(browser, lnk)
	page.open()

	# есть кнопка добавления
	page.should_be_add_btn()

	# жмём её
	page.add_btn_click()
	#time.sleep(2)
	page.solve_quiz_and_get_code()
	#time.sleep(2)
	# есть сообщение об успешном добавлении
	page.should_be_success_add_alert()

    # смотрим на название добавленной в корзину книги
	page.is_book_name_added_and_equal2_name( page.get_product_name() )

	# смотрим на ценник добавленный в корзину
	page.is_price_in_cart_and_equal2_price( page.get_product_price() )

#	time.sleep(5)