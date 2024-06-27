# pip install selenium ( прога для автоматизации работы с браузером )
from asyncio import sleep

from selenium import webdriver

driver = webdriver.Chrome()

# open localhost admin panel
driver.get('http://localhost:8000/admin/')

#input('i`m done press Enter to continue')

# find input with name username
username_element = driver.find_element(by='xpath', value='//input[@name="username"]')
username_element.send_keys('ivan')
sleep(2)
# find input with name password
password_element = driver.find_element(by='xpath', value='//input[@name="password"]')
password_element.send_keys('1111')
sleep(2)
# find the login button
login_button = driver.find_element(by='xpath', value='//input[@type="submit"]')
login_button.click()

title = driver.find_element(by='xpath', value='//h1')
assert title.text == 'Django administration'

input('Press Enter to continue...')