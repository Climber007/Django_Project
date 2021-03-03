import requests, time, datetime, re, json, random
from bs4 import BeautifulSoup

# 爬取 淘宝店铺 评论
headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
    'referer': "https://item.taobao.com/item.htm?spm=a230r.1.14.46.4b5d6494N4F7IF&id=540674962228&ns=1&abbucket=11",
    # detail_url
    'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
    'cookie': "t=ca1218ded111b679cb6c4b99bd75a3f2; _samesite_flag_=true; cookie2=149c11417406eff38ccf9b4198ddf2c3; thw=cn; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zMG1aAN%2F0TkjYGZjkj6rrK3kv4LgxGhtlxvv2n2588IGecb7R1wUpOfVv1057o9qO7dyRk5yfQu4GVjRK3fWdVWAxRAzI79usNDfxPYF%2FQfBXQbh9XAmvFw%2FtACdTo%2FwRIbTB3YqllMbIqwq1qqFkjmfV%2B4mgp04JA2eYelYIZUnuJVOPV%2FMZaUue1wmfqwYIaR19qz16m6XQp07EKMycwerJssXk2mufOvcEmRH0sSSyMoIU8wNK7yZdkvufcVkm55HnxHewhMAkXKqzAOJk7zm9x1u33aljgJKe%2Fy3Ry78qwrP84O%2FUQAV6huyKkZvzJ12J9Wp7jacYyNTwZ0BG%2FSAw%3D; enc=HCSX9KVT1HvH7RWFb%2FjTy8il6cDJVGGiZCkasIPrpohgtC9Auc6W5WDDVKNfwHvWodZvDEjh3EwX%2BmnEh78Gqw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; cna=kpgeGFopnXwCAXWWvFYMOP+B; v=0; lgc=%5Cu6D77%5Cu7684%5Cu590F%5Cu65E5%5Cu54E6; dnk=%5Cu6D77%5Cu7684%5Cu590F%5Cu65E5%5Cu54E6; tracknick=%5Cu6D77%5Cu7684%5Cu590F%5Cu65E5%5Cu54E6; mt=ci=103_1; xlly_s=1; _tb_token_=55eb3bb81633e; uc3=nk2=2QNmkkQKTuv1eQ%3D%3D&vt3=F8dCufJEB9MF8sfeUWM%3D&lg2=URm48syIIVrSKA%3D%3D&id2=UUpidH%2F8V9rDDA%3D%3D; csg=a3029427; sgcookie=E100AQC15FbnZXLDnkfBhB9y166vSLVrGOAfXTf6S%2FVCJ63DAo2uWjnx6koozwldJml%2BikYVc%2FzaVe%2B%2Bz%2B3a3SzzHg%3D%3D; skt=d72d0c96c7cb57a5; existShop=MTYwNDExNDc2Nw%3D%3D; uc4=id4=0%40U2gosS8c%2FnmsJJVcqTw6hKdeLlKW&nk4=0%402%2BUl7E4E67VAwJxWyaOM9Ds%2BHBkP; _cc_=VFC%2FuZ9ajQ%3D%3D; uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie14=Uoe0abO8CKxqTw%3D%3D&existShop=false&pas=0&cookie21=URm48syIZJfmYzXrEixrAg%3D%3D; _m_h5_tk=d9dcc45aaedc0dd49107639b03bd2fee_1604141096157; _m_h5_tk_enc=f81641f67d2d17a31221e5619e2e185b; tfstk=cDQ5Beb-GYD5adqEz_N2aXRj-QYla5HXTuOdNgF444LQD0CkHsmx7dORzMDikhdf.; l=eBxFBi4lOATgyVdMKO5aFurza77tuQAbzsPzaNbMiInca1ldZFtRgNQVdgg6odtjgt5UzetyNxVOSRe284U38tTH3O8qOC0eQNvpRe1..; isg=BMnJLx0O8uWvD46UDZiMa40E2PUjFr1In9zGRGs8XbDnsuvEs2dgGeUk9BYE6lWA"
}

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
get_comment(2)





