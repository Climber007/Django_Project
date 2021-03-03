from django.shortcuts import render
from django.http import JsonResponse, HttpRequest,HttpResponseBadRequest
from user.models import User
from user.views import auth
from post.models import Post, Content
import simplejson, datetime

def get(request: HttpRequest):
    return JsonResponse()

@auth
def pub(request:HttpRequest):
    try:
        payload = simplejson.loads(request.body)

        title = payload['title']
        c = payload['content']

        post = Post()
        post.title = title
        post.postdate = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
        post.author = request.user

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

def getall(request: HttpRequest):
    return JsonResponse()
