from selenium import webdriver

print("Enter a valid muscore url")
url = input()

#TODO: Check that url is valid

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(url)
driver.maximize_window()
