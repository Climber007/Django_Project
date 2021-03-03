import asyncio, time, random, pymongo, re, ssl

from pyppeteer import launch
from bs4 import BeautifulSoup
from config import *
from requests import Session
from requests.models import Response

client = pymongo.MongoClient('mongodb://localhost:27017')

def get_url():
    # pymongo 中读取 url
    db = client.taobao.product
    items = db.find()
    for item in items:
        url = 'https:' + item['url']
        # itemID = item['itemID']
        # sellerID = item['sellerID']
        yield url, itemID, sellerID


async def get_spuID(url):
    # no login
    browser = await launch(headless=True, dumpio=True, autoClose=False, userDataDir=r"F:\test",
                           args=['--no-sandbox', '--window-size=1920,1080', '--disable-infobars'])   # 进入有头模式)
    page = await browser.newPage()

    await page.setViewport({'width':1920, 'height':1080})
    await page.setUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36")
    await page.evaluateOnNewDocument('() =>{ Object.defineProperties(navigator,'
                                     '{ webdriver:{ get: () => false } }) }')
    await page.goto(url)
    await asyncio.sleep(random.randint(1, 3))

    res = await page.content()
    if url[8] == 'd':   # tm
        spu = re.findall(r'spuId...[0-9]*', res)[0]
        spuID = spu.split(':')[-1][1:]
        spuID = re.findall(r'[0-9]*', spuID)[0]
    else:    # tb
        spu = re.findall(r'spuId...[0-9]*', res)[0]
        spuID = spu.split('=')[-1][:-1]
        spuID = re.findall(r'\d{1,}', spuID)[0]
    print('---传入url：{}, 解析spuID:{}'.format(url, spuID))
    await browser.close()

async def main():
    for i in get_url():
        url = i[0]
        await get_spuID(url)
    print('task done')

asyncio.get_event_loop().run_until_complete(main())  # 调用

def get_comment(num): # 爬取 第几页

    # 时间戳 补全
    s_list = str(time.time()).split('.')
    _ksTS = '{}{}_1531'.format(s_list[0],s_list[1][:3])   # 1531 会动态变化
    num = num + 1
    for i in range(1,num): # 爬取页码
        params = {"auctionNumId":"540674962228",
                  "userNumId":"60020847",
                  "currentPageNum":num,
                  "pageSize":"20",
                  "rateType":"",
                  "orderType":"sort_weight",
                  "attribute":"",
                  "sku":"",
                  "hasSku":"false",
                  "folded":"0",
                  "ua":"137%232%2FE9hE9o9ablByN34BHvFwAGInQe3B4u%2FEzQVL034DFNxJpqW3wYpMj5HpqVAs7NUB4fXK7ON8gl%2Fqha96m%2FbPT3c6S1FwNNxUdHKISH5mrgoV%2F2AaUxBziXJ8eWASbIzIPT4GvEziwUA0%2B17t%2FXKaS%2BNh8VAYam3jgheW50UqIhtD4y9n7CtO8AlW4BljQoj%2Bdj53yzhz0M%2FJopiI3ad2FWEdOBTxyLiV0DTBwiXgV93XZUuwvPXbkKt4299N98VFXnvYXEALWa%2FNacB3wfRP615AHtQJOxv2YsV8EjEUikR5U%2F8jqSW6ZT2PLGaPrAOkwoXQ7qLObLEA6B5Vea%2FCmP4W8oyHBZzBs0xNctV%2BGO%2FiDQ%2FudYM7cKVWqI0nWlvEGfz%2BWyl3MHsjogdeytXg5O7fioAdrtH3vHC7Cr9A%2BAM0e70T0XpfNs%2Fh21xNvoNo5mYOBhhEeUP5vxGTBcT0Um1AEi%2BsIhYrJx19QByLSkQefJ%2BZDVpRUc1AIy%2BtpWpbMc0ZQiqtpcQonJ%2BZfCpImA8zSoZpIWbfO%2BmZikoZiWmonDQwDVbk%2FwjAEy%2BpipYTOx1lgippim7efJ%2BGXVpRJc1Iei%2BppVYT%2FR9hT27fP9iIS2oEG%2FVkaaA9EZJNMAzkr%2Bb4r%2BmKa1dpkyKMPb%2BEeM8olVxHcpeM2X%2B6N55ErMTMjMsp0nM0%2Bvabnbogftz%2BBpov2vWMPEqYlPahiwdLqFsBn7kMCQIPU0hyCiQIWnjamGIffH%2F%2B2g4CAcWH9BIzw5n%2BEGRhJFLpMP2gGFxi3cDFi3Fc3rBro1Mpof9ls0IlUsHeUFdjQgk%2FrROYCPexkS7FcfUvNZFwOxhvc9zBRMvxc6m%2BUu6l2gClPdFQnR8wO9N%2FlllmesYAOYPSO1qybfdcxa%2Fg64%2FJy1HTGQyqQ7oYTbfsyaYfaXBFWIbvKTToplz6%2BeRHFLRyYfGaG%2Be7Dx8m8kTUPdz6tWbbEtY6SFyxCqH5USSXK%3D",
                  "_ksTS":_ksTS,
                  "callback":"jsonp_tbcrate_reviews_list"}

        raw_url = 'https://rate.taobao.com/feedRateList.htm?'
        res = requests.get(raw_url, params=params, headers=headers)
        if res.status_code:

            print('开始解析数据！')
            data = re.findall(r'{.*}', res.text)[0]
            print(data)
            datas = json.loads(data)
            print(datas['comments'])
            for j in datas['comments']:
                comment = j['content']
                print(comment)
        else:
            print('网页下载 失败，请调整 参数')
        print('\n')
        print('第{}页评论数据爬取成功！----------------'.format(i))