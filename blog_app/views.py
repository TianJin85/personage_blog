from django.http import HttpResponse
from django.shortcuts import render

import markdown
from django.views import View

from blog_app.libs.post_art import post_article
from utils import PageMode

from .models import Article
from .forms.Base import ArticleForm


class ListIndexView(View):
    template_name = 'blog_app/index.html'

    def get(self, request, *args, **kwargs):

        article = Article.objects.values('id', 'title', 'put_date', 'text_type')[::-1]  # 查询文章列表倒序排列
        # 查询最新排行榜
        sort_date = Article.objects.values("id", "title").order_by("put_date")[::-1][:6]
        # 查询点击量排行榜
        sort_click = Article.objects.values("id", "title").order_by("click_num")[::-1][:5]

        sort_date = [item for item in sort_date]
        value = [item for item in article]
        sort_click = [item for item in sort_click]
        values = PageMode.Page(request, value, 15)
        return render(request, self.template_name, {"values": values, "sort_date": sort_date, "sort_click": sort_click})

    def post(self, request, *args, **kwargs):
        data = "tianjin"
        print(self.request.POST['id'])
        return HttpResponse(content=data)


class ListAboutView(View):
    template_name = 'blog_app/about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ListCaselistView(View):
    template_name = 'blog_app/caselist'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ListKnowledgeView(View):
    template_name = 'blog_app/knowledge.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ListMoodlistView(View):
    template_name = 'blog_app/moodlist.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ListNewView(View):
    template_name = 'blog_app/new.html'

    def get(self, request, article_id):
        article = Article.objects.get(id=int(article_id))
        # 获取最大id数
        list_id = [item for items in Article.objects.values('id') for item in items.values()]

        # 查询最新排行榜
        sort_date = Article.objects.values("id", "title").order_by("put_date")[::-1][:6]
        sort_date = [item for item in sort_date]

        # 查询点击量排行榜
        sort_click = Article.objects.values("id", "title").order_by("click_num")[::-1][:5]
        sort_click = [item for item in sort_click]

        # 下一篇文章
        next_article = Article.objects.get(id=int(article_id - 1))
        next_article = {"id": next_article.id, "title": next_article.title}
        if max(list_id) > article_id:
            # 上一篇文章

            up_article = Article.objects.get(id=int(article_id + 1))
            up_article = {"id": up_article.id, "title": up_article.title}

        else:
            up_article = {"id": None, "title": None}

        article.text_content = markdown.markdown(article.text_content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'])
        lick_title = Article.objects.filter(title__contains=article.title).values()[:6]
        lick_title = [{'id': items['id'], 'title': items['title']}for items in lick_title]

        text_content = {'article': article, 'sort_date': sort_date, 'sort_click': sort_click,
                        'next_article': next_article, 'up_article': up_article, 'lick_title': lick_title
                        }

        return render(request, self.template_name, text_content)
    def post(self,request, *args, **kwargs):
        article_id = self.request.POST['article_id']
        article = Article.objects.get(id=int(article_id))
        article.click_num += 1
        article.save()
        return HttpResponse(content=article_id)

class ListShareView(View):
    template_name = 'blog_app/share.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'blog_app/share.html')


class ListTemplateView(View):
    template_name = 'blog_app/template.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'blog_app/template.html')


class ListMarkdownsView(View):
    template_name = 'markdown/index.html'
    template_index = 'blog_app/index.html'

    def get(self, request, *args, **kwargs):
        article = Article.objects.values('title_class')
        context ={it for item in list(article) for it in item.values() if it not in ''}
        context = [{'title_class': item}for item in context]
        contexts = {"contexts": context[:6]}

        return render(request, self.template_name,contexts)

    def post(self, request, *args, **kwargs):
        post_article(request, Article)
        return render(request, self.template_name)


class ListUpdateView(View):
    template_name = 'markdown/update.html'

    def get(self, request, *args, **kwargs):

        update_val = Article.objects.all()
        update_val = [item for item in update_val]
        update_val = PageMode.Page(request, update_val, 10)  # 分页

        return render(request, self.template_name, {"update_val": update_val})


class ListDeleteView(View):
    template_name = 'markdown/delete.html'

    def get(self, request, *args, **kwargs):

        # return render(request, self.template_name)
        return HttpResponse(stats=400)

    def post(self, request, *args, **kwargs):

        return HttpResponse(200)


class ListNewlistView(View):
    template_name = 'blog_app/newlist.html'

    def get(self, request, *args, **kwargs):
        # 查询最新排行榜
        sort_date = Article.objects.values("id", "title").order_by("put_date")[::-1][:6]

        # 查询点击量排行榜
        sort_click = Article.objects.values("id", "title").order_by("click_num")[::-1][:5]
        sort_date = [item for item in sort_date]
        sort_click = [item for item in sort_click]
        text_content = {"sort_date": sort_date, "sort_click": sort_click}

        return render(request, self.template_name, text_content)


class ListAmendView(View):
    template_name = 'markdown/upindex.html'

    def get(self, request, *args, **kwargs):

        article = Article.objects.get(id=int(request.GET['id']))
        context = {"article": article}

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        article = Article.objects.get(id=int(request.POST['id']))
        print(article)

        return HttpResponse(article.text_content)






