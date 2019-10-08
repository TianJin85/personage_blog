from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListIndexView.as_view(), name='index'),
    path('about', views.ListAboutView.as_view(), name='about'),
    path('caselist', views.ListCaselistView.as_view(), name='caselist'),
    path('knowledge', views.ListKnowledgeView.as_view(), name='knowledge'),
    path('moodlist', views.ListMarkdownsView.as_view(), name='moodlist'),
    path('<int:article_id>/new', views.ListNewView.as_view(), name='new'),
    path('share', views.ListShareView.as_view(), name='share'),
    path('template', views.ListTemplateView.as_view(), name='template'),
    path('markdowns', views.ListMarkdownsView.as_view(), name='markdowns'),
    path('update', views.ListUpdateView.as_view(), name='update'),
    path('delete', views.ListDeleteView.as_view(), name='delete'),
    path('newlist', views.ListNewlistView.as_view(), name='newlist'),
    path('amend', views.ListAmendView.as_view(), name='amend')
]
