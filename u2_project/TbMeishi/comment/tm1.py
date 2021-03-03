
import requests

url = "https://rate.tmall.com/list_detail_rate.htm?"

querystring = {"itemId":"596581206111","spuId":"1915053039","sellerId":"2200863423968","order":"3","currentPage":"1","append":"0","content":"1"}

payload = ""
headers = {
    'accept-language': "zh-CN,zh;q=0.9",
    'cookie': "tk_trace=1; cna=8n6QGK4lvlICAXWWvAjQgrYX; t=cbd57b25289c33451aa3acf8d7e61a06; _tb_token_=eb87d383e1647; cookie2=2a4ac6e524ecb1fac8839b017a02ea46; dnk=%5Cu6D77%5Cu7684%5Cu590F%5Cu65E5%5Cu54E6; uc1=cookie14=Uoe1g8so%2Bmb0oA%3D%3D&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&pas=0&cookie15=VT5L2FSpMGV7TQ%3D%3D&existShop=false&cookie21=URm48syIZJfmYzXrEixrAg%3D%3D; uc3=lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dCuAFVoeshJPUIAV4%3D&id2=UUpidH%2F8V9rDDA%3D%3D&nk2=2QNmkkQKTuv1eQ%3D%3D; tracknick=%5Cu6D77%5Cu7684%5Cu590F%5Cu65E5%5Cu54E6; lid=%E6%B5%B7%E7%9A%84%E5%A4%8F%E6%97%A5%E5%93%A6; uc4=nk4=0%402%2BUl7E4E67VAwJxWyaKugu8BGIXg&id4=0%40U2gosS8c%2FnmsJJVcqT2RlY%2F3YLoE; lgc=%5Cu6D77%5Cu7684%5Cu590F%5Cu65E5%5Cu54E6; sgcookie=E100eBlElStkkd6tcEQdbN%2Blck5widhjC6miK%2B%2BVt2jFpNNiNyyB%2F0dbaDntyKQEtIyjJf5mP%2BllvxIVlxJV3xuLlw%3D%3D; csg=03f1ecec; enc=sO8vSOSDq0u%2BEoz4r7AujbxU6hvOnRzg6Sdw02oVLEnV6T1eeT5xRrQmpqWjfjFFk%2BIJPMjL6IGUyntXHdPlMg%3D%3D; xlly_s=1; tfstk=c-_VB39g0rUVQV8_vETZhyKflgZAZHXGH4JymGehqJh4jExcieD9ZSjHaKJLrnf..; l=eBgFIyvPjjY-19mUBO5Cnurza779uIdb8sPzaNbMiInca6BhZeGd-NCIW8zJodtjgtfvpeKz4rz6LRnw-f4_Wr_ceTwhKXIpBxv9-; isg=BKWlnh4mKZx9v03xh8ERj1wKtGHf4ll0uIJrdaeL9VzMvsQwbjM8Rl6YSCLIvnEs",
    'referer': "https://detail.tmall.com/item.htm?id=596581206111&ali_refid=a3_430583_1006:1214580125:N:Z3n/4zOj22Oo%20vA/6f3FTQ==:743abf6e93404b8570a15aa390883b91&ali_trackid=1_743abf6e93404b8570a15aa390883b91&spm=a230r.1.14.3",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)

# 美食页面
t=75009ff2c6ca2c5bcb280b349303f4fc;         # t=cbd57b25289c33451aa3acf8d7e61a06;
cna=G3EmGGC0CG0CAXWWvFbpCVae;  # 2          # cna=8n6QGK4lvlICAXWWvAjQgrYX;
xlly_s=1;
sgcookie=E100XSUs4EIl1fIdjCmMsqEHrCt0FdFA1x1cvFBi003Zw%2BM8fEEa2cmXy93Y9gLjp02jeJtDrX8d%2BAydu135a6dvsQ%3D%3D;
uc3=id2=UUpidH%2F8V9rDDA%3D%3D&lg2=URm48syIIVrSKA%3D%3D&nk2=2QNmkkQKTuv1eQ%3D%3D&vt3=F8dCuASu83tMu2bm2J0%3D;
lgc=%5Cu6D77%5Cu7684%5Cu590F%5Cu65E5%5Cu54E6;
uc4=nk4=0%402%2BUl7E4E67VAwJxWyaKr49iAzgU2&id4=0%40U2gosS8c%2FnmsJJVcqT2UmJGq3fhS;
tracknick=%5Cu6D77%5Cu7684%5Cu590F%5Cu65E5%5Cu54E6;
_cc_=WqG3DMC9EA%3D%3D;
mt=ci=114_1;
thw=cn;
enc=gePD2CitB%2FfzYgm%2FIwffL2sh9uSUc6PnC9lscbFJM5LgP%2Fc%2ByfCJry4%2F%2B2cXPjRCVvJHTL4Te8Whex9%2BubmDAA%3D%3D;
hng=CN%7Czh-CN%7CCNY%7C156;
_m_h5_tk=fe0c76df21f5f2c596a3bfaffd99be48_1614345065811;
_m_h5_tk_enc=6d8fb39a4ddf6818e43d7fd3f08a1cf0; cookie2=1fb11d73efed0bb8defea6294ed310d6;
uc1=cookie14=Uoe1hgVrP7XzIA%3D%3D;
_tb_token_=733e3ee886e37;   # _tb_token_=eb87d383e1647;
alitrackid=www.taobao.com;
lastalitrackid=www.taobao.com;
JSESSIONID=E77C75EDC343A62124CE972182065B00;
l=eBaXKupHO2CWOwx2BOfwourza77OSIRAguPzaNbMiOCPOk5p5zwAW6g9Yw89C3Gch62yR3beztBJBeYBqS24n5U62j-la_kmn;
tfstk=cooVBbNMunK29mE6JoZNGedCqmrAZMliMgPzoVdQgvLAC-4cigfTFaa7USkNjrf..;  # c-_VB39g0rUVQV8_vETZhyKflgZAZHXGH4JymGehqJh4jExcieD9ZSjHaKJLrnf..
isg=BFZW_F8_KhnKmCEaczcFEUA4pwxY95oxL3OxFsC_QjnUg_YdKIfqQbzxHx5vK5JJ # BKWlnh4mKZx9v03xh8ERj1wKtGHf4ll0uIJrdaeL9VzMvsQwbjM8Rl6YSCLIvnEs



#

