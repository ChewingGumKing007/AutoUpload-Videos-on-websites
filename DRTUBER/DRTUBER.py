# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 15:45:44 2022

@author: ChewingGumKing_OJF
"""

#loads necessary libraries
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 
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
import itertools
import json
warnings.filterwarnings("ignore")

# reading the straight_data from the file 
with open('straight.txt') as f: 
    data1 = f.read()    
# reconstructing the data as a dictionary 
straight = json.loads(data1) 
# reading the gay_data from the file 
with open('gay.txt') as fa: 
    data2 = fa.read()    
# reconstructing the data as a dictionary 
gay = json.loads(data2) 
# reading the data from the file 
with open('trans.txt') as fah: 
    data3 = fah.read()    
# reconstructing the data as a dictionary 
trans = json.loads(data3)

try:
    dr_dir=os.getcwd()
    dr_dire=dr_dir.replace("\\DRTUBER","")
except:
    print("Could not get a valid current working directory, please manually provide one that ends in a 'DRTUBER' folder")
    dr_dire=input("Please provide a directory here; ")
try:
    path=dr_dire + "\\videos"
    os.chdir(path)
except:
    print('Kernel will restart!! Press "OK" and run the code again')
    exit()
#open a new window, load the website and logs in
driver = webdriver.Chrome(r'C:\Users\840 g3\Desktop\upload_web\chromedriver.exe')


url = 'https://www.drtuber.com/'
driver.get(url)
driver.maximize_window()
time.sleep(3)
#click the login key
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/span[1]/a').click()
time.sleep(3)


def login():
    #login with username and password
    login = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')

    #enter the credentials here
    login.send_keys('opeolu202')
    password.send_keys('Opeolu2012')
    time.sleep(2)
    #click_checkbox=driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/form/div[2]/div[3]/label').click()
    #time.sleep(1)
    login.send_keys(Keys.RETURN)
    time.sleep(5)

login()
try:
    password = driver.find_element_by_name('password')
    print('Could not log in, please retry after some hours')
    exit()
except:
    pass

#***can cut here

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
    FLV = glob.glob(path + '/*.flv')
    GP3 = glob.glob(path + '/*.3gp')
    MKV = glob.glob(path + '/*.mkv')


combined = itertools.chain(mp4, AVI, MOV, MPEG, MPG, WMV, FLV, GP3, MKV)
uploads=list(combined)
files=[i.rsplit("\\")[-1] for i in uploads]

##***can cut here
directory = os.getcwd()
for i in files:
    title = ".".join(i.split('.')[:-1])
    desc = ".".join(i.split('.')[:-1])
    #loads the upload page
    driver.get("https://www.drtuber.com/upload")
    
    time.sleep(2)
    #click upload video
    try:
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/button').click()
    except:
        pass
    
    #clicking the select file button
    try:
        
        driver.find_element_by_xpath('//*[@id="UploadButtonStyle"]').click()
    except:
        print('trying once more')
        try:
            driver.get("https://www.drtuber.com/upload")

            time.sleep(2)
            try:
                driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/button').click()
            except:
                pass

            try:
                #clicks the select file button
                driver.find_element_by_xpath('//*[@id="UploadButtonStyle"]').click()
            except:
                pass
        except:
            print('something is wrong')
            break
        
    
    #the time sleep here is very important
    time.sleep(5)

    pyautogui.write(r'{}'.format(path +'\\'+ ".".join(i.rsplit('.')[:-1])))
    pyautogui.press('return')
    
    time.sleep(15)
    try:
        pyautogui.write(r'{}'.format(directory+'\\'+ ".".join(i.rsplit('.')[:-1])))
        pyautogui.press('return')
    except:
        pass
    #fill in other details
    #fill in the title
    driver.find_element_by_xpath('//*[@id="video_title"]').send_keys(title)
    
    time.sleep(10)
    
    #check if there is error
    try:
        if len(driver.find_element_by_xpath('//*[@id="uload_file_errors_block"]').text) >5:
            print('an error occured, please make sure this video isnt too short or havent been uploaded previously')
            break
    except:
        pass
    
    
    try:
        driver.find_element_by_xpath('//*[@id="uploadVideo"]/div[3]/div[1]').click()
        chains = ActionChains(driver)

        chains.send_keys(Keys.ARROW_DOWN)
        chains.send_keys(Keys.ENTER)
        chains.perform()
    except:
        pass
    
    
    #pick one of three category types straight,gay or trans
    category_selection=["straight","gay","trans"]
    user_input=input("Enter any category type(just one of straight, gay or trans); ").lower()

    while user_input not in category_selection:
        user_input=input("Enter any category type(just one of straight, gay or trans); ").lower()

    category_type=user_input.strip().title()
    if category_type=="Straight":
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/form/div[3]/div[1]/div/a/span[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[9]/ul/li[1]/div").click()
        time.sleep(2)

        User_input=input("Enter any number of category(seperate each category by a comma); ").split(",")
        category=[i.strip().title() for i in User_input]
        category_copy=[i.strip().title() for i in User_input]
        count=0
        for j in category:
            if count>9:
                break
            try:
                xpath=straight[j] + "/div"
                driver.find_element_by_xpath(f"{xpath}").click()
                try:
                    alert = driver.switch_to.alert
                    alert.accept()
                    driver.implicitly_wait(20)
                except:
                    pass
            except:
                print(j," was not found. Please enter just one VALID category!!")
                j = input().title()

                if "," in j:
                    j = input().title()

                while j not in straight.keys():
                    print(j," was not found. Please enter one VALID category!!")
                    j = input().title()
                    if "," in j:
                        j = input().title()

                xpath = straight[j] + "/div"
                driver.find_element_by_xpath(f"{xpath}").click()
            count+=1

    elif category_type=="Gay":
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/form/div[3]/div[1]/div/a/span[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[9]/ul/li[2]/div").click()
        time.sleep(2)

        User_input=input("Enter any number of category(seperate each category by a comma); ").split(",")
        category=[i.strip().title() for i in User_input]
        category_copy=[i.strip().title() for i in User_input]
        count=0
        for j in category:
            if count>9:
                break
            try:
                xpath=gay[j] + "/div"
                driver.find_element_by_xpath(f"{xpath}").click()
                try:
                    alert = driver.switch_to.alert
                    alert.accept()
                    driver.implicitly_wait(20)
                except:
                    pass
            except:
                print(j," was not found. Please enter just one VALID category!!")
                j = input().title()

                if "," in j:
                    j = input().title()

                while j not in gay.keys():
                    print(j," was not found. Please enter one VALID category!!")
                    j = input().title()
                    if "," in j:
                        j = input().title()

                xpath = gay[j] + "/div"
                driver.find_element_by_xpath(f"{xpath}").click()
            count+=1


    elif category_type=="Trans":
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/form/div[3]/div[1]/div/a/span[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[9]/ul/li[3]/div").click()
        time.sleep(2)

        User_input=input("Enter any number of category(seperate each category by a comma); ").split(",")
        category=[i.strip().title() for i in User_input]
        category_copy=[i.strip().title() for i in User_input]
        count=0
        for j in category:
            if count>9:
                break
            try:
                xpath=trans[j] + "/div"
                driver.find_element_by_xpath(f"{xpath}").click()
                try:
                    alert = driver.switch_to.alert
                    alert.accept()
                    driver.implicitly_wait(20)
                except:
                    pass
            except:
                print(j," was not found. Please enter just one VALID category!!")
                j = input().title()

                if "," in j:
                    j = input().title()

                while j not in trans.keys():
                    print(j," was not found. Please enter one VALID category!!")
                    j = input().title()
                    if "," in j:
                        j = input().title()

                xpath = trans[j] + "/div"
                driver.find_element_by_xpath(f"{xpath}").click()
            count+=1

    else:
        print("Enter a valid category_type") 

    #fill in the description
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/form/div[8]/div[1]/textarea').send_keys(desc)

    #terms and conditions
    driver.find_element_by_xpath('//*[@id="uploadVideo"]/div[11]/div[2]/div').click()

    fatai=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/form/div[12]").get_attribute('innerHTML')
    blokos=fatai[188:188+8]
    while blokos=='disabled':
        time.sleep(10)
        fatai=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/form/div[12]").get_attribute('innerHTML')
        blokos=fatai[188:188+8]
    

    time.sleep(5)
    try:
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/form/div[12]/input[2]').click()
    except:
        print('it did not upload')
        break
    time.sleep(10)

    driver.implicitly_wait(10)
    #skip thumbnail
    try:
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div[2]/div/div[2]/div[3]/div/input').click()
        time.sleep(5)
        driver.implicitly_wait(10)
    except:
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[3]/div[2]/div/div[2]/div[3]/input").click()
        time.sleep(5)
        driver.implicitly_wait(10)
        pass

