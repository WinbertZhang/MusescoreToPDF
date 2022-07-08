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
If you are using macOS, you may want to look at the version of chrome that you're using by going to chrome settings `Command + ,` and `About Chrome` at the bottom. Download the appropriate selenium driver [here](https://chromedriver.chromium.org/downloads). Make sure to download the `_m1` version if you are running on ARM.

After you extract the zip file, add it to your PATH:
```
sudo cp ~/Downloads/chromedriver /usr/local/bin
```

If you downloaded `chromedriver` elsewhere you may change the source path in the above command.

Verify that it exists by ensuring there's a proper output with `command -v chromedriver`. Now we can install the python dependencies using python's built in virtual environment llibrary:
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
You may run into the error "chromedriver" cannot be opened because the developer cannot be verified. In that case run
```
sudo xattr -d com.apple.quarantine /usr/local/bin/chromedriver
```

If your code works, follow the onscreen instructions! To stop the virtual environment run `deactivate`.

