from .serializers import GoodsSerializer

from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.generics import ListAPIView

from .models import Goods

# Create your views here.

class GoodsListView(ListAPIView):
    '''
    商品列表页

    '''
    queryset = Goods.objects.all()[:10]
    serializer_class = GoodsSerializer


    # def post(self,request, format=None):
    #     serializer = GoodsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
