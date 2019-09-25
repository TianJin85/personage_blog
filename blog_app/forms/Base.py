from django import forms


class ArticleForm(forms.Form):

    title = forms.CharField()
    label = forms.CharField()
    title_class = forms.CharField()
    text_type = forms.CharField()
    blog_type = forms.CharField()
    text_content = forms.CharField()
    click_num = forms.IntegerField()


class CommentForm(forms.Form):

    Ip = forms.CharField()
    cet_conte = forms.CharField()
    cet_date = forms.CharField()

