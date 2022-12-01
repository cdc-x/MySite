from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^article/map", DashboardView.as_view()),
]
