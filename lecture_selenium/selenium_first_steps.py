from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = Chrome(service=service)
driver.get('https://demoqa.com/text-box')
user_form = driver.find_element(By.ID, 'userForm')
full_name_field = user_form.find_element(By.ID, 'userName')
full_name_field.send_keys('Vasya Pupkin')
text = full_name_field.get_attribute('value')

email_field = user_form.find_element(By.ID, 'userEmail')
email_field.send_keys('pupkin@mail.com')

current_address = driver.find_element(By.ID, 'currentAddress')
current_address.send_keys('My current address')
curr_addr_val = current_address.get_attribute('value')

perm_address = driver.find_element(By.XPATH, '//textarea[@id="permanentAddress"]')
perm_address.send_keys('My permanent address')

assert user_form.is_displayed()
assert text == 'Vasya Pupkin'
assert email_field.get_attribute('value') == 'pupkin@mail.com'
assert curr_addr_val == 'My current address'
assert perm_address.get_attribute('value') == 'My permanent address'
pass

driver.quit()
