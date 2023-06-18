from django.conf.urls import url, include

urlpatterns = [
    url('^admin/', include("UserManage.urls")),
    url('^admin/', include("CategoryManage.urls")),
    url('^admin/', include("TagManage.urls")),
    url('^admin/', include("ArticleManage.urls")),
    url('^admin/', include("CommonManage.urls")),
    url('^q/', include("QueryManage.urls")),
]
