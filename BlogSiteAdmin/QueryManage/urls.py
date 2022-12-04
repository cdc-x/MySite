from django.conf.urls import url
from .DashboardView import QueryDashboardDataView
from .ArchiveView import ArticleArchiveView
from .ArticleViews import *

urlpatterns = [
    # ��ѯ�������ͳ������
    url(r"^about_site$", QueryDashboardDataView.as_view()),
    # ���¹鵵��Ϣ
    url(r"^archive$", ArticleArchiveView.as_view()),
    # ��ѯ�����б�
    url(r"^article/all$", QueryArticleListView.as_view()),
    # ��ѯ������������
    url(r"^article/hot$", QueryHotArticleListView.as_view()),
    # ��ѯTag����
    url(r"^article/tags$", QueryArticleTagsView.as_view()),

    # url(r"^article/all$", QueryArticleListView.as_view()),
    # url(r"^article/hot$", QueryHotArticleListView.as_view()),
    # url(r"^article/tags$", QueryArticleTagsView.as_view()),
    # url(r"^article/content$", QueryArticleContentView.as_view()),
    # url(r"^article/count/thumb$", QueryArticleThumbView.as_view()),
    # url(r"^article/count/browse$", QueryArticleBrowseView.as_view()),
    # url(r"^article/thumb$", ArticleThumbView.as_view()),
    # url(r"^article/check/thumb$", CheckArticleThumbView.as_view()),
]
