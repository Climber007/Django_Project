import requests, time, datetime, re, json, random
from bs4 import BeautifulSoup

# 爬取 淘宝店铺 评论
headers = {
    'accept-language': "zh-CN,zh;q=0.9",
    'cookie': "tk_trace=1; cna=8n6QGK4lvlICAXWWvAjQgrYX; t=cbd57b25289c33451aa3acf8d7e61a06; _tb_token_=eb87d383e1647; cookie2=2a4ac6e524ecb1fac8839b017a02ea46; dnk=%5Cu6D77%5Cu7684%5Cu590F%5Cu65E5%5Cu54E6; uc1=cookie14=Uoe1g8so%2Bmb0oA%3D%3D&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&pas=0&cookie15=VT5L2FSpMGV7TQ%3D%3D&existShop=false&cookie21=URm48syIZJfmYzXrEixrAg%3D%3D; uc3=lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dCuAFVoeshJPUIAV4%3D&id2=UUpidH%2F8V9rDDA%3D%3D&nk2=2QNmkkQKTuv1eQ%3D%3D; tracknick=%5Cu6D77%5Cu7684%5Cu590F%5Cu65E5%5Cu54E6; lid=%E6%B5%B7%E7%9A%84%E5%A4%8F%E6%97%A5%E5%93%A6; uc4=nk4=0%402%2BUl7E4E67VAwJxWyaKugu8BGIXg&id4=0%40U2gosS8c%2FnmsJJVcqT2RlY%2F3YLoE; lgc=%5Cu6D77%5Cu7684%5Cu590F%5Cu65E5%5Cu54E6; sgcookie=E100eBlElStkkd6tcEQdbN%2Blck5widhjC6miK%2B%2BVt2jFpNNiNyyB%2F0dbaDntyKQEtIyjJf5mP%2BllvxIVlxJV3xuLlw%3D%3D; csg=03f1ecec; enc=sO8vSOSDq0u%2BEoz4r7AujbxU6hvOnRzg6Sdw02oVLEnV6T1eeT5xRrQmpqWjfjFFk%2BIJPMjL6IGUyntXHdPlMg%3D%3D; xlly_s=1; tfstk=c-_VB39g0rUVQV8_vETZhyKflgZAZHXGH4JymGehqJh4jExcieD9ZSjHaKJLrnf..; l=eBgFIyvPjjY-19mUBO5Cnurza779uIdb8sPzaNbMiInca6BhZeGd-NCIW8zJodtjgtfvpeKz4rz6LRnw-f4_Wr_ceTwhKXIpBxv9-; isg=BKWlnh4mKZx9v03xh8ERj1wKtGHf4ll0uIJrdaeL9VzMvsQwbjM8Rl6YSCLIvnEs",
    'referer': "https://detail.tmall.com/item.htm?id=596581206111&ali_refid=a3_430583_1006:1214580125:N:Z3n/4zOj22Oo%20vA/6f3FTQ==:743abf6e93404b8570a15aa390883b91&ali_trackid=1_743abf6e93404b8570a15aa390883b91&spm=a230r.1.14.3",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
    }

# def tm_comment(num): # 爬取 第几页

# 时间戳 补全
s_list = str(time.time()).split('.')
_ksTS = '{}{}_{}'.format(s_list[0],s_list[1][:3],s_list[1][-4:])   # 1531 会动态变化
callback = 'jsonp{}'.format(str(int(s_list[1][-4:])+1))
print(_ksTS, callback)

# num = num + 1
for i in range(1,2): # 爬取页码
    params = {"itemId":"620355053596",
              "spuId":" 1705147973",
              "sellerId":" 2081314055",
              "order":"3",
              "currentPage":"1",
              "append":"0",
              "content":"1",
              "tagId":"",
              "posi":"",
              "picture":"",
              "groupId":"",
              "ua":"098#E1hvaQvUvbpvUvCkvvvvvjiWP2Fhlj1hR2MwAjEUPmPhtjibRLdWgjinRFFUzj3Wi9hvCvvvpZpRvpvhvv2MMQvCvvOv9hCvvvmIvpvUvvCCnP6EDUkUvpvVvpCmp/2ZKvhv8vvvpjLMMMMtvvC2Epvvv+Wvvhi8vvmmZvvvoyIvvUECvvCjGQvvvSGUvpCWvnHZxC0g+LoQRpn+yX79R3oAVAdWaXp7+ul1occ6+u0OV16F/E7reEKKfvDrAEkK5dUf8r3lj3TAdcHUafmAdX9fjomxfX9wdiZDNF9CvvpvvhCv",
              "needFold":"0",
              "_ksTS":_ksTS,
              "callback":callback}

    # time.sleep(random.random)
    raw_url = 'https://rate.tmall.com/list_detail_rate.htm?'
    res = requests.get(raw_url, params=params, headers=headers)
    print(res.status_code, res.text)
    if res.status_code:
        print('开始解析数据！')
        data = re.findall(r'{"auctionPicUrl.*}]', res.text)[0]
        # datas = re.findall(r'"rateContent":"([\u4e00-\u9fa5]|\s|[\u3000-\u301e\ufe10-\ufe19\ufe30-\ufe44\ufe50-\ufe6b\uff01-\uffee])*"', data)
        datas = re.findall(r'(?<="rateContent":")[^A-Za-z]*",', data)
        print(datas)
        print(len(datas))

    else:
        print('网页下载 失败，请调整 参数')
    print('\n')
    print('第{}页评论数据爬取成功！----------------'.format(i))



