from selenium import webdriver
from fpdf import FPDF

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

elt = driver.find_element_by_xpath("/html/body[@class='js desktop js-cookie-compliance theme-react summer-sale']/div[@class='js-page react-container']/div[@class='_5tn-M']/section[@class='HJV7K']/main[@class='_1sdLO _1ss1d']/div[@class='_2G3ri']/div[@class='_3UHUA']/div[@class='_36dkj']/div[@id='jmuse-scroller-component']/div[@class='vAVs3'][1]/img[@class='_2zZ8u']");
print(elt.get_attribute("src"))