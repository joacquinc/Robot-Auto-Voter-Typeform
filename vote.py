import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from timeit import default_timer as timer
from datetime import timedelta

options = Options()
options.add_experimental_option("detach", True)

begin = time.time()
i = 0
while i >= 0:
    start = timer()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://45ysidyz49o.typeform.com/TestAmbassdor?typeform-source=www.huawei.com")
    driver.maximize_window()
    pick1 = driver.find_elements("xpath",
                                 "//div[contains(@class,'Root-sc-__sc-164255h-0 kIkYlk ChoiceRoot-sc-__sc-1g50zb3-5 ixDWjX')][.//div[contains(text(),'Mark')]]")
    pick2 = driver.find_elements("xpath",
                                 "//div[contains(@class,'Root-sc-__sc-164255h-0 kIkYlk ChoiceRoot-sc-__sc-1g50zb3-5 ixDWjX')]")
    pick3 = driver.find_elements("xpath",
                                 "//div[contains(@class,'Root-sc-__sc-164255h-0 kIkYlk ChoiceRoot-sc-__sc-1g50zb3-5 ixDWjX')]")
    print(pick1)
    time.sleep(200)
    random_pick = random.sample(pick2, 3)
    pick2 = random_pick
    random_pick = random.sample(pick3, 3)
    pick3 = random_pick
    button = driver.find_elements("xpath", "//button[contains(@class, 'ButtonWrapper-sc-__sc-1qu8p4z-0 iPnBIj')]")

    for picks in pick1:
        picks.click()
        break
    for picks in pick2:
        picks.click()
        break
    for picks in pick3:
        picks.click()
        break
    for picks in button:
        picks.click()
        break

    time.sleep(3)
    end = timer()
    final = end - start
    tot = (time.time() - begin)
    i = i +1
    print('Loop: ', i, '. ', end=' ')
    print(f"{final:.02f} secs.", "Total Time: ", str(timedelta(seconds=tot)))
    driver.close()