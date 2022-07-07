from selenium import webdriver
from fpdf import FPDF
from PIL import Image
import urllib.request
import time
import warnings
import os

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
warnings.filterwarnings("ignore", category=DeprecationWarning) 

elt = driver.find_element_by_xpath("/html/body[@class='js desktop js-cookie-compliance theme-react summer-sale']/div[@class='js-page react-container']/div[@class='_5tn-M']/section[@class='HJV7K']/main[@class='_1sdLO _1ss1d']/div[@class='_2G3ri']/div[@class='_3UHUA']/div[@class='_36dkj']/div[@id='jmuse-scroller-component']/div[@class='vAVs3'][1]/img[@class='_2zZ8u']")
altTag = elt.get_attribute("alt")

try:
    numPages = int(altTag[::-1][5:altTag[::-1].find(" ", 6)][::-1])
except:
    print('Number of Pages not found')

print("DEBUG LOG (numPages): " + str(numPages))

images = []

for pageNum in range(1, numPages+1):
    elt = driver.find_element_by_xpath("/html/body[@class='js desktop js-cookie-compliance theme-react summer-sale']/div[@class='js-page react-container']/div[@class='_5tn-M']/section[@class='HJV7K']/main[@class='_1sdLO _1ss1d']/div[@class='_2G3ri']/div[@class='_3UHUA']/div[@class='_36dkj']/div[@id='jmuse-scroller-component']/div[@class='vAVs3']["+str(pageNum)+"]/img[@class='_2zZ8u']")
    time.sleep(1)
    print("DEBUG LOG (current page):" + elt.get_attribute("src"))
    url = elt.get_attribute("src")
    image = urllib.request.urlretrieve(url, str(pageNum)+".png")
    images.append(Image.open(str(pageNum)+".png"))

pdf_path = "C:\\Users\\conne\\Documents\\GitHub\\MusescoreToPDF\\sheetmusic.pdf"
images[0].save(pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])

for pageNum in range(1, numPages+1):
    os.remove(str(pageNum)+".png")