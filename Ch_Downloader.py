# import sys
from tkinter.filedialog import askdirectory, askopenfilename

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time

timeout = 60  # seconds


def get_user_choice():

    input("press enter when ready to choose the list of songs")
    songs_list = askopenfilename(initialdir='.')

    if not songs_list:
        raise ValueError("You did not choose the songs list file.")
    if not songs_list.endswith("txt"):
        raise ValueError("A text file must be chosen.")

    input("press enter when ready to choose the download directory")
    download_directory = askdirectory(initialdir='.')

    if not download_directory:
        raise ValueError("You did not choose the download directory.")

    return songs_list, download_directory


songs_list, download_directory = get_user_choice()

# Setting chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'download.default_directory': download_directory})

# Starting the Driver
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()


def downloader():

    driver.get("http://convert2mp3.net/en/")

    search = driver.find_element_by_name("url")
    search.clear()
    search.send_keys(url.strip())
    search.send_keys(Keys.RETURN)

    try:
        myElem = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.NAME, 'tags'))
        )
    except TimeoutException:
        print("Timed out waiting for page to load")

    button_cont = driver.find_elements_by_tag_name("a")[12]
    button_cont.click()

    button_download = driver.find_elements_by_tag_name("a")[9]
    button_download.click()

    time.sleep(.500)


with open(songs_list) as in_file:
    for url in in_file:
        downloader()


# driver.quit()
