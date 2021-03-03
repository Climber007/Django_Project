from django.http import JsonResponse,HttpRequest,HttpResponseBadRequest
import simplejson,jwt,bcrypt
from .models import User
from django.db.models import Q
from django.conf import settings


def gen_token(user_id):  # 生成令牌；
    key = settings.SECRET_KEY
    return jwt.encode({'user_id': user_id}, key, 'HS256')

# register
def reg(request:HttpRequest):
    print(request.body)

    try:
        payload = simplejson.loads(request.body)  # 用户数据Json化 提交；
        print(type(settings))

        email = payload['email']      # 提取内容
        query = User.objects.filter(email=email)   # 看email是否已经存在；
        if query.first():  # 查一下： email 如果存在，则return error;
            print('============================')
            return HttpResponseBadRequest('用户名已存在')

        # 用户名不存在，继续向下；
        name = payload['name']   #
        password = payload['password']

        user = User()
        user.email = email
        user.name = name
        user.password = bcrypt.hashpw(password.encode(),bcrypt.gensalt())   # 密码采用bcrypt加密；

        try:
            user.save()    #保存到数据库test,唯一键约束
            return JsonResponse({
                'user_id':user.id
            })   # 保存数据后返回一个令牌数据回去；
        # 可以返回user_id status=201（注册成功 重新登录） 或者 token（登录）

        except Exception as e:
            return JsonResponse({'reason':'asdaf'},status=400)
    except Exception as e:
        print(e)
        return HttpResponseBadRequest('参数错误')


def login(request:HttpRequest):
    try:
        payload = simplejson.loads(request.body)
        email = payload['email']
        password = payload['password']

        user = User.objects.filter(email=email).first()
        if user:
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                token = gen_token(user.id)
                res = JsonResponse({
                    'user':{
                        'user_id': user.id,
                        'name': user.name,
                        'email': user.email
                    }, 'token': token
                })

                res.set_cookie('jwt',token)  # 演示 如何 set_cookie

                return res
            else:
                return HttpResponseBadRequest('登录失败3')
        else:
            return HttpResponseBadRequest('登录失败1')


    except Exception as e:   # 记录登录日志；
        print(e)
        return HttpResponseBadRequest('登录失败2')

def auth(view_func):
    def wrapper(request:HttpRequest):
        token = request.META.get('HTTP_JWT', None)  # 拿到http_jwt 字典的值
        # print(list(filter(lambda x: x.lower().endswith('jwt'),meta)))  #查询 http_jwt
        print(token)
        key = settings.SECRET_KEY
        try:
            print('=============================')
            payload = jwt.decode(token, key, algorithms=['HS256'])  # 解失败，被改过；接成功；没改过；
            print(payload)
            user = User.objects.filter(pk=payload['user_id']).first()   # 查询一次数据库；
            # user = User.objects.filter(pk=payload['user_id']).filter(isactive=True).first()

            if user: # 拿到user,
                request.user = user  #request 动态添加属性；
                ret = view_func(request)

                return ret
            else:
                return HttpResponseBadRequest('1用户名密码错误')
        except Exception as e:
            print(e)
            return HttpResponseBadRequest('2用户名密码错误')

    return wrapper

@auth        # 认证拦截
def show(request):          # 方法的使用方式各不相同；
    print(request.user, '---------------------------')
    return JsonResponse({'status': 'ok'})

# class AuthMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.
#
#     def __call__(self, request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
#         print(request, '++++++++++++++++++++++++++')
#         token = request.META.get('HTTP_JWT', None)
#         print(token)
#         # 统计IP验证 : 1分钟1000次以上；  使用字典记录次数 =》 redis kv; 调shell - 防火墙；
#
#         response = self.get_response(request)
#
#         # Code to be executed for each request/response after
#         # the view is called.
#
#         return response