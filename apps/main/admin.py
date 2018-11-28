import xadmin
from django.contrib import auth
from django.contrib.auth.models import User
from xadmin import views

from apps.main.models import Navigation, Shop, UserProfile, Review, Banner, Category, Order, Property, PropertyValue, \
    ShopCar, ShopImage, SubMenu, SubMenu2


class BaseStyleSettings:
    # 开启主题修改
    enable_themes = True
    # 使用bootbootstrap的主题
    use_bootswatch = True


# 注册自定义全局配置
xadmin.site.register(views.BaseAdminView, BaseStyleSettings)


class GlobalSettings:
    # 修改标题
    site_title = 'tmall商城管理后台'
    # 修改底部显示
    site_footer = 'tmall科技有限公司'


xadmin.site.register(views.CommAdminView, GlobalSettings)


class NavigationAdmin:
    # 默认情况下显示object对象
    list_display = ['nav_id', 'nav_name']


xadmin.site.register(Navigation, NavigationAdmin)


class ShopAdmin:
    # 默认情况下显示object对象
    list_display = ['shop_id', 'name', 'sub_title', 'create_date']
    # 修改分页的默认的条数
    list_per_page = 10
    # 搜索字段
    search_fields = ['name', 'sub_title']
    list_editor = []


xadmin.site.register(Shop, ShopAdmin)


class ReviewAdmin:
    list_display = ['review_id', 'content', 'create_date', 'shop', 'user']


xadmin.site.register(Review, ReviewAdmin)


class BannerAdmin:
    list_display = ['banner_id', 'title', 'image', 'detail_url', 'order', 'create_time']


xadmin.site.register(Banner, BannerAdmin)


class CategoryAdmin:
    list_display = ['cate_id', 'name']


xadmin.site.register(Category, CategoryAdmin)


class OrderAdmin:
    list_display = ['oid', 'order_code', 'address', 'post', 'receiver', 'mobile', 'user_message', 'create_date',
                    'pay_date', 'delivery_date', 'confirm_date', 'status', 'user']


xadmin.site.register(Order, OrderAdmin)


class PropertyAdmin:
    list_display = ['property_id', 'name', 'cate']


xadmin.site.register(Property, PropertyAdmin)


class PropertyValueAdmin:
    list_display = ['pro_value_id', 'shop', 'property', 'value']


xadmin.site.register(PropertyValue, PropertyValueAdmin)


class ShopCarAdmin:
    list_display = ['car_id', 'number', 'shop', 'user', 'order', 'status']


xadmin.site.register(ShopCar, ShopCarAdmin)


class ShopImageAdmin:
    list_display = ['shop_img_id', 'shop', 'type']


xadmin.site.register(ShopImage, ShopImageAdmin)


class SubMenuAdmin:
    list_display = ['sub_menu_id', 'name', 'cate']


xadmin.site.register(SubMenu, SubMenuAdmin)


class SubMenu2Admin:
    list_display = ['sub_menu2_id', 'name', 'sub_menu']


xadmin.site.register(SubMenu2, SubMenu2Admin)


# class UserProfileAdmin:
#     list_display = ['phone', 'desc', 'uid',  'user', 'img_show']
#
#
# xadmin.site.register(UserProfile, UserProfileAdmin)

# # 自定义的admin
# from xadmin.plugins import auth
#
#
# # 显示自定义的方式
# class UserAdmin(auth.UserAdmin):
#     list_display = ['id', 'username', 'email']
#
#
# # 先注销
# xadmin.site.unregister(User)
# # 在注册
# xadmin.site.register(User, UserAdmin)
