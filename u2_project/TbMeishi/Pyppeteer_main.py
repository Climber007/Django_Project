import asyncio, time, random, pymongo
from pyppeteer import launch
from bs4 import BeautifulSoup
from config import *

url = 'https://www.taobao.com/'
browser, num = None, None

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

async def init(url):
    '''浏览器 初始化设置：窗口大小、UA、'''
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
    '''登录淘宝只需要首次登录'''
    # login
    await page.waitForSelector('#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-sign > a.h')
    await page.click('#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-sign > a.h')
    await page.waitForSelector('div.fm-field > div.input-plain-wrap.input-wrap-loginid > input')    # #fm-login-id

    await page.waitForSelector('div.fm-field > div.input-plain-wrap.input-wrap-password > input')
    await page.type('div.fm-field > div.input-plain-wrap.input-wrap-loginid > input', '425338522@qq.com')
    await asyncio.sleep(random.randint(1, 3))      # 休眠
    await page.type('div.fm-field > div.input-plain-wrap.input-wrap-password > input', 'ls17720422')
    await asyncio.sleep(random.randint(1, 3))
    await page.click('#login-form > div.fm-btn > button')  # 点击登录
    await asyncio.sleep(random.randint(1, 3))
    print('登录成功')

    print(await get_cookie(page))

async def get_cookie(page):
    ''' get cookies'''
    cookie_list = await page.cookies()
    cookies = ''
    for cookie in cookie_list:
        str_cookie = '{0}={1};'
        str_cookie = str_cookie.format(cookie.get('name'), cookie.get('value'))
        cookies += str_cookie
    print(cookies)
    return cookies


async def search():
    '''搜索关键字： 美食'''
    # search
    await page.waitForSelector('#q')
    await page.type('#q', '美食')
    await asyncio.sleep(random.randint(1, 3))
    await page.click('#J_TSearchForm > div.search-button > button')
    await page.waitForNavigation()
    await asyncio.sleep(2)
    print('搜索关键词成功')

async def get_page(num):
    await page.waitForSelector('#mainsrp-pager > div > div > div > div.form > input')
    await page.type('#mainsrp-pager > div > div > div > div.form > input', num)
    await asyncio.sleep(random.randint(1, 3))
    await page.click('#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')
    await asyncio.sleep(1)
    print('搜索第{}页'.format(num))

async def parse():
    try:
        # html = await page.evaluate('document.body.textContent', force_expr=True)
        html = await page.content()
        html = html.split('<body')[-1]
        soup = BeautifulSoup(html, 'lxml')
        items = soup.find_all('div', class_='item J_MouserOnverReq')
        if not items:
            print('数据为空')
        i = 0
        for item in items:
            products = {
                'title': item.find('div', class_='row row-2 title').text.strip(),
                'deal': item.find('div', class_='deal-cnt').text[:-3],
                'price': item.find('div', class_='price g_price g_price-highlight').text.strip(),
                'shop': item.find('div', class_='shop').text.strip(),
                'location': item.find('div', class_='location').text,
                'image': item.find('img', class_='J_ItemPic img')['data-src'],
                'url': item.find('div', class_='row row-2 title').find('a')['href'],
                'itemID': item.find('div', class_='pic').find('a')['data-nid'],
                'sellerID': item.find('div', class_='shop').find('a')['data-userid']
            }
            await save_to_mongo(products)
            i += 1

        print(i)
        print('-' * 30)
    except Exception as e:
        print(e)


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
        # await login()
        await search()
        for i in range(1, 2):
            num = str(i)
            await get_page(num)
            await parse()
    finally:
        await asyncio.sleep(6)
        # await browser.close()
    print('task done')


asyncio.get_event_loop().run_until_complete(main())  # 调用
