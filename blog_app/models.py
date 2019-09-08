from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=20)  # 标题
    label = models.CharField(max_length=20)  # 标签
    put_date = models.DateTimeField('date published')  # 提交时间
    title_class = models.CharField(max_length=20)  # 文章分类
    text_type = models.CharField(max_length=20)  # 文章类型
    blog_type = models.CharField(max_length=20)  # 博客类型
    text_content = models.CharField(max_length=10000)  # 文章内容
    click_num = models.IntegerField(default=0)  # 文章阅读量


class Comment(models.Model):

    Ip = models.CharField(max_length=20)  # 评论IP地址
    cet_content = models.CharField(max_length=10000)  # 评论文章
    cet_date = models.DateTimeField('date published')  # 评论时间