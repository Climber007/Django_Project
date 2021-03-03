import asyncio, time
from pyppeteer import launch

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    url = 'https://www.taobao.com/'
    time.sleep(2)
    await page.goto(url)
    # content = await page.content()
    content = await page.evaluate('document.body.textContent', force_expr=True)
    e = await page.querySelectorAll('#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-user > a')
    for item in e:
        print(await item.getProperty('textContent'))
        title_str = await (await item.getProperty('textContent')).jsonValue()
        print(title_str)

    # 获取元素的某个属性值
    # await browser.close()
asyncio.get_event_loop().run_until_complete(main())