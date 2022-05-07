# #######################   Registration_login: регистрация аккаунта    ##########################
# # 1. Откройте http://practice.automationtesting.in/
# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# # 2. Нажмите на вкладку "My Account Menu"
# my_account = driver.find_element_by_id('menu-item-50')
# my_account.click()
# # 3. В разделе "Register", введите email для регистрации
# reg_email = driver.find_element_by_id('reg_email')
# reg_email.send_keys('q123456789@mail.ru')
# # 4. В разделе "Register", введите пароль для регистрации
# reg_password = driver.find_element_by_id('reg_password')
# reg_password.send_keys('zq1xw2ce3vr4')
# # 5. Нажмите на кнопку "Register"
# register = driver.find_element_by_css_selector('[name="register"]')
# register.click()
# driver.quit()

# ########################################## Registration_login: логин в систему  ###############################
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# #1. Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# # 2. Нажмите на вкладку "My Account Menu"
# my_account = driver.find_element_by_id('menu-item-50')
# my_account.click()
# # 3. В разделе "Login", введите email для логина
# username = driver.find_element_by_id('username')
# username.send_keys('serega@mail.ru')
# # 4. В разделе "Login", введите пароль для логина
# password= driver.find_element_by_id('password')
# password.send_keys('138811serega')
# # 5. Нажмите на кнопку "Login"
# btn_login = driver.find_element_by_css_selector('[name="login"]')
# btn_login.click()
# # 6. Добавьте проверку, что на странице есть элемент "Logout"
# logout = driver.find_element_by_link_text("Logout")
# logout_get_text=logout.text
# assert logout_get_text == "Logout"
# driver.quit()
