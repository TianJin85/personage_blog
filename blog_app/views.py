from django.http import HttpResponse
from django.shortcuts import render

import markdown

from utils import PageMode

from .models import Article


def index(request):

    article = Article.objects.values('id', 'title', 'put_date', 'text_type')[::-1]  # 查询文章列表倒序排列
    # 查询最新排行榜
    sort_date = Article.objects.values("id", "title").order_by("put_date")[::-1][:6]
    # 查询点击量排行榜
    sort_click = Article.objects.values("id", "title").order_by("click_num")[::-1][:5]

    sort_date = [item for item in sort_date]
    value = [item for item in article]
    sort_click = [item for item in sort_click]
    values = PageMode.Page(request, value, 15)

    return render(request, 'blog_app/index.html',{"values": values, "sort_date": sort_date, "sort_click": sort_click})

def about(request):

    return render(request, 'blog_app/about.html')


def caselist(request):

    return render(request, 'blog_app/caselist')


def knowledge(request):

    return render(request, 'blog_app/knowledge.html')


def moodlist(request):

    return render(request, 'blog_app/moodlist.html')


def new(request, article_id):
    article = Article.objects.get(id=int(article_id))
    article.click_num += 1
    article.save()
    # 查询最新排行榜
    sort_date = Article.objects.values("id", "title").order_by("put_date")[::-1][:6]
    sort_date = [item for item in sort_date]

    # 查询点击量排行榜
    sort_click = Article.objects.values("id", "title").order_by("click_num")[::-1][:5]
    sort_click = [item for item in sort_click]

    # 上一篇文章

    up_article = Article.objects.get(id=int(article_id+1))
    up_article = {"id": up_article.id, "title": up_article.title}

    # 下一篇文章

    next_article = Article.objects.get(id=int(article_id-1))
    next_article = {"id": next_article.id, "title": next_article.title}

    article.text_content = markdown.markdown(article.text_content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'])

    text_content = {'article' : article, "sort_date": sort_date, "sort_click": sort_click,
                    'next_article': next_article, 'up_article': up_article
                    }

    return render(request, 'blog_app/new.html', text_content)


def share(request):

	return render(request, 'blog_app/share.html')


def template(request):

    return render(request, 'blog_app/template.html')

def markdowns(request):

    if request.method == 'POST': # 判断提交方式
        # 获取提交的数据
        title = request.POST['title']
        label = request.POST['label']
        put_date = request.POST['put_date'].replace(".", "-")
        title_class = request.POST['title_class']
        text_type = request.POST['text_type']
        blog_type = request.POST['blog_type']
        text_content = request.POST['content']
        text_types = {"0": "null","original" : "原创", "repost" : "转载", "translated" : "翻译"}
        blog_types = {"0": "选择分类","28": "人工智能","1": "移动开发","29": "物联网","15": "架构","2": "云计算",
                      "17": "互联网","30": "游戏开发","12": "运维","6": "数据库","14": "前端",
                      "31": "后端","16": "编程语言","3": "研发管理","32": "安全","33" : "程序人生","34": "区块链",
                      "35": "音视频开发","36": "资讯","37" : "计算机理论与基础"}
        text_type = text_types[text_type]
        blog_type = blog_types[blog_type]

        At = Article(title=title, label=label, put_date=put_date,title_class=title_class, text_type=text_type,
                     blog_type=blog_type, text_content=text_content)
        At.save()

    return render(request, 'markdown/index.html')

def update(request):
    update_val = Article.objects.all()
    update_val = [item for item in update_val]
    update_val = PageMode.Page(request, update_val, 10)  # 分页

    return render(request, 'markdown/update.html', {"update_val": update_val})

def delete(request):

    return render(request, 'markdown/delete.html')

def newlist(request):
    # 查询最新排行榜
    sort_date = Article.objects.values("id", "title").order_by("put_date")[::-1][:6]
    # 查询点击量排行榜
    sort_click = Article.objects.values("id", "title").order_by("click_num")[::-1][:5]
    sort_date = [item for item in sort_date]
    sort_click = [item for item in sort_click]
    text_content = {"sort_date": sort_date, "sort_click": sort_click}

    return render(request, 'blog_app/newlist.html', text_content)
def amend(request):
    return render(request, 'markdown/amend.html')



