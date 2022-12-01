import datetime
import logging
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import EmptyPage, Paginator
from ArticleManage.models import *
from TagManage.models import Tag

logger = logging.getLogger("log")


class QueryArticleListView(APIView):
    authentication_classes = []

    @staticmethod
    def get(request):
        try:
            search_content = request.GET.get("searchContent", "")
            search_tag = request.GET.get("searchTag", "")
            page = request.GET.get("page", 1)

            sql = f"""
                SELECT DISTINCT 
                    a.*,
                    d.category as category_name
                FROM
                    article a 
                    LEFT JOIN article_tag b ON b.article_id=a.aid
                    LEFT JOIN tag c ON b.tag_id=c.tid
                    LEFT JOIN category d ON a.category_id=d.cid
            """

            if search_content:
                sql += f" WHERE a.title like '%%{search_content}%%'"

            if search_tag:
                sql += f" WHERE c.tag='{search_tag}'"

            sql += " ORDER BY a.publish_time desc, a.title desc"

            query = Article.objects.raw(sql)
            paginator = Paginator(query, 8)

            try:
                page_content = paginator.page(page)
            except EmptyPage as e:
                logger.error(str(e))
                page_content = []

            data_list = list()
            for obj in page_content:
                data_list.append({
                    "id": obj.aid,
                    "title": obj.title,
                    "desc": obj.article_desc,
                    "publish_time": obj.publish_time.strftime("%Y-%m-%d") if obj.publish_time else "",
                    "thumb": obj.thumb,
                    "browse": obj.browse,
                    "category": obj.category_name,
                })

            # 查询时间标记
            date_mark = list()
            date_query = Article.objects.all().values("publish_time").distinct()
            for item in date_query:
                if item["publish_time"]:
                    date_mark.append(item["publish_time"].strftime("%Y/%m/%d"))

            ret_data = {"status_code": 1000, "data": data_list, "total": len(query), "date_mark": date_mark,
                        "page": page}
        except Exception as e:
            logger.error(str(e))
            ret_data = {"status_code": 1001, "message": str(e)}

        return Response(ret_data)


class QueryHotArticleListView(APIView):
    authentication_classes = []

    @staticmethod
    def get(request):
        try:
            sql = f"""
                SELECT
                    a.*,
                    b.category as category_name
                FROM
                    article a 
                    LEFT JOIN category b ON a.category_id=b.cid
                ORDER BY browse desc 
            """

            query = Article.objects.raw(sql)

            data_list = list()
            for obj in list(query)[0:8]:
                data_list.append({
                    "id": obj.aid,
                    "title": obj.title,
                    "desc": obj.article_desc,
                    "publish_time": obj.publish_time.strftime("%Y-%m-%d") if obj.publish_time else "",
                    "thumb": obj.thumb,
                    "browse": obj.browse,
                    "category": obj.category_name,
                })

            ret_data = {"status_code": 1000, "data": data_list}
        except Exception as e:
            logger.error(str(e))
            ret_data = {"status_code": 1001, "message": str(e)}

        return Response(ret_data)


class QueryArticleTagsView(APIView):
    authentication_classes = []

    @staticmethod
    def get(request):
        try:
            sql = f"""
                SELECT
                    a.*,
                    c.tag as tag_name
                FROM
                    article a 
                    LEFT JOIN article_tag b ON a.aid=b.article_id
                    LEFT JOIN tag c ON c.tid=b.tag_id
            """

            query = Article.objects.raw(sql)
            tag_query = Tag.objects.all()

            tag_count = dict()
            for obj in tag_query:
                tag_count[obj.tag] = 0

            for obj in query:
                tag_count[obj.tag_name] += 1

            ret_data = {"status_code": 1000, "data": tag_count}
        except Exception as e:
            logger.error(str(e))
            ret_data = {"status_code": 1001, "message": str(e)}

        return Response(ret_data)


class QueryArticleContentView(APIView):
    authentication_classes = []

    @staticmethod
    def get(request):
        try:
            aid = request.GET.get("p", "")
            obj = Article.objects.filter(aid=aid).first()
            content = ""
            category = ""
            pub_time = ""
            if obj:
                content = obj.content
                category = obj.category.category
                pub_time = obj.publish_time.strftime("%Y-%m-%d") if obj.publish_time else ""
                obj.browse += 1
                obj.save()

            ret_data = {"status_code": 1000, "data": content, "category": category, "pub_time": pub_time}
        except Exception as e:
            logger.error(str(e))
            ret_data = {"status_code": 1001, "data": "", "category": "", "pub_time": ""}

        return Response(ret_data)


class QueryArticleThumbView(APIView):
    authentication_classes = []

    @staticmethod
    def get(request):
        try:
            aid = request.GET.get("p", "")
            obj = Article.objects.filter(aid=aid).first()
            thumb = 0
            if obj:
                thumb = obj.thumb
            ret_data = {"status_code": 1000, "data": thumb}
        except Exception as e:
            logger.error(str(e))
            ret_data = {"status_code": 1001, "data": 0}

        return Response(ret_data)


class QueryArticleBrowseView(APIView):
    authentication_classes = []

    @staticmethod
    def get(request):
        try:
            aid = request.GET.get("p", "")
            obj = Article.objects.filter(aid=aid).first()
            browse = 0
            if obj:
                browse = obj.browse
            ret_data = {"status_code": 1000, "data": browse}
        except Exception as e:
            logger.error(str(e))
            ret_data = {"status_code": 1001, "data": 0}

        return Response(ret_data)


class ArticleThumbView(APIView):
    authentication_classes = []

    @staticmethod
    def get(request):
        try:
            host = request.META.get("REMOTE_ADDR", "")
            aid = request.GET.get("p", "")

            # 查询用户是否已赞过该篇文章
            query = ThumbRecord.objects.filter(host=host, article_id=aid)
            if not query:
                # 记录点赞信息
                ThumbRecord.objects.create(
                    tid=str(uuid.uuid4()),
                    host=host,
                    article_id=aid,
                    thumb_time=datetime.datetime.now()
                )

                # 文章点赞数加1
                obj = Article.objects.filter(aid=aid).first()
                if obj:
                    obj.thumb += 1
                    obj.save()

            ret_data = {"status_code": 1000, "message": "success"}
        except Exception as e:
            logger.error(str(e))
            ret_data = {"status_code": 1001, "message": str(e)}

        return Response(ret_data)


class CheckArticleThumbView(APIView):
    authentication_classes = []

    @staticmethod
    def get(request):
        try:
            host = request.META.get("REMOTE_ADDR", "")
            aid = request.GET.get("p", "")

            # 查询用户是否已赞过该篇文章
            query = ThumbRecord.objects.filter(host=host, article_id=aid)
            if query:
                flag = True
            else:
                flag = False
            ret_data = {"status_code": 1000, "flag": flag}
        except Exception as e:
            logger.error(str(e))
            ret_data = {"status_code": 1001, "flag": False}

        return Response(ret_data)
