from django.urls import path
from .views import *

app_name = '[ZOL]'
urlpatterns = [
    # 首页
    path('',index,name='index'),                                                # 首页
    path('getbanners/',get_banners,name='getbanners'),                          # 大轮播图
    path('getluns/',get_luns,name='getluns'),                                   # 小轮播图
    path('gettuans/',get_tuans,name='gettuans'),                                # 团购
    path('getfloorgoods/',get_floor_goods,name='getfloorgoods'),                # 获取楼层商品

    path('register/',register,name='register'),                                 # 注册
    path('login/',login,name='login'),                                          # 登录
    path('verifycode/', generate_verifycode, name='verifycode'),                # 验证码
    path('logout/', logout, name='logout'),                                     # 注销
    path('addfloorgoods/',add_floor_goods,name='addfloorgoods'),                # 添加楼层商品
    path('addfloor/',add_floor,name='addfloor'),                                # 添加楼层
    path('addclass/', add_class, name='addclass'),                              # 添加分类

    path('goodlist/',good_list,name='goodlist'),                                # 商品列表
    # 商品搜索筛选
    path('goodsearch/<brand_name>/<min_price>/<max_price>/<feature>/<network>/<int:sort_by>/<key_word>/',
         good_search,name='goodsearch'),
    path('add_brand/',add_brand,name='addbrand'),                               # 添加品牌
    path('gooddetail/<id>/',good_detail,name='gooddetail'),                     # 商品详情

    # 购物车
    path('addcart/',add_goods_to_cart,name='addcart'),                          # 添加商品至购物车
    path('cart/',cart,name='cart'),                                             # 购物车
    path('numadd/',num_add,name='numadd'),                                      # 商品数量增加
    path('numreduce/',num_reduce,name='numreduce'),                             # 商品数量增加
    path('gooddel/',good_del,name='gooddel'),                                   # 商品删除
    path('selectchange/',select_change,name='selectchange')    ,                # 更改商品勾选状态
    path('allselect/',all_select,name='all_select'),                            # 全选状态判断

    # 购买
    path('buynow/',buy_now,name='buynow'),                                      # 立即购买

    # 订单
    path('postorder/<order_id>/',post_order,name='postorder'),                  # 提交订单
    path('addorder/',add_order,name='addorder'),                                # 增添订单
    path('receiveinfo/',add_receive_info,name='receiveinfo'),                   # 新增收货地址
    path('orderaddreceive/',order_add_receive,name='orderaddreceive'),          # 为订单添加收货信息
    path('order/',order,name='order'),                                          # 订单集合页面
    path('littleskip/<order_id>/<int:status>/',little_skip,name='littleskip'),  # 一个小跳转


    # 支付宝
    path('api/',api,name='api'),                                                # 支付宝接口
    path('pay/', pay,name='pay'),                                               # 支付宝支付
    path('notify/', notify,name='notify'),
    path('result/', result,name='result'),                                      # 支付宝结果
]