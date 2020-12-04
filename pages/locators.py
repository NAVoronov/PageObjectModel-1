from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REG_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
	#add_to_basket_form > button
	# class = btn-add-to-basket
	ADD_BTN = (By.CSS_SELECTOR, "#add_to_basket_form > button") #"button.btn-add-to-basket"

	ALERTS = (By.CSS_SELECTOR, ".alertinner strong") # сообщения о добавлении - в нулевом цена, во втором название
	SUC_ALERT = (By.CSS_SELECTOR, ".alert-success") # есть успешное добавление #.alert-success

	BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color") # цена книги   p.price_color
	CART_PRICE = (By.CSS_SELECTOR, ".alertinner >p strong") # стоимость всей корзины в .alertinner >p strong

	BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1") # название книги .col-sm-6.product_main >h1	
	cart_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner strong") # название добавленной книги в .alertinner strong

