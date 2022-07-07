from selenium import webdriver
from fpdf import FPDF
import time

while(True):
    print("Enter a valid musescore url")
    url = input()
    if not (url.startswith('https://musescore.com') or url.startswith('musescore.com')):
        print('Invalid url')
    else:
        break

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(url)
driver.implicitly_wait(5)

urlList = set()

elt = driver.find_element_by_xpath("/html/body[@class='js desktop js-cookie-compliance theme-react summer-sale']/div[@class='js-page react-container']/div[@class='_5tn-M']/section[@class='HJV7K']/main[@class='_1sdLO _1ss1d']/div[@class='_2G3ri']/div[@class='_3UHUA']/div[@class='_36dkj']/div[@id='jmuse-scroller-component']/div[@class='vAVs3'][1]/img[@class='_2zZ8u']")
elt.get_attribute("alt")

for pageNum in range(1, 2):
    elt = driver.find_element_by_xpath("/html/body[@class='js desktop js-cookie-compliance theme-react summer-sale']/div[@class='js-page react-container']/div[@class='_5tn-M']/section[@class='HJV7K']/main[@class='_1sdLO _1ss1d']/div[@class='_2G3ri']/div[@class='_3UHUA']/div[@class='_36dkj']/div[@id='jmuse-scroller-component']/div[@class='vAVs3']["+str(pageNum)+"]/img[@class='_2zZ8u']")
    time.sleep(1)
    print(elt.get_attribute("src"))
    urlList.add(elt.get_attribute("src"))

print(urlList)