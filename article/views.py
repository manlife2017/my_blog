from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
# 导入model 模块对象进行数据操作
from article.models import Article
from datetime import datetime
from django.contrib.syndication.views import Feed
# Create your views here.


def man(request):
    return HttpResponse('<h1>fdsfdsf</h1>')


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})


def home(request):
    res = Article.objects.all()
    return render(request, 'home.html', {'post_list': res})


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Exception as e:
        raise Http404
    return render(request, 'post.html', {'post': post})


def archives(request):
    try:
        post_list = Article.objects.all()
    except Exception as e:
        raise Http404
    return render(request, 'archives.html', {'post_list': post_list, 'error': False})


def about_me(request):
    return render(request, 'about_me.html')


def label(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact=tag)
    except Exception as e:
        raise Http404
    return render(request, 'home.html', {'post_list': post_list})


def tag_list(request):
    try:
        post_list = Article.objects.all()
        if post_list:
            pass
        else:
            raise Http404
    except Exception as e:
        raise Http404
    return render(request, 'tag_list.html', {'post_list': post_list})


def blog_search(request):
    if 's' in request.GET:
        data = request.GET['s']
        post_list = Article.objects.filter(title__icontains=data)
        if len(post_list) == 0:
            return render(request, 'archives.html', {'post_list': post_list, 'error': True})
        else:
            return render(request, 'archives.html', {'post_list': post_list, 'error': False})


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    # def item_pubdate(self, item):
    #      return item.add_date

    def item_description(self, item):
        return item.content



