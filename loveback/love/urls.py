from love import views
#这里必须从love里面导入views
from django.conf.urls import url

# 这里写的是方法路径

urlpatterns = [
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),


]



