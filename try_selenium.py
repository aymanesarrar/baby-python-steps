from selenium import webdriver
# you should change the path
path = "/mnt/c/Python38/webdrivers/geckodriver.exe" 
driver = webdriver.Firefox(executable_path=path)
driver.get('')
#driver.get() get the website where you wanna go
#driver.find_element_by_css_selector() it gonna get an element from the html
username = driver.find_element_by_css_selector('#user_email')
username.send_keys('')
# username.send_keys() fill ip the form
password = driver.find_element_by_css_selector('#user_password')
password.send_keys('')
connection = driver.find_element_by_css_selector('input.btn')
# connection.click() click the button
connection.click()
choice = int(input())
if choice == 1:
  driver.close()