# -*- encoding: utf-8 -*-
"""
@File    : post_art.py
@Time    : 2019/10/20 22:27
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from blog_app.forms.Base import ArticleForm


def post_article(request, Article):
    if ArticleForm(request.POST).is_valid():  # 表单验证

        # 获取提交的数pa据
        title = request.POST['title']
        label = request.POST['label']
        put_date = request.POST['put_date'].replace(".", "-")
        title_class = request.POST['title_class']
        text_type = request.POST['text_type']
        blog_type = request.POST['blog_type']
        text_content = request.POST['text_content']
        text_types = {"0": "null", "original": "原创", "repost": "转载", "translated": "翻译"}
        blog_types = {"0": "选择分类", "28": "人工智能", "1": "移动开发", "29": "物联网", "15": "架构", "2": "云计算",
                      "17": "互联网", "30": "游戏开发", "12": "运维", "6": "数据库", "14": "前端",
                      "31": "后端", "16": "编程语言", "3": "研发管理", "32": "安全", "33": "程序人生", "34": "区块链",
                      "35": "音视频开发", "36": "资讯", "37": "计算机理论与基础"}
        text_type = text_types[text_type]
        blog_type = blog_types[blog_type]

        At = Article(title=title, label=label, put_date=put_date, title_class=title_class, text_type=text_type,
                     blog_type=blog_type, text_content=text_content)
        At.save()
