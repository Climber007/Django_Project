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

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def search():
    try:
        browser.get('https://www.taobao.com/')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
        )  # 选择输入框

        # 点击搜索按钮
        submit = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        time.sleep(1)
        input.send_keys('美食')
        time.sleep(1)
        submit.click()

        # login
        input_username = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.fm-field > div.input-plain-wrap.input-wrap-loginid > input')))
        input_password = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.fm-field > div.input-plain-wrap.input-wrap-password > input')))
        input_login = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#login-form > div.fm-btn > button')))

        input_username.send_keys('425338522@qq.com')
        print('账户名输入完成')
        time.sleep(1)
        input_password.send_keys('sy7646001')
        print('密码输入完成')
        # input_password.send_keys(Keys.ENTER)
        time.sleep(1)
        # 等待登录按钮
        input_login.click()
        print('登录成功!')

        # 页数
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
        get_products()
        return total.text
    except TimeoutException:
        return search()   # 超时重新请求；

def next_page(page_number):
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        time.sleep(2)

        # 判断是否翻页成功
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number)))

        get_products()

    except TimeoutException:
        next_page(page_number)

def get_products():
    # 宝贝信息
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-pager .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnl').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)

def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('保存到mongo_DB成功', result)
    except Exception:
        print('保存到mongo失败', result)




def main():
    total = search()
    total = int(re.compile('(\d+)').search(total).group())
    for i in range(2, 3):
        next_page(i)

    print(total)

if __name__ == '__main__':
    main()