from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('caselist', views.caselist, name='caselist'),
    path('knowledge', views.knowledge, name='knowledge'),
    path('moodlist', views.moodlist, name='moodlist'),
    path('<int:article_id>/new', views.new, name='new'),
    path('share', views.share, name='share'),
    path('template', views.template, name='template'),
    path('markdowns', views.markdowns, name='markdowns'),
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete'),
    path('newlist', views.newlist, name='newlist'),
    path('amend', views.amend, name='amend')
]
