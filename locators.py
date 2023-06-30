from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())

driver = Chrome(service=service)

driver.get('https://demoqa.com/text-box')
user_form = driver.find_element(By.ID, 'userForm')
full_name_field = user_form.find_element(By.ID, 'userName')
email_field = user_form.find_element(By.ID, 'userEmail')
current_address_field = user_form.find_element(By.ID, 'currentAddress')
permanent_address_field = user_form.find_element(By.ID, 'permanentAddress')

full_name_field.send_keys('Vasya Pupkin')
email_field.send_keys('pupkin@mail.com')
current_address_field.send_keys('my current address')
permanent_address_field.send_keys('my permanent address')

text = full_name_field.get_attribute('value')
assert user_form.is_displayed()
assert text == 'Vasya Pupkin'
pass
