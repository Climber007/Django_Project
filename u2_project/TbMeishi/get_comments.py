import asyncio, time, random, pymongo
from pyppeteer import launch
from bs4 import BeautifulSoup
from config import *

def get_url():
    # pymongo 中读取 url
    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client.taobao.product

    items = db.find({"url":{"$exists":True}})

    for item in items:
        url = 'https:' + item['url']
        yield url

async def init():
    global browser, page
    browser = await launch(headless=False, dumpio=True, autoClose=False, userDataDir=r"F:\test",
                           args=['--no-sandbox', '--window-size=1920,1080', '--disable-infobars'])   # 进入有头模式
    page = await browser.newPage()           # 打开新的标签页
    await page.setViewport({'width': 1920, 'height': 1080})      # 页面大小一致
    await page.setUserAgent(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36")

    # await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await page.evaluateOnNewDocument('() =>{ Object.defineProperties(navigator,'
                                     '{ webdriver:{ get: () => false } }) }')
    print('页面初始化完成！')

#login-info > a.sn-login

async def login_taobao(url):

    # login
    # await page.waitForSelector('#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-sign > a.h')
    await page.click('#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-sign > a.h')
    await page.waitForSelector('div.fm-field > div.input-plain-wrap.input-wrap-loginid > input')
    await page.waitForSelector('div.fm-field > div.input-plain-wrap.input-wrap-password > input')
    await page.type('div.fm-field > div.input-plain-wrap.input-wrap-loginid > input', '425338522@qq.com')
    await asyncio.sleep(random.randint(1, 3))      # 休眠
    await page.type('div.fm-field > div.input-plain-wrap.input-wrap-password > input', 'ls17720422')
    await asyncio.sleep(random.randint(1, 3))
    await page.click('#login-form > div.fm-btn > button')  # 点击登录
    await asyncio.sleep(random.randint(1, 3))
    print('登录成功')
    time.sleep(1)

async def login_tianmao():
    await page.goto(url)
    # print('访问网页成功')
    # login
    await page.waitForSelector('#login-info > a.sn-login')
    await page.click('#login-info > a.sn-login')
    await page.waitForSelector('div.fm-field > div.input-plain-wrap.input-wrap-loginid > input')
    await page.waitForSelector('div.fm-field > div.input-plain-wrap.input-wrap-password > input')
    await page.type('div.fm-field > div.input-plain-wrap.input-wrap-loginid > input', '425338522@qq.com')
    await asyncio.sleep(random.randint(1, 3))  # 休眠
    await page.type('div.fm-field > div.input-plain-wrap.input-wrap-password > input', 'ls17720422')
    await asyncio.sleep(random.randint(1, 3))
    await page.click('#login-form > div.fm-btn > button')  # 点击登录
    await asyncio.sleep(random.randint(1, 3))
    print('登录成功')
    time.sleep(1)

async def get_comments():
    await page.waitForSelector('#J_TabBar > li.selected > a')
    html = await page.content()

    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('li', class_='J_KgRate_ReviewItem kg-rate-ct-review-item')
    for item in items:
        comment = {
            're_id': item.find('li')['id'],
            'date': item.find('div', class_='tb-r-date').find('span').text,
            'info': item.find('div', class_='J_KgRate_ReviewContent tb-tbcr-content ').text
        }
        print(comment)
    return comment




async def close_page():
    await browser.close()


async def main():
    await init()

    for i in get_url():
        print(i)

        print('访问网页成功')
        if i[2] == 'i':
            await page.goto(i)
            await login_taobao(i)
        else:
            await page.goto(i)
            await  login_tianmao()

        await get_comments()
        # await close_page()

asyncio.get_event_loop().run_until_complete(main())  # 调用

