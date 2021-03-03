
import asyncio, time, random, pymongo
from pyppeteer import launch
from bs4 import BeautifulSoup
from config import *

url = 'https:'+'//item.taobao.com/item.htm?id=622552925786&ns=1&abbucket=15#detail'


MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_TABLE = 'comments'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


# 爬取 单个商品网页的 评论信息；
async def init(url):
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
    await page.goto(url) # 访问主页

async def login():
    # login
    await page.waitForSelector('#sufei-dialog-close')
    await page.click('#sufei-dialog-close')
    print('登录成功')
    try:
        key = await page.waitForXPath('//*[@id="J_TabBar"]/li[2]/a')
        await key.click()
        await asyncio.sleep(random.randint(1, 3))
        html = await page.content()
        # print(html)
    except Exception as e:
        print(e)



    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('li', class_='J_KgRate_ReviewItem kg-rate-ct-review-item')
    if items:
        for item in items:
            print(item)
            comment = {
                # 're_id': item.find('li')['id'],
                'date': item.find('span', class_='tb-r-date').text,
                'info': item.find('div', class_='J_KgRate_ReviewContent').text.strip()
            }

            await save_to_mongo(comment)


    # return comment

async def save_to_mongo(result):
    print('开始保存数据')
    try:
        if db[MONGO_TABLE].insert(result):
            print('保存到mongo_DB成功', result)
    except Exception:
        print('保存到mongo失败', result)


async def main():
    try:
        await init(url)
        await login()
        # await search()
        # for i in range(1, 4):
        #     num = str(i)
        #     await get_page(num)
        #     await parse()
    finally:
        await asyncio.sleep(6)
        # await browser.close()
    print('task done')
asyncio.get_event_loop().run_until_complete(main())  # 调用