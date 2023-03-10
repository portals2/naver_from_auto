# https://naver.me/FTkLTYx3


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import math
import random

driver = webdriver.Chrome()
#exe로 만든다고 하다면 크롬파일은 어디서 
#가죠와야하는 거지?

def perf(url, n, b): #첫 번째 선택지만 선택
    driver.get(url)
    start = time.time()
    math.factorial(100000)
    
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
            r = random.choices(range(1, 4), weights=[0.85, 0.1, 0.05])
            if (r[0] == 1):
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB,Keys.ENTER)
            elif (r[0] == 2):
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB,Keys.ARROW_DOWN,Keys.ENTER)
            else:
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB,Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ENTER)
        print("count", j+1)

    print('{0}{1} all_done{0}'.format('@'*10, n))
    end = time.time()
    print(f"{end - start:.5f} sec")

# perf('https://naver.me/FTkLTYx3', 100, 10) # 'url', 횟수, 문제개수

# 2, 3은 화살표 아래키 입력 램덤

