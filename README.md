# MusescoreToPDF
Uses a single Python script to scrape [Musescore](https://musescore.com) and saves the score as a pdf. Below are the instructions for use with Windows 10 and above.

## Dependencies

- Chrome version 103
- Python 3
- Selenium, Pillow, Pyautogui (run below to install)
```
pip install selenium
pip install Pillow
pip install pyautogui
```

## Instructions
    1. run python main.py
    2. enter valid musescore url
    3. pdf will be in folder named as MusescoreToPDF.pdf

## Additional Notes
Don't click on the screen while program is running  
DISCLAIMER: We are not responsible for any legal issues regarding users of our software

## MacOS
If you are using macOS, you may want to look at the version of chrome that you're using, and download the appropriate selenium driver [here](https://chromedriver.chromium.org/downloads). Make sure to download the `_m1` version if you are running on ARM.

After you extract the zip file, add it to this directory. Now install the python dependencies:

```
pip3 install venv
python3 -m venv venv
source venv/bin/activate
```
Now that you're in a virtual environment, you can install the required dependencies and run your code.
```
pip3 install -r requirements.txt
python3 main.py
```
Follow the onscreen instructions! To stop the virtual environment run `deactivate`.

