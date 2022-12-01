import datetime
from django.utils.deprecation import MiddlewareMixin
from CommonManage.models import Browse
from ArticleManage.models import Article


class SiteBrowseMiddleware(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        visit_path = request.path

        if not visit_path.__contains__("admin"):
            if request.META.get('HTTP_X_FORWARDED_FOR'):
                ip = request.META.get("HTTP_X_FORWARDED_FOR")
            else:
                ip = request.META.get("REMOTE_ADDR")

            if ip:
                Browse.objects.create(
                    host=ip,
                    browse_time=datetime.datetime.now().replace(microsecond=0)
                )


class ArticleBrowseMiddleware(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        # 获取访问的文章的ID
        aid = request.GET.get("p", "")

        # 获取用户IP
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = request.META.get("HTTP_X_FORWARDED_FOR")
        else:
            ip = request.META.get("REMOTE_ADDR")

        if aid and ip:
            # 文章访问量+1
            article_obj = Article.objects.filter(id=aid).first()
            article_obj.browse += 1
            article_obj.save()
