# ###                                      Shop: отображение страницы товара
# # 1. Откройте http://practice.automationtesting.in/
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# # 2. Залогиньтесь
# my_account = driver.find_element_by_id('menu-item-50')
# my_account.click()
# username = driver.find_element_by_id('username')
# username.send_keys('serega@mail.ru')
# password= driver.find_element_by_id('password')
# password.send_keys('138811serega')
# btn_login = driver.find_element_by_css_selector('[name="login"]')
# btn_login.click()
# # 3. Нажмите на вкладку "Shop"
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# # 4. Откройте книгу "HTML 5 Forms"
# html=driver.find_element_by_css_selector('[title="Mastering HTML5 Forms"]')
# html.click()
# # 5. Добавьте тест, что заголовок книги назвается:"HTML5 Forms"
# html5 = driver.find_element_by_class_name('product_title')
# html5_get_text=html5.text
# assert html5_get_text == "HTML5 Forms"
# driver.quit()

#                                    Shop: количество товаров в категории

# # 1. Откройте http://practice.automationtesting.in/
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# # 2. Залогиньтесь
# my_account = driver.find_element_by_id('menu-item-50')
# my_account.click()
# username = driver.find_element_by_id('username')
# username.send_keys('serega@mail.ru')
# password= driver.find_element_by_id('password')
# password.send_keys('138811serega')
# btn_login = driver.find_element_by_css_selector('[name="login"]')
# btn_login.click()
# # 3. Нажмите на вкладку "Shop"
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# # 4. Откройте категорию "HTML"
# html = driver.find_element_by_link_text('HTML')
# html.click()
# # 5.Добавьте тест, что отображается три товара
# products = driver.find_elements_by_class_name('product')
# a = len(products)
# if len(products) ==3:
#     print (" Количестов товаров равно 3")
# else:
#     print("Ошибка. Количество товаров: "+str(a))
# driver.quit()

# #                                                 Shop: сортировка товаров
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# #Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# #2 Логинимся
# my_account = driver.find_element_by_id('menu-item-50')
# my_account.click()
# username = driver.find_element_by_id('username')
# username.send_keys('serega@mail.ru')
# password= driver.find_element_by_id('password')
# password.send_keys('138811serega')
# btn_login = driver.find_element_by_css_selector('[name="login"]')
# btn_login.click()
# #3 Нажмимаем на вкладку "Shop"
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# # 4 Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# # • Используйте проверку по value
# selector=driver.find_element_by_class_name('orderby')
# selector_default = selector.get_attribute("value")
# if selector_default == 'menu_order':
#     print('Значение выбрано по умолчанию')
# else:
#     print('Значение выбрано НЕ по умолчанию')
# # 5 Отсортируйте товары по цене от большей к меньшей
# # • в селекторах используйте класс Select
# select=Select(selector)
# select.select_by_value('price-desc')
# # 6 Снова объявите переменную с локатором основного селектора сортировки
# selector=driver.find_element_by_class_name('orderby')
# selector_price_desc = selector.get_attribute("value")
# if selector_price_desc == 'price-desc':
#     print('Сортировка от большего к меньшему')
# else:
#     print('Сортировка выбрана не правильно')
# driver.quit()

# #                                          Shop: отображение, скидка товара
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# # 1. Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# # 2. Залогиньтесь
# my_account = driver.find_element_by_id('menu-item-50')
# my_account.click()
# username = driver.find_element_by_id('username')
# username.send_keys('serega@mail.ru')
# password= driver.find_element_by_id('password')
# password.send_keys('138811serega')
# btn_login = driver.find_element_by_css_selector('[name="login"]')
# btn_login.click()
# # 3 Нажмите на вкладку Shop
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# # 4. Откройте книгу "Android Quick Start Guide"
# book = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]')
# book.click()
# # 5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
# old_price = driver.find_element_by_css_selector('del>span')
# old_price_get=old_price.text
# assert old_price_get == '₹600.00'
# # 6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
# new_price = driver.find_element_by_css_selector('ins>span')
# new_price_get=new_price.text
# assert new_price_get == '₹450.00'
# # 7. Добавьте явное ожидание и нажмите на обложку книги
# # • Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
# book_android = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='Android Quick Start Guide']"))
# )
# book_android.click()
# # 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
# book_android_close = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))
# )
# book_android_close.click()
# driver.quit()
#                                                       Shop: проверка цены в корзине
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# # 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# driver.get("http://practice.automationtesting.in/")
# # 2. Нажмите на вкладку "Shop"
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# # 3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
# add_basket = driver.find_element_by_css_selector('[data-product_id="182"]')
# add_basket.click()
# time.sleep(1)
# # 4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# # • Используйте для проверки assert
# item = driver.find_element_by_class_name('cartcontents')
# item_get_text = item.text
# assert item_get_text == "1 Item"
# price = driver.find_element_by_css_selector('.wpmenucart-contents>:nth-child(3)')
# price_get_text = price.text
# assert price_get_text == "₹180.00"
# # 5. Перейдите в корзину
# item.click()
# # 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# subtotal = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal']"), "₹180.00")
# )
# # 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
# total = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Total']>strong"), "₹189.00")
# )
# driver.quit()

#                                                     Shop: работа в корзине
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# # 1. Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# # 2. Нажмите на вкладку "Shop"
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# # 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# # • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# # • После добавления 1-й книги добавьте sleep
# driver.execute_script("window.scrollBy(0, 300);")
# add_basket_1 = driver.find_element_by_css_selector('[data-product_id="182"]')
# add_basket_1.click()
# time.sleep(2)
# add_basket_2 = driver.find_element_by_css_selector('[data-product_id="180"]')
# add_basket_2.click()
# # 4. Перейдите в корзину
# basket = driver.find_element_by_class_name('cartcontents')
# basket.click()
# # 5. Удалите первую книгу
# time.sleep(2)
# remove_1_book = driver.find_element_by_css_selector('[data-product_id="182"]')
# remove_1_book.click()
# # 6. Нажмите на Undo (отмена удаления)
# undo = driver.find_element_by_partial_link_text("Undo?")
# undo.click()
# # 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# # • Предварительно очистите поле с помощью локатор_поля.clear()
# quantity = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
# quantity.clear()
# quantity.send_keys('3')
# # 8. Нажмите на кнопку "UPDATE BASKET"
# update_basket_btn = driver.find_element_by_css_selector('[name="update_cart"]')
# update_basket_btn.click()
# # 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
# quantity_js = quantity.get_attribute('value')
# assert quantity_js == '3'
# # 10. Нажмите на кнопку "APPLY COUPON"
# # • Перед нажатимем добавьте sleep
# time.sleep(2)
# apply_btn = driver.find_element_by_css_selector('[name="apply_coupon"]')
# apply_btn.click()
# # 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
# # вариант проверки 1
# # error = driver.find_element_by_class_name('woocommerce-error')
# # error_get_text = error.text
# # assert  error_get_text == "Please enter a coupon code."
# # вариант проверки 2
# error= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-error"), "Please enter a coupon code."))
# driver.quit()

#                                                                       Shop: покупка товара
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.implicitly_wait(15)
# driver.maximize_window()
# import time
# # 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# driver.get("http://practice.automationtesting.in/")
# # 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# # 3. Добавьте в корзину книгу "HTML5 WebApp Development"
# add_basket_1 = driver.find_element_by_css_selector('[data-product_id="182"]')
# add_basket_1.click()
# time.sleep(2)
# # 4. Перейдите в корзину
# basket = driver.find_element_by_class_name('cartcontents')
# basket.click()
# # 5. Нажмите "PROCEED TO CHECKOUT"
# # • Перед нажатием, добавьте явное ожидание
# checkout_btn = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")) )
# checkout_btn.click()
# # 6. Заполните все обязательные поля
# # • Перед заполнением first name, добавьте явное ожидание
# # • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# # • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
# first_name = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.ID, "billing_first_name")) )
# first_name.send_keys('John')
# last_name = driver.find_element_by_id('billing_last_name')
# last_name.send_keys('Parkers')
# email = driver.find_element_by_id('billing_email')
# email.send_keys('new_york_sk@gmail.com')
# phone = driver.find_element_by_id('billing_phone')
# phone.send_keys('38347789')
# country = driver.find_element_by_id('s2id_billing_country')
# country.click()
# country_send_text = driver.find_element_by_class_name('select2-input')
# country_send_text.send_keys("South Korea")
# country_click = driver.find_element_by_class_name('select2-match')
# country_click.click()
# postcode = driver.find_element_by_id('billing_postcode')
# postcode.send_keys("111789")
# adress = driver.find_element_by_id('billing_address_1')
# adress.send_keys('11 street 22')
# city = driver.find_element_by_id('billing_city')
# city.send_keys("Seul")
# # 7. Выберите способ оплаты "Check Payments"
# # • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(2)
# radio_btn = driver.find_element_by_id('payment_method_cheque')
# radio_btn.click()
# # 8. Нажмите PLACE ORDER
# time.sleep(3)
# place = driver.find_element_by_id('place_order')
# place.click()
# # 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
# text = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".page-content.entry-content"), "Thank you. Your order has been received.")
# )
# # 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
# text2 = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".page-content.entry-content"), "Check Payments")
# )