# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 00:10:59 2022

@author: ChewingGumKing_Ahmed
"""

#loads necessary libraries
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
from datetime import datetime
import openpyxl
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
import shutil
import glob
import os
import warnings
import copy
import itertools
warnings.filterwarnings("ignore")
try:
    path=os.getcwd() + "\\videos"
    os.chdir(path)
except:
    print('Restart the kernel first')
    exit()

mp4 = []
AVI = []
MOV = []
MPEG = []
MPG = []
WMV = []
WMA = []
MPG3 = []
x264 = []
M4V = []
for k in os.listdir():
    mp4 = glob.glob(path + '/*.mp4')
    AVI = glob.glob(path + '/*.avi')
    MOV = glob.glob(path + '/*.mov')
    MPEG = glob.glob(path + '/*.mpeg')
    MPG = glob.glob(path + '/*.mpg')
    WMV = glob.glob(path + '/*.wmv')
    WMA = glob.glob(path + '/*.wma')
    MPG3 = glob.glob(path + '/*.mpg3')
    x264 = glob.glob(path + '/*.x264')
    M4V = glob.glob(path + '/*.m4v')


combined = itertools.chain(mp4, AVI, MOV, MPEG, MPG, WMV, WMA, MPG3, x264, M4V)
uploads=list(combined)
files=[i.rsplit("\\")[-1] for i in uploads]

#open a new window, load the website and logs in
driver = webdriver.Chrome(r'C:\Users\840 g3\Desktop\upload_web\chromedriver.exe')

url = 'https://www.tnaflix.com/upload/'
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)
#click the login key
driver.find_element_by_xpath('/html/body/header/div[1]/div[2]/div/a[1]/i').click()
driver.implicitly_wait(5)
#login with username and password
login = driver.find_element_by_name('login')
password = driver.find_element_by_name('password')

#enter the credentials here
login.send_keys('opeolu202')
password.send_keys('Opeolu2012')
time.sleep(2)
click_checkbox=driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/form/div[2]/div[3]/label').click()
driver.implicitly_wait(5)
login.send_keys(Keys.RETURN)
time.sleep(5)


click_upload=driver.find_element_by_xpath('/html/body/header/div[1]/div[2]/a/i').click()
driver.implicitly_wait(3)
driver.switch_to.window(driver.window_handles[1])
click_upload=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/button').click()
driver.implicitly_wait(5)

for idx, k in enumerate(files):
    driver.get('https://beta-upload.tnaflix.com/uploads.php')
    try:
        alert = driver.switch_to.alert
        alert.accept()
        driver.implicitly_wait(20)
    except:
        pass
    desc = k.split(".")[0]
    time.sleep(5)
    
    driver.find_element_by_xpath('/html/body/section/div/div[2]/div/div/div/div/div/div[1]/span').click()
    
    time.sleep(5)

    pyautogui.write(r'{}'.format(path+'\\'+k.split('.')[0]))
    pyautogui.press('return')
    
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="videoDescription"]').send_keys(desc)
    time.sleep(2)
    #select a category
    User_input=input("Enter any number of category(seperate each category by a comma); ").split(",")
    category=[i.strip().title() for i in User_input]
    
    category_copy=[i.strip().title() for i in User_input]
    count=0
    for i in range(1,75):
        if count==len(category):
            break
        if count>4:
            break
        
        try:
            xpath=f'/html/body/section/div/div[2]/div/div/div/div/div[2]/form/div[1]/div[2]/div[2]/div/div[{i}]'
        
            text=driver.find_element_by_xpath(xpath).text
            
        except:
            xpath=f'/html/body/section/div/div[2]/div/div/div/div/div[1]/form/div[1]/div[2]/div[2]/div/div[{i}]'

            text=driver.find_element_by_xpath(xpath).text 
      

        if text in category:
            driver.find_element_by_xpath(xpath).click()
            category_copy.remove(text)
            count+=1

    if len(category_copy)>=1:
        print("This list of category was not found")
        print(category_copy)
        
    
    print("Ready to upload video", idx+1)
    try:
        alert = driver.switch_to.alert
        alert.accept()
        driver.implicitly_wait(20)
    except:
        pass
    ht=driver.find_element_by_xpath('/html/body/section/div/div[2]/div/div/div/div/div[1]/form/div[1]/div[6]/div/button[1]').text
    
    while ht!='Save & Close':
        time.sleep(10)
        ht=driver.find_element_by_xpath('/html/body/section/div/div[2]/div/div/div/div/div[1]/form/div[1]/div[6]/div/button[1]').text


    driver.find_element_by_xpath('/html/body/section/div/div[2]/div/div/div/div/div[1]/form/div[1]/div[6]/div/button[1]').click()
    time.sleep(4)
    print("video", idx+1, "uploaded")
 