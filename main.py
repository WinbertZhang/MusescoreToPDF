from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image, UnidentifiedImageError
import pyautogui
import urllib.request
import warnings
import os
import unicodedata
import re
import hashlib


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")


PDF_PATH = "converted_pdfs"
CACHE_PATH = ".pdf_data"

while True:
    print("Enter a valid musescore url")
    url = input()
    if not (url.startswith("https://musescore.com") or url.startswith("musescore.com")):
        print("Invalid url")
    else:
        break

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get(url)
driver.implicitly_wait(5)
warnings.filterwarnings("ignore", category=DeprecationWarning)

driver.find_element(
    By.XPATH,
    "/html/body[@class='js desktop js-cookie-compliance theme-react summer-sale']/div[@class='js-page react-container']/div[@class='_5tn-M']/section[@class='HJV7K']/main[@class='_1sdLO _1ss1d']/div[@class='_2G3ri']/div[@class='_3UHUA']/div[@class='_36dkj']/div[@id='jmuse-scroller-component']",
).click()
elt = driver.find_element(
    By.XPATH,
    "/html/body[@class='js desktop js-cookie-compliance theme-react summer-sale']/div[@class='js-page react-container']/div[@class='_5tn-M']/section[@class='HJV7K']/main[@class='_1sdLO _1ss1d']/div[@class='_2G3ri']/div[@class='_3UHUA']/div[@class='_36dkj']/div[@id='jmuse-scroller-component']/div[@class='vAVs3'][1]/img[@class='_2zZ8u']",
)
alt_tag = elt.get_attribute("alt")

images = []
piece_name = driver.find_element(
    By.XPATH, "/html/body/div[1]/div/section/aside/div[1]/h1"
).text
short_piece_name = slugify(piece_name, True)
hash_file = hashlib.sha256(short_piece_name.encode("utf-8")).hexdigest()
if os.path.isdir(CACHE_PATH) and os.path.isfile(f"{CACHE_PATH}/{hash_file}"):
    print(
        "You have already rendered this pdf! Please check your 'converted_pdfs' folder."
    )
    driver.quit()
    exit()

try:
    numPages = int(alt_tag[::-1][5 : alt_tag[::-1].find(" ", 6)][::-1])
except:
    print("Number of Pages not found")

driver.maximize_window()
pyautogui.click(100, 100)
for i in range(10):
    pyautogui.hotkey("ctrl", "-")
    pyautogui.hotkey("command", "-")

for pageNum in range(1, numPages + 1):
    elt = driver.find_element(
        By.XPATH,
        "/html/body[@class='js desktop js-cookie-compliance theme-react summer-sale']/div[@class='js-page react-container']/div[@class='_5tn-M']/section[@class='HJV7K']/main[@class='_1sdLO _1ss1d']/div[@class='_2G3ri']/div[@class='_3UHUA']/div[@class='_36dkj']/div[@id='jmuse-scroller-component']/div[@class='vAVs3']["
        + str(pageNum)
        + "]/img[@class='_2zZ8u']",
    )
    src_tag = elt.get_attribute("src")
    for i in range(5):
        pyautogui.press("down")
    print("DEBUG LOG (current page): " + src_tag)
    try:
        image = urllib.request.urlretrieve(src_tag, str(pageNum) + ".png")
        images.append(Image.open(str(pageNum) + ".png"))
    except UnidentifiedImageError:
        print(
            "The format of this pdf is not supported at the time. We're working on it!"
        )
        driver.quit()
        exit()

if not os.path.isdir(PDF_PATH):
    os.makedirs(PDF_PATH)

if not os.path.isdir(CACHE_PATH):
    os.makedirs(CACHE_PATH)

with open(f"{CACHE_PATH}/{hash_file}", "w") as f:
    f.write(short_piece_name)

images[0].save(
    f"{PDF_PATH}/{short_piece_name}.pdf",
    "PDF",
    resolution=100.0,
    save_all=True,
    append_images=images[1:],
)

for pageNum in range(1, numPages + 1):
    os.remove(str(pageNum) + ".png")

driver.quit()
