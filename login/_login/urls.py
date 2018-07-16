from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^_login/signup/$',views.signup),
    url(r'^_login/signup_hander/$',views.signup_hander),
    url(r'^_login/login/$',views.login),
    url(r'^_login/login_hander/$',views.login_hander),
    # url(r'^_login/signup_hander2/$',views.signup_hander2)
]