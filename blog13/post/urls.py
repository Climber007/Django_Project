from django.conf.urls import url
from .views import get, getall, pub

urlpatterns = [
    url(r'^pub$', pub),
    url(r'^(\d+)$', get),
    url(r'^$', getall),
]