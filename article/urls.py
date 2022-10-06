from django.urls import path
from . import views


app_name = 'article'

urlpatterns = [
     path('add-article', views.artikelAddView, name="addArticle"),
     path('add-article2', views.artikelAddView2, name="addArticle2"),
     path('article-reinaldo', views.reinaldoview, name="article_reinaldo"),
     path('', views.artikelIndexView, name="index"),
]
