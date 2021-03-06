from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): 
	def should_be_add_btn(self):
		assert self.is_element_present(*ProductPageLocators.ADD_BTN), "Add to basket btn is not presented"
		print("кнопка добавления товара в корзину на месте !")

	def add_btn_click(self):
		addbtn = self.browser.find_element(*ProductPageLocators.ADD_BTN)
		addbtn.click()

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.ALERTS), \
				"Success message is presented, but should not be"

	def should_DISSAPEAR(self):
		assert self.is_disappeared(*ProductPageLocators.ALERTS), \
				"Success message is NOT DISSAPERARED, but should be"

	def should_be_success_add_alert(self):
	    assert self.is_element_present(*ProductPageLocators.ALERTS), "No Success add alert on page !"
	    print("Есть удачное добавление товара в корзину !")

	def get_product_price(self):
		return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text

	def get_product_name(self):
		return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text

	def is_book_name_added_and_equal2_name(self, s1):		
		s2 = self.browser.find_element(*ProductPageLocators.cart_BOOK_NAME).text
		s3 = self.browser.find_elements(*ProductPageLocators.ALERTS)[0].text
		assert s1 == s2 == s3, "Ошибочка - Название книги не равно добавленному в корзину названию !!!"

	def is_price_in_cart_and_equal2_price(self, s1):
		s2 = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
		s3 = self.browser.find_elements(*ProductPageLocators.ALERTS)[2].text
		assert s1 == s2 == s3, "Ошибочка - ЦЕНА книги не равна добавленной в корзину цене !!!"
