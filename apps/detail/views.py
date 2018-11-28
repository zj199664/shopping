from django.shortcuts import render
from apps.account.models import *


def detail(request):
    if request.method == 'GET':
        try:
            shop_id = request.GET.get('shop_id')
            if shop_id:
                # 获取商品的所有信息
                shop = Shop.objects.get(shop_id=shop_id)
                # 获取商品的图片信息
                shop.imgs = shop.shopimage_set.all()
                # 获取商品的参数信息
                values = shop.propertyvalue_set.all()
                # for value in shop.values:
                # 获取商品的评论信息
                reviews = shop.review_set.all()
                count = shop.review_set.all().count()
                return render(request, 'detail.html',
                              {'shop': shop, 'values': values, 'reviews': reviews, 'count': count})
        except Exception as e:
            return render(request, 'error.html')
