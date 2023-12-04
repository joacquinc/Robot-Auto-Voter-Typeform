import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from timeit import default_timer as timer

options = Options()
options.add_experimental_option("detach", True)
j = 0
i = 0
while j >= 0:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://smtickets.com/events/view/11921#")
    driver.maximize_window()
    #answer = np.array(['GO ON WITHOUT ME', "I DON'T WANNA BE LIKE YOU", 'SITTING IN TRAFFIC', 'JAPANESE WHISKEY',
    #                   'GROWING UP IS', 'SET YOURSELF ON FIRE', 'LIE', 'LET THE GRASS GROW', 'YOU AGAINST YOURSELF',
    #                   "SOMEONE ELSE'S PROBLEM", 'WISH I HAD YOU', 'IF AND/OR WHEN', 'MUST BE NICE', 'END SCENE'])
    answer = np.array(['Painkiller', 'Younger', "Not Thinkin' Bout You", 'Face to Face', 'Dazed & Confused', "Don't Tell Me",
                       'Younger', 'as long as you care', 'Say', "Real Thing", 'distance', 'Hard Sometimes', 'Free Time', 'Down for You',
                       'Golden Years', 'Unsaid', 'say it over', 'courage', "Don't Cry", 'too many feelings', "Don't Tell Me",
                       'up to something'])
    #answer = np.array([])
    #answer = np.array([])
    driver.find_element(By.ID, "cookie-notification-accept").click()
    #button = driver.find_elements("xpath", '//button[text()="Proceed"]')
    button = driver.find_elements("xpath", "//div[contains(@class,'swal2-actions')][.//button[contains(text(),'Proceed')]]")

    for picks in answer:
        driver.find_element(By.ID, "answer").send_keys(answer[i])
        i+=1
        print("entered")
        #driver.find_element("xpath", '//button[text()="Proceed"]').click()
        break
    for picks in button:
        picks.click()
        break
    time.sleep(2)
    driver.close()