def spuID():
    # 商品URL
    url = "https://detail.tmall.com/item.htm?spm=a230r.1.14.19.17746494iQ8m5K&id=620355053596&ns=1&abbucket=11"

    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
        'referer': "https://item.taobao.com/item.htm?spm=a230r.1.14.46.4b5d6494N4F7IF&id=540674962228&ns=1&abbucket=11",
        # detail_url
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
        'cookie': "tk_trace=1; cna=kpgeGFopnXwCAXWWvFYMOP+B; dnk=%5Cu6D77%5Cu7684%5Cu590F%5Cu65E5%5Cu54E6; tracknick=%5Cu6D77%5Cu7684%5Cu590F%5Cu65E5%5Cu54E6; lid=%E6%B5%B7%E7%9A%84%E5%A4%8F%E6%97%A5%E5%93%A6; lgc=%5Cu6D77%5Cu7684%5Cu590F%5Cu65E5%5Cu54E6; cookie2=149c11417406eff38ccf9b4198ddf2c3; t=ca1218ded111b679cb6c4b99bd75a3f2; hng=CN%7Czh-CN%7CCNY%7C156; enc=HCSX9KVT1HvH7RWFb%2FjTy8il6cDJVGGiZCkasIPrpohgtC9Auc6W5WDDVKNfwHvWodZvDEjh3EwX%2BmnEh78Gqw%3D%3D; _m_h5_tk=d937ebe654985ca179832bf002b7c3a0_1604121053312; _m_h5_tk_enc=7c01d5950498888208ebc214ce8b97a6; xlly_s=1; uc1=cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&pas=0&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie14=Uoe0abDIi1pcvQ%3D%3D&cookie21=V32FPkk%2FhodrpstKOCa5aA%3D%3D; uc3=nk2=2QNmkkQKTuv1eQ%3D%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D&id2=UUpidH%2F8V9rDDA%3D%3D&vt3=F8dCufJL9vxE4oIrjJE%3D; _l_g_=Ug%3D%3D; uc4=id4=0%40U2gosS8c%2FnmsJJVcqTw6h%2Ff95KnN&nk4=0%402%2BUl7E4E67VAwJxWyaOM94ivEHUK; unb=2236463935; cookie1=AHstaW48SYNRo%2B1A%2BCCPYNI2p0CWmKF7UpQAev6Ah7E%3D; login=true; cookie17=UUpidH%2F8V9rDDA%3D%3D; _nk_=%5Cu6D77%5Cu7684%5Cu590F%5Cu65E5%5Cu54E6; sgcookie=E100HrDUrRcKGmHhWxy2H%2BKsX3fWy5v2DuoKOUo1bZx%2BRlT99T3IcmLS8n3I9NjVSoXPhCt5ybgvrfehfK%2FeSiMUZA%3D%3D; sg=%E5%93%A659; csg=1a1a4bbd; _tb_token_=ea5d78f79b3fe; cq=ccp%3D0; pnm_cku822=098%23E1hv3vvUvbpvjQCkvvvvvjiWP2FUsjlnP2sy6jD2PmPUzjl8PFFOQjDnRsdWgjuevpvhvvmv99gCvvLMMQvvvvhvC9vhvvCvpv9CvhQUgs6vCAKxfwF9digDN%2BFwafktRm1H64mUkEp7EcqWAjc6%2BulAo57gAXZq%2BFECD4my%2Bb8rwyxlYExreByaWTeYifyZh7Eb%2BExrACeKuvhvmvvv9bd28Nu%2FkvhvC99vvOCgLf9Cvm9vvvmoS6vvnQvv94DvpCCnvvvHvhCvHUUvvvZvphvZm9vv9livpC2sRvhvCvvvvvv%3D; tfstk=csKVB_fiumn420IsJisal38IqduAZidMMu5PoFyYvLQ8A1QciXVOExYhUs5KqZf..; l=eBOumRgnOATEyTp9BOfZnurza77TsIRAguPzaNbMiOCPO-Cy5fHVWZWEvlT2CnGVh6VpR3RSn5QgBeYBqomRCSBNa6Fy_Ckmn; isg=BMPDOcenmLQzGFTGPWqiC1R-UodtOFd6KRq8NvWgFiKYtOPWfQupy4SmLkT6FK9y"
    }

    res = requests.get(url= url, headers=headers)
    print(res.status_code)
    print(res.text)
    res = res.text
    spu = re.findall(r'.spuId...[0-9]*', res)[0]
    spuID = re.findall(r'[0-9]*', spu)

    # s = str(res.headers)
    #
    # # spu = json.loads(str(res.headers))
    print(spuID[-2])

