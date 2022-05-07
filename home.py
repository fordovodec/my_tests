#                                              Home:добавление комментария
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
#1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# 2. Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
selenium_ruby_btn = driver.find_element_by_css_selector('[alt="Selenium Ruby"]')
selenium_ruby_btn.click()
# 4. Нажмите на вкладку "REVIEWS"
reviews_btn= driver.find_element_by_css_selector('[href="#tab-reviews"]')
reviews_btn.click()
# 5. Поставьте 5 звёзд
star5 = driver.find_element_by_class_name('star-5')
star5.click()
# 6. Заполните поле "Review" сообщением: "Nice book!"
Review = driver.find_element_by_id('comment')
Review.send_keys("Nice book!")
#  7. Заполните поле "Name"
name= driver.find_element_by_id('author')
name.send_keys('Donald')
#  8. Заполните "Email"
email = driver.find_element_by_id('email')
email.send_keys('123456@gmail.com')
#  9. Нажмите на кнопку "SUBMIT"  submit
submit = driver.find_element_by_id('submit')
submit.click()
driver.quit()


