from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import pyautogui
import urllib.request
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

driver.find_element(By.XPATH, "/html/body[@class='js desktop js-cookie-compliance theme-react summer-sale']/div[@class='js-page react-container']/div[@class='_5tn-M']/section[@class='HJV7K']/main[@class='_1sdLO _1ss1d']/div[@class='_2G3ri']/div[@class='_3UHUA']/div[@class='_36dkj']/div[@id='jmuse-scroller-component']").click()
elt = driver.find_element(By.XPATH, "/html/body[@class='js desktop js-cookie-compliance theme-react summer-sale']/div[@class='js-page react-container']/div[@class='_5tn-M']/section[@class='HJV7K']/main[@class='_1sdLO _1ss1d']/div[@class='_2G3ri']/div[@class='_3UHUA']/div[@class='_36dkj']/div[@id='jmuse-scroller-component']/div[@class='vAVs3'][1]/img[@class='_2zZ8u']")
altTag = elt.get_attribute("alt")
images = []
pdf_path = "converted_pdfs/MusescoreToPDF.pdf"

try:
    numPages = int(altTag[::-1][5:altTag[::-1].find(" ", 6)][::-1])
except:
    print('Number of Pages not found')

driver.maximize_window()
pyautogui.click(100, 100)
for i in range(10):
    pyautogui.hotkey('ctrl', '-')
    pyautogui.hotkey('command', '-')

for pageNum in range(1, numPages+1):
    elt = driver.find_element(By.XPATH, "/html/body[@class='js desktop js-cookie-compliance theme-react summer-sale']/div[@class='js-page react-container']/div[@class='_5tn-M']/section[@class='HJV7K']/main[@class='_1sdLO _1ss1d']/div[@class='_2G3ri']/div[@class='_3UHUA']/div[@class='_36dkj']/div[@id='jmuse-scroller-component']/div[@class='vAVs3']["+str(pageNum)+"]/img[@class='_2zZ8u']")
    for i in range(5):
        pyautogui.press('down')
    print("DEBUG LOG (current page): "+ elt.get_attribute("src"))
    url = elt.get_attribute("src")
    image = urllib.request.urlretrieve(url, str(pageNum)+".png")
    images.append(Image.open(str(pageNum)+".png"))\

os.makedirs('converted_pdfs')

images[0].save(pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])

for pageNum in range(1, numPages+1):
    os.remove(str(pageNum)+".png")
