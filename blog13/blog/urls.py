"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf.urls import url,include   # 另加信息

def index(request:HttpRequest):
    """视图函数：请求进来返回响应"""
    # template:Template = loader.get_template('index.html')   # 加载器搜索模块 并加载；
    # print(type(template))
    context = {'school':'magedu'}   #正文字符串  数据传输
    # html = template.render(context)   # render拼接字符
    # print(html)
    # return HttpResponse(html.encode())
    return render(request, 'index.html', context, status=201)

urlpatterns = [                  # 必须写urlpatterns = [] 列表
    url(r'^admin/', admin.site.urls),   # 正则表达式模式匹配
    url(r'^$', index),   # 以它开头、结尾的；
    url(r'^index$', index),  # 以 index开头 index1、index/ ；
    # 两个不同的函数指向同一个问题url；不是多对多；
    #url(r'^user/reg$', reg)
    url(r'^user/', include('user.urls')),   #以user/开头的就去找 user.urls函数 做映射
    url(r'^post/', include('post.urls')),
]