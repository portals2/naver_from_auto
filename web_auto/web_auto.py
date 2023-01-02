# https://naver.me/FTkLTYx3


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

def perf(url, n, b): #첫 번째 선택지만 선택
    driver.get(url)

    time.sleep(1)

    for i in range(n):
        driver.execute_script('window.open("%s");'%url)
    print('{0}web_loding_done{0}'.format('@'*10))

    for j in range(n):
        driver.switch_to.window(driver.window_handles[j])
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
        for i in range(b+1): # n
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB,Keys.ENTER)
        print(j+1)
        # time.sleep(1)

    print('{0}all_done{0}'.format('@'*10))


perf('https://naver.me/FTkLTYx3', 30, 10) # 'url', 횟수, 문제개수

# 2, 3은 화살표 아래키 입력 램덤