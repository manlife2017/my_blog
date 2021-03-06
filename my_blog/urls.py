"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from article.views import RSSFeed
from my_blog import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'article.views.man'),
    # url(r'^test/$', 'article.views.test'),
    url(r'^home/$', 'article.views.home', name='home'),
    # url(r'^static/(?P<Path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})
    url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
    # 拦截归档的
    url(r'^archives/$', 'article.views.archives', name='archives'),
    url(r'^about_me/$', 'article.views.about_me', name='about_me'),
    url(r'^tag(?P<tag>.+)/$', 'article.views.label', name='label'),
    url(r'^list_tag/$', 'article.views.tag_list', name='tag_list'),
    url(r'^search/$', 'article.views.blog_search', name='search'),
    url(r'^feed/$', RSSFeed(), name="RSS"),  #新添加的urlconf, 并将name设置为RSS, 方便在模板中使用url
]
