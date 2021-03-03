
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest,HttpResponseBadRequest
from user.models import User
from user.views import auth
from post.models import Post, Content
import simplejson, datetime, math

# Create your views here.
def get(request:HttpRequest, id):  # 不是所有的request都是两个参数； id - str
    print(id,type(id))
    try:
        post = Post.objects.get(pk=int(id))

        return JsonResponse({
            'post':{
                'post_id': post.id,
                'auther_id': post.auther_id,
                'title': post.title,
                'postdate': int(post.postdate.timestamp()),
                'auther': post.auther.name,
                'content': post.content.content,
            }
        })
    except Exception as e:
        return HttpResponseNotFound()

@auth
def pub(request:HttpRequest):
    try:
        payload = simplejson.loads(request.body)

        title = payload['title']
        c = payload['content']

        post = Post()
        post.title = title
        post.postdate = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
        post.auther = User(pk=request.user.id)# request.user    # User(request.user.id) # User(pk=request.user.id)

        post.save()

        content = Content()
        content.post = post
        content.content = c

        content.save()
        return JsonResponse({
            'post_id': post.id
        })
    except Exception as e:
        print(e)
        return  HttpResponseBadRequest()


def validate(d:dict,name:str,convert_func,default,valida_func):   #抽象化处理；
    try:
        x = convert_func(d.get(name))
        ret = validate_func(x,default)
        # ret = x if x>0 else default # lambda x,y:x if x>0 else y
    except:
        ret = default
    return ret

# http://127.0.0.1:8000/post?page=1&size=2
def getall(request:HttpRequest):  # 文章列表 不显示内容；

    page = validate(request.GET,'page',int,1,lambda x,y:x if x>0 else y)

    # get_size
    size = validate(request.GET,'size',int,2,lambda x,y: x if x>0 and x<101 else y)

    # pagination
    start = (page-1)*size
    posts = Post.objects.order_by('-pk')
    count = posts.count()
    posts = posts[start:start+size]
    pages = math.ceil(count/size) # 向上取整数

    if posts:
        return JsonResponse({
            'posts':[{
                    'post_id': post.id,
                    'title': post.title,
                } for post in posts
            ],'pagination':{
                'page':page,
                'size':size,
                'count':count,
                'pages':pages
            }
        })
    else:
        return HttpResponseNotFound()