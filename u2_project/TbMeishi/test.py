from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
from config import *

import time, datetime, random, re, pymongo

# 创建Chrome浏览器对象，这会在电脑中打开一个窗口
browser = webdriver.Chrome('C:/Users/dell/Downloads/chromedriver_win32 (1)/chromedriver.exe')
wait = WebDriverWait(browser, 10)
url = 'https://www.taobao.com/'
key = '美食'

def login(url):
    browser.get(url)
    submit = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-sign > a.h")))
    submit.click()
    input_username = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.fm-field > div.input-plain-wrap.input-wrap-loginid > input')))
    input_password = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.fm-field > div.input-plain-wrap.input-wrap-password > input')))
    input_login = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#login-form > div.fm-btn > button')))
    input_username.send_keys('425338522@qq.com')
    time.sleep(1)
    input_password.send_keys('sy7646001')
    time.sleep(1)
    input_login.click()
    print('淘宝登录成功！')
login(url)

def search(key:str):
    # 搜索框
    input = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#q")))

    # 点击搜索按钮
    submit = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
    time.sleep(1)
    input.send_keys(key)
    time.sleep(1)
    submit.click()

search(key)