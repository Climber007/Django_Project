import requests,re,csv,simplejson
from bs4 import BeautifulSoup

Page_url = []

def get_url(num):
    urlfirst = 'https://rate.tmall.com/list_detail_rate.htm?itemId=552918017887&spuId=856416229&sellerId=2455250363&order=3&currentPage='
    urllast = '&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvE9v8vWyvjQCkvvvvvjiWP2MygjrPPsdOzjljPmP96jlEPsFwtjlHPFFv1j0%2BvpvEvv2gMivvvUh%2Fi9hvCvvvpZpgvpvhvvCvpvgCvvLMMQvvuvhvmvvvpLLBS3bkkvhvC9hvpyP9lb9Cvm9vvh2CvvmCC9vvpqQvvvbAvvC8o9vv9Dvvvhi8vvmmppvvBAgvvU8KmvhvLvhytRpaQE97RqwiLO2v5fVQKoZH1nvaRfUTnZJt9b8rV8tYVVzhd3w0%2BktE64h7%2Bu0fjomxfBeKydUf8z7Q%2Bu6Xd56OfwoKHqh6UxWvvpvVvUCvpvvv39hvCvmvphv%3D&needFold=0&_ksTS=1603980442141_424&callback=jsonp425'
    for i in range(0, num):
        Page_url.append(urlfirst+str(1+i)+urllast)
    print(Page_url)


def get_comment(num):
    headers = {
        'accept': '*/*',
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
        'cookie': "tk_trace=1; cna=kpgeGFopnXwCAXWWvFYMOP+B; dnk=%5Cu6D77%5Cu7684%5Cu590F%5Cu65E5%5Cu54E6; uc3=lg2=W5iHLLyFOGW7aA%3D%3D&nk2=2QNmkkQKTuv1eQ%3D%3D&vt3=F8dCufJHDhibOu0q62Q%3D&id2=UUpidH%2F8V9rDDA%3D%3D; tracknick=%5Cu6D77%5Cu7684%5Cu590F%5Cu65E5%5Cu54E6; lid=%E6%B5%B7%E7%9A%84%E5%A4%8F%E6%97%A5%E5%93%A6; uc4=id4=0%40U2gosS8c%2FnmsJJVcqTw9O%2B%2Bca2Rv&nk4=0%402%2BUl7E4E67VAwJxWyaOLAGvq1I51; lgc=%5Cu6D77%5Cu7684%5Cu590F%5Cu65E5%5Cu54E6; cookie2=149c11417406eff38ccf9b4198ddf2c3; sgcookie=E100yDsS0UM8xMCZ3s1LXFF3X8eveTdZtSahC%2Ftkwg6cXblt%2BXirk4MBb9QME4ogR7ihjkhrPYXO71ko4m5Djpg9FQ%3D%3D; t=ca1218ded111b679cb6c4b99bd75a3f2; csg=22330db3; _tb_token_=35be5905153ee; hng=CN%7Czh-CN%7CCNY%7C156; uc1=pas=0&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&cookie21=UIHiLt3xSixwG45%2Bs3wzsA%3D%3D&existShop=false&cookie14=Uoe0bkFA5yTF0A%3D%3D; enc=HCSX9KVT1HvH7RWFb%2FjTy8il6cDJVGGiZCkasIPrpohgtC9Auc6W5WDDVKNfwHvWodZvDEjh3EwX%2BmnEh78Gqw%3D%3D; xlly_s=1; _m_h5_tk=d9035fd8753e33dee00d620e2670fd12_1603982842408; _m_h5_tk_enc=d0d8e2bfb9405f249ccfc10e2dcf6820; l=eBOumRgnOATEyYOwBOfZnurza779KIRAguPzaNbMiOCPOgfH5FvOWZWaUYYMCnGVh62wR3RSn5QgBeYBqSx0x6aNa6Fy_Ckmn; tfstk=cmIdBdNKW5VHmsvO3wUiVLN6MD2cZEwp_v9K2-9Lod_qYniRimscDZjYRBlpXRC..; isg=BBERSEulKrpTOEasu-zQUbrQIB2rfoXwlyQOnPOmT1j3mjHsO86RwqF8PG58kh0o",
        'referer': "https://detail.tmall.com/item.htm?spm=a230r.1.14.1.55a84b1721XG00&id=552918017887&ns=1&abbucket=17",
        'sec-fetch-dest': "script",
        'sec-fetch-mode': "no-cors",
        'sec-fetch-site': "same-site",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        }
    for i in range(num):
        res = requests.get(Page_url[i], headers=headers)
        print(res.status_code)
        print(res.content)  # 加密字体woff文件；
get_url(5)
get_comment(1)








url = 'https://detail.tmall.com/item.htm?spm=a230r.1.14.1.55a84b1721XG00&id=552918017887&ns=1&abbucket=17'