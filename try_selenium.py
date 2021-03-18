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



########################NOTES####################
# To import selenium, you need to run: "from selenium import webdriver" (and not "import selenium").
# To open the browser, run: browser = webdriver.Firefox()
# To send the browser to a URL, run: browser.get(‘https://inventwithpython.com')
# The browser.find_elements_by_css_selector() method will return a list of WebElement objects: elems = browser.find_elements_by_css_selector(‘img')
# WebElement objects have a "text" variable that contains the element's HTML in a string: elems[0].text
# The click() method will click on an element in the browser.
# The send_keys() method will type into a specific element in the browser.
# The submit() method will simulate clicking on the Submit button for a form.
# The browser can also be controlled with these methods: back(), forward(), refresh(), quit().