import logging
import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from CategoryManage.models import Category

logger = logging.getLogger("log")


class DashboardView(APIView):
    @staticmethod
    def get(request):
        pass
