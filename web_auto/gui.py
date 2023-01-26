from tkinter import *
from tkinter.messagebox import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import math
import random

driver = webdriver.Chrome()

tk = Tk()
tk.title('네이버 폼 오토')

tk.geometry("500x500")
tk.resizable(False, False)
###################################################
def perf(): #첫 번째 선택지만 선택
    url = entry1.get()
    n = int(entry2.get())
    b = int(entry3.get())
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
    showerror("완료", f"{end - start:.5f} sec, 완료!!")
##############################################

label1 = Label(tk,text='url').grid(row=0, column=0)
label2 = Label(tk,text='반복횟수').grid(row=1,column=0)
label3 = Label(tk,text='문항 개수').grid(row=2,column=0)

# 각 단위 입력받는 부분 만들기
entry1 = Entry(tk)
entry2 = Entry(tk)
entry3 = Entry(tk)


entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
entry3.grid(row=2,column=1)

btn1 = Button(tk,text='실행하기',bg='black',fg='white',command=perf).grid(row=3,column=0)


tk.mainloop()
 
#https://naver.me/5grkWhyD
