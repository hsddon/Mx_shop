from rest_framework import serializers

from goods.models import Goods
from goods.models import GoodsCategory

#自定义自己的serializer，定义所有的字段，对表进行序列化成json
# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()
#
#     def create(self, validated_data):
#         '''
#         :param validated_data:
#         :return:
#         '''
#         return Goods.objects.create(**validated_data)

class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = GoodsCategorySerializer()
    class Meta:
        model = Goods
        fields = "__all__"