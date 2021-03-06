from rest_framework import viewsets
from rest_framework.response import Response
from .models import Manufactory, ProductModel
from .serializers import ManufactorySerializer, ProductModelSerializer


# Create your views here.

class ManufactoryViewset(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定制造商信息
    list:
        返回制造商列表
    update:
        更新制造商信息
    partial_update:
        更新部分制造商字段
    destory:
        删除制造商信息
    create:
        创建制造商记录
    """
    serializer_class = ManufactorySerializer

    def get_queryset(self):
        return Manufactory.objects.all()

    def list(self, request, *args, **kwargs):
        # 当传回nopage参数为1时，不分页
        queryset = self.filter_queryset(self.get_queryset())
        nopage = request.query_params.get("nopage")
        manufactory = self.get_queryset()
        if nopage == '1':
            self.paginator.page_size = manufactory.count()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProductModelViewset(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定产品型号信息
    list:
        返回产品型号列表
    update:
        更新产品型号信息
    partial_update:
        更新部分产品型号字段
    destory:
        删除产品型号信息
    create:
        创建产品型号记录
    """
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
