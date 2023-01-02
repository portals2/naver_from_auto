# https://naver.me/FTkLTYx3


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

def perf(url, n): #첫 번째 선택지만 선택
    driver.get(url)

    time.sleep(1)

    for i in range(n-1):
        driver.execute_script('window.open("%s");'%url)

    for i in range(n):
        driver.switch_to.window(driver.window_handles[i])
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
        for i in range(n+1): # n
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB,Keys.ENTER)
        time.sleep(1)

    while(True):pass 

perf('https://naver.me/FTkLTYx3', 10) # 'url', 횟수