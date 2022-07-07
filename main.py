from selenium import webdriver

loop = True
while(loop):
    print("Enter a valid muscore url")
    url = input()

    if not (url.startswith('https://musescore.com') or url.startswith('musescore.com')):
        print('Invalid url')
    else:
        loop = False

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(url)
driver.maximize_window()
