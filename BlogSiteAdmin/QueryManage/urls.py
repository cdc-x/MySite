from django.conf.urls import url
from .DashboardView import QueryDashboardDataView
from .ArchiveView import ArticleArchiveView
from .ArticleViews import *

urlpatterns = [
    # 查询文章相关统计数据
    url(r"^about_site$", QueryDashboardDataView.as_view()),
    # 文章归档信息
    url(r"^archive$", ArticleArchiveView.as_view()),
    # 查询文章列表
    url(r"^article/all$", QueryArticleListView.as_view()),
    # 查询热门文章数据
    url(r"^article/hot$", QueryHotArticleListView.as_view()),
    # 查询Tag分类
    url(r"^article/tags$", QueryArticleTagsView.as_view()),
    # 查询文章内容
    url(r"^article/content$", QueryArticleContentView.as_view()),
    # 获取文章点赞数
    url(r"^article/count/thumb$", QueryArticleThumbView.as_view()),
    # 获取文章阅读量
    url(r"^article/count/browse$", QueryArticleBrowseView.as_view()),
    # 检查当前用户是否对文章点赞
    url(r"^article/check/thumb$", CheckArticleThumbView.as_view()),
    # 文章点赞
    url(r"^article/thumb$", ArticleThumbView.as_view()),
]
