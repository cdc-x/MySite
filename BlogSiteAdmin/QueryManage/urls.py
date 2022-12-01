from django.conf.urls import url
from .ArticleViews import *

urlpatterns = [
    url(r"^article/all$", QueryArticleListView.as_view()),
    url(r"^article/hot$", QueryHotArticleListView.as_view()),
    url(r"^article/tags$", QueryArticleTagsView.as_view()),
    url(r"^article/content$", QueryArticleContentView.as_view()),
    url(r"^article/count/thumb$", QueryArticleThumbView.as_view()),
    url(r"^article/count/browse$", QueryArticleBrowseView.as_view()),
    url(r"^article/thumb$", ArticleThumbView.as_view()),
    url(r"^article/check/thumb$", CheckArticleThumbView.as_view()),
]
