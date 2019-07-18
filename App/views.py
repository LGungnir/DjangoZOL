import io
import os
import re
import random


from PIL import Image, ImageDraw, ImageFont
from django.core import serializers
from django.db.models import Q,F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect,reverse
from django.views.decorators.csrf import csrf_exempt

from App.alipay.alipay import AliPay
from ZOL.settings import BASE_DIR
from .forms import *
from .models import *
from .other import *

# 首页
def index(request):
    # 检测用户登录
    user = request.user
    # 楼层
    floors = list(range(3,Floor.objects.all().count()+3))

    data = {
        'user':user,
        'floors':floors,
    }

    return render(request,'index.html',data)

# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # 表单验证成功
            username = form.cleaned_data.get('username')
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password')
            vcode = form.cleaned_data.get('vcode')          # 前台输入的验证码
            verify_code = request.session.get('verify_code')  # 后台生成的验证码


            # 检测验证码
            if vcode.upper() == verify_code.upper():
                # 注册用户，然后跳转到登录页面
                User.objects.create(
                    username=username,
                    phone=phone,
                    password=my_md5(password),          # md5 加密
                )

                return redirect(reverse('ZOL:login'))
            else:
                return render(request, 'register.html', {'msg': '验证码错误'})
        else:
            # 验证失败
            return render(request, 'register.html', {'errors': form.errors})


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # 表单验证成功
            user = form.cleaned_data.get('user')
            vcode = form.cleaned_data.get('vcode')  # 前台输入的验证码
            verify_code = request.session.get('verify_code')  # 后台生成的验证码


            # 检测验证码
            if vcode.upper() == verify_code.upper():
                # 设置session
                request.session['user_id'] = user.id

                return redirect(reverse('ZOL:index'))
            else:
                return render(request, 'login.html', {'msg': '验证码错误'})

        return render(request, 'login.html', {'errors': form.errors})


# 注销
def logout(request):

    del request.session['user_id']
    request.session.flush()
    return redirect(reverse('ZOL:index'))


def good_list(request):
    # if request.method == 'POST':
    key_word = request.POST.get('key_word')
    if not key_word:
        key_word = '0'
    return redirect(reverse('ZOL:goodsearch',args=['0','0','0','0','0','0',key_word]))


# 商品筛选    参数分别为：品牌、最低价格、最高价格、特性、网络、排序、关键词
def good_search(request,brand_name,min_price,max_price,feature,network,sort_by,key_word):

    user = request.user

    # 品牌列表
    brands = Brand.objects.all()

    # 特性列表
    features = ['麒麟980','骁龙855','A12','徕卡','超广角','屏下指纹','全面屏','全视屏','水滴屏']

    # 网络列表
    networks = ['全网通','双4G','移动4G','联通4G','电信4G']

    # 排序列表
    sort_list = ['默认', '高人气', '价格由高到低', '价格由低到高', '发货地']

    # 商品列表
    goods = Good.objects.all()

    # 通过关键词筛选
    if key_word != '0':
        key_word = key_word.replace(' ', '')
        goods = Good.objects.filter(desc__icontains=key_word)


    # 总字符串desc拼接 在进行 关键词搜索
    # 获取Good的属性值列表
    # good_values = Good.objects.values_list()
    # print(good_values)
    # for good_value in good_values:
        # 获取该手机的品牌，把其品牌的名字进行字符串拼接
        # good_brand = Brand.objects.get(id=good_value[-1])
        # value_str = good_brand.cname + good_value[1] + good_brand.ename + good_value[1]
        # for i in range(2, len(good_value) - 3):
            # 拼接除id和img外的属性
            # value_str += str(good_value[i])

        # print('*'*100)
        # print('value_str:',value_str)

        # value_str = value_str.replace(' ','').lower()
        # agood = Good.objects.get(id=good_value[0])
        # agood.desc = value_str
        # agood.save()



    # 通过品牌筛选
    if brand_name != '0':
        goods = goods.filter(brand__cname=brand_name)

    # 通过价格筛选
    if max_price == '0':
        # xx元以上的情况
        goods = goods.filter(price__gte=min_price)
    else:
        # 普通情况：xx元--xx元
        goods = goods.filter(price__range=[min_price,max_price])

    # 通过特性筛选
    if feature != '0':
        # 如小米的水滴屏叫水滴全面屏，因而把屏字去掉过滤
        if re.match(r'\w+屏$',feature):
            goods = goods.filter(feature__contains=feature[:-1])
        else:
            goods = goods.filter(feature__contains=feature)

    # 通过网络筛选
    if network != '0':
        goods = goods.filter(network__contains=network)

    # 通过排序筛选
    # 高人气（销量）和发货地先不写
    if sort_by == 1:
        pass
    elif sort_by == 2:
        goods = goods.order_by('-price')
    elif sort_by == 3:
        goods = goods.order_by('price')
    elif sort_by == 4:
        pass


    data = {
        'user': user,
        'brands':brands,
        'goods':goods,
        'brand_name':brand_name,
        'min_price':min_price,
        'max_price':max_price,
        'features':features,
        'feature':feature,
        'networks':networks,
        'network':network,
        'sort_list':sort_list,
        'sort_by':sort_by,
        'key_word':key_word,
    }

    return render(request, 'goodslist.html', data)


# 商品详情
def good_detail(request,id):
    user = request.user
    good = Good.objects.get(id=id)
    colors = good.color.split(';')
    rams = good.ram.split(';')
    roms = good.rom.split(';')

    data = {
        'user':user,
        'good':good,
        'colors':colors,
        'rams':rams,
        'roms':roms,
    }

    return render(request, 'goodsdetail.html', data)


# 添加商品至购物车
def add_goods_to_cart(request):
    user = request.user
    good_id = request.POST.get('goodId')
    num = request.POST.get('num')
    color = request.POST.get('color')
    ram = request.POST.get('ram')
    rom = request.POST.get('rom')

    data = {
        'status': 1,
        'msg': 'ok',
    }

    # 判断购物车是否存在同样的商品
    carts = Cart.objects.filter(good_id=good_id,user_id=user.id,color=color,ram=ram,rom=rom)
    if carts.exists():
        # 存在相同的商品
        cart = carts.first()
        cart.num += int(num)
        cart.save()
    else:
        # 加入购物车
        cart = Cart()
        cart.user_id = user.id
        cart.good_id = good_id
        cart.num = num
        cart.color = color
        cart.ram = ram
        cart.rom = rom
        cart.save()

    return JsonResponse(data)

# 购物车
def cart(request):
    carts = Cart.objects.filter(user_id=request.user.id)
    # 初始化被选择的状态
    carts.update(is_select=0)
    return render(request, 'cart.html',{'carts':carts})


# 购物车商品数量增加( +号 )
def num_add(request):
    data = {
        'status': 1,
        'msg': 'ok'
    }

    if request.method == 'GET':
        cart_id = request.GET.get('cart_id')

        cart = Cart.objects.filter(id=cart_id).first()
        if cart:
            cart.num += 1
            cart.save()
            data['num'] = cart.num
        else:
            data['status'] = -1
            data['msg'] = '不存在该记录'
    else:
        data['status'] = -3
        data['msg'] = '请求方式错误'

    return JsonResponse(data)


# 购物车商品数量减少( -号 )
def num_reduce(request):
    data = {
        'status': 1,
        'msg': 'ok'
    }

    if request.method == 'GET':
        cart_id = request.GET.get('cart_id')

        cart = Cart.objects.filter(id=cart_id).first()
        if cart:
            if cart.num > 1:
                cart.num -= 1
                cart.save()
                data['num'] = cart.num
            else:
                data['msg'] = '商品数量至少为1'
        else:
            data['status'] = -1
            data['msg'] = '不存在该记录'
    else:
        data['status'] = -3
        data['msg'] = '请求方式错误'

    return JsonResponse(data)


# 购物车删除商品
def good_del(request):
    data = {
        'status': 1,
        'msg': 'ok'
    }

    if request.method == 'GET':
        cart_id = request.GET.get('cart_id')
        Cart.objects.filter(id=cart_id).first().delete()
    else:
        data['status'] = -3
        data['msg'] = '请求方式错误'

    return JsonResponse(data)


# 更换勾选状态
def select_change(request):
    data = {
        'status': 1,
        'msg': 'ok'
    }

    if request.method == 'GET':
        cart_id = request.GET.get('cart_id')
        cart = Cart.objects.filter(id=cart_id).first()
        if cart:
            cart.is_select = not cart.is_select
            cart.save()
            data['is_select'] = cart.is_select
        else:
            data['status'] = -1
            data['msg'] = '不存在该记录'
    else:
        data['status'] = -3
        data['msg'] = '请求方式错误'

    return JsonResponse(data)


# 全选状态判断
def all_select(request):
    data = {
        'status': 1,
        'msg': 'ok'
    }

    if request.method == 'GET':
        # 全部商品的勾选状态随全选颠倒
        is_all_select = int(request.GET.get('isAllSelect'))
        carts = Cart.objects.filter(user_id=request.user.id)
        carts.update(is_select=not is_all_select)

        # 返回倒转的状态
        data['is_all_select'] = not is_all_select
    else:
        data['status'] = -3
        data['msg'] = '请求方式错误'

    return JsonResponse(data)


# 增添订单
def add_order(request):
    data = {
        'status': 1,
        'msg': 'ok'
    }

    if request.method == 'POST':
        # 生成订单
        order = Order()
        order.order_id = get_uid()
        order.user_id = request.user.id
        order.save()

        # 生成订单商品
        carts = Cart.objects.filter(user_id=request.user.id,is_select=True)
        total = 0
        for cart in carts:
            order_goods = OrderGoods()
            order_goods.goods_id = cart.good.id
            order_goods.order_id = order.id
            order_goods.num = cart.num
            order_goods.color = cart.color
            order_goods.ram = cart.ram
            order_goods.rom = cart.rom
            order_goods.save()

            total += order_goods.num * order_goods.goods.price

        order.order_price = total
        order.save()
        # 删除购物车中被提交的
        carts.delete()
        data['order_id'] = order.order_id
    else:
        data['status'] = -3
        data['msg'] = '请求方式错误'

    return JsonResponse(data)


# 提交订单页面
def post_order(request,order_id):
    orders = Order.objects.filter(order_id=order_id,user_id=request.user.id)

    if orders.exists():
        order = orders.first()
        # 方便跳转
        request.session['order_id'] = order.order_id
    else:
        return HttpResponse('此非您的订单，无权访问')
    order_goods = order.ordergoods_set.all()

    receives = Receive.objects.filter(user_id=request.user.id)

    # 设置准备支付订单的session
    request.session['paying_order_id'] = order_id

    data = {
        'order':order,
        'order_goods':order_goods,
        'receives':receives,
    }

    return render(request,'postorder.html',data)


# 立即购买
def buy_now(request):
    # 先增添订单
    data = {
        'status': 1,
        'msg': 'ok'
    }

    user = request.user
    good_id = request.POST.get('goodId')
    num = request.POST.get('num')
    color = request.POST.get('color')
    ram = request.POST.get('ram')
    rom = request.POST.get('rom')

    if request.method == 'POST':
        # 生成订单
        order = Order()
        order.order_id = get_uid()
        order.user_id = request.user.id
        order.save()

        # 生成订单商品
        order_goods = OrderGoods()
        order_goods.goods_id = good_id
        order_goods.order_id = order.id
        order_goods.num = num
        order_goods.color = color
        order_goods.ram = ram
        order_goods.rom = rom
        order_goods.save()

        order.order_price = float(num) * float(Good.objects.get(id=good_id).price)
        order.save()

        data['order_id'] = order.order_id
    else:
        data['status'] = -3
        data['msg'] = '请求方式错误'

    return JsonResponse(data)



# 增加收货地址
def add_receive_info(request):
    if request.method == 'GET':
        return render(request, 'addreceiveinfo.html')

    elif request.method == 'POST':
        person = request.POST.get('person')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        receives = Receive.objects.filter(user_id=request.user.id,person=person,phone=phone,address=address)
        if receives.exists():
            return HttpResponse('该收货地址已存在')

        # 新建收货信息
        receive = Receive()
        receive.person = person
        receive.phone = phone
        receive.address = address
        receive.user_id = request.user.id
        receive.save()

        order_id = request.session.get('order_id')
        status = request.session.get('status')

        del request.session['order_id']
        # flush回重载回到登录页面
        # request.session.flush()
        if not status:
            # 跳转回订单页面,并初始化(删除)order_id
            return redirect('/ZOL/postorder/' + order_id)
        else:
            # 添加收货信息至订单，并跳转到订单集合
            order = Order.objects.filter(order_id=order_id).first()
            order.receive = receive
            order.save()
            return redirect(reverse('ZOL:order'))


# 为订单添加收货信息
def order_add_receive(request):
    data = {
        'status': 1,
        'msg': 'ok'
    }

    if request.method == 'POST':
        receive_id = request.POST.get('receive_id')
        order_id = request.POST.get('order_id')

        # 为订单添加收货信息
        order = Order.objects.filter(order_id=order_id).first()
        order.receive_id = receive_id
        order.save()

    else:
        data['status'] = -3
        data['msg'] = '请求方式错误'

    return JsonResponse(data)


# 订单集合页面
def order(request):
    orders = Order.objects.filter(user_id=request.user.id)

    data = {
        'orders':orders,
    }

    return render(request,'order.html',data)


# 小跳转，订单集合页面的跳转给予session
def little_skip(request,order_id,status):
    # 跳转到收货页面
    if status == 1:
        request.session['order_id'] = order_id
        # 判断依据
        request.session['status'] = status
        return redirect(reverse('ZOL:receiveinfo'))

    # 跳转到支付宝
    elif status == 2:
        request.session['paying_order_id'] = order_id
        return redirect(reverse('ZOL:api'))


# 验证码
def generate_verifycode(request):
    # 1.创建画布
    # mode: 颜色模式
    # size: 画布大小
    # bgcolor: 背景颜色RGB
    image = Image.new('RGB', (100, 50), random_color())

    # 2.创建画笔
    draw = ImageDraw.Draw(image, 'RGB')

    # 3.创建字体
    font_path = 'static/fonts/ADOBEARABIC-BOLD.OTF'
    # font_path = os.path.join(BASE_DIR, font_path)
    font = ImageFont.truetype(font_path, 40)

    # 4.画
    code = random_code()
    draw.text((10, 5), code, font=font, fill=random_color())

    # 保存验证码，方便后续验证
    request.session['verify_code'] = code

    # 干扰点
    for i in range(100):
        draw.point((random.randint(0,98), random.randint(0,48)), fill=random_color())

    # 5.渲染成图片
    buff = io.BytesIO()  # 创建一个二进制的缓冲区
    image.save(buff, 'png')  # 将画布以png图片形式保存到缓冲区

    # 联合ajax重载
    data = buff.getvalue()
    return HttpResponse(data)
    # return HttpResponse(buff.getvalue(), 'image/png')  # 将图片二进制取出，并以png形式响应到浏览器


# 支付宝相关接口
# 接口
def api(request):
    return render(request, 'alipay.html')

# 支付
def pay(request):
    order_id = request.session.get('paying_order_id')
    order = Order.objects.filter(order_id=order_id).first()

    # 传递参数初始化支付类
    alipay = AliPay(
        appid="2016100100640329",  # 设置签约的appid
        app_notify_url="http://120.25.165.214/ZOL/notify/",  # "http://projectsedus.com/",  # 异步支付通知url
        app_private_key_path=r"App/alipay/ying_yong_si_yao.txt",  # 设置应用私钥
        alipay_public_key_path=r"App/alipay/zhi_fu_bao_gong_yao.txt",  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        debug=True,  # 默认False,            # 设置是否是沙箱环境，True是沙箱环境
        return_url="http://120.25.165.214/ZOL/result/",  # "http://47.92.87.172:8000/"  # 同步支付通知url
    )

    # 传递参数执行支付类里的direct_pay方法，返回签名后的支付参数，
    url = alipay.direct_pay(
        subject="ZOL商城订单",  # 订单名称
        # 订单号生成，一般是当前时间(精确到秒)+用户ID+随机数
        out_trade_no= order.order_id,  # 订单号
        total_amount= order.order_price,  # 支付金额
        return_url="http://120.25.165.214/ZOL/result/"  # 支付成功后，跳转url
    )

    # 将前面后的支付参数，拼接到支付网关
    # 注意：下面支付网关是沙箱环境，最终进行签名后组合成支付宝的url请求
    re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
    # print(re_url)
    return JsonResponse({'re_url': re_url})


# 异步支付通知url (上线后使用)
def notify(request):
    print("notify:", dict(request.GET))
    return HttpResponse("支付成功:%s" % (dict(request.GET)))


# 付款成功后跳转的url
def result(request):
    # 获取订单，添加已支付状态
    order_id = request.session.get('paying_order_id')
    order = Order.objects.filter(order_id=order_id).first()
    order.order_status = 1
    order.save()

    # 并删除(初始化)支付订单id
    del request.session['paying_order_id']
    # request.session.flush()

    return redirect(reverse('ZOL:index'))
    # print("result:", dict(request.GET))
    # return HttpResponse("支付成功:%s" % (dict(request.GET)))


# 首页的ajax
# 大轮播图
def get_banners(request):
    if request.method == 'GET':
        data = list(Banner.objects.values('img'))

    return JsonResponse(data,safe=False)


# 小轮播图
def get_luns(request):
    if request.method == 'GET':
        data = list(Lun.objects.values('img'))

    return JsonResponse(data,safe=False)


# 团购
def get_tuans(request):
    if request.method == 'GET':
        data = list(Tuan.objects.values('img'))

    return JsonResponse(data,safe=False)


# 楼层商品
def get_floor_goods(request):
    if request.method == 'GET':
        # 楼层总集合
        floor_all_info = []

        for i in range(1,Floor.objects.all().count()+1):
            # 单层集合
            floor_info = []
            mainsell = list(Floor.objects.filter(id=i).values('img'))[0]
            floor_info.append(mainsell)

            goods = FloorGood.objects.filter(floor=i)
            for good in goods:
                good_dict = {}
                good_dict['id'] = good.product_id
                good_dict['img'] = good.img
                good_dict['a'] = good.a
                good_dict['p'] = good.p
                good_dict['price'] = good.price
                floor_info.append(good_dict)

            mainlist = list(Floor.objects.filter(id=i).values('img2'))[0]
            floor_info.append(mainlist)

            floor_all_info.append(floor_info)

        data = floor_all_info

    return JsonResponse(data,safe=False)


# 添加品牌
def add_brand(request):
    # 品牌名称列表
    brand_cnames = ['华为', '三星', '荣耀', '魅族', '酷派', '联想', '宏达电', '小米', '中兴',
              '欧珀', '苹果', '乐视', '维沃', '飞利浦', '努比亚', '摩托罗拉', '索尼','一加']
    brand_enames = ['huawei', 'sansung', 'honor', 'meizu', 'coolpad', 'lenovo', 'htc', 'xiaomi', 'zte',
              'oppo', 'apple', 'letv', 'vivo', 'philips', 'nuoio', 'motorola ', 'sony','oneplus']

    for i in range(18):
        Brand.objects.create(
            cname = brand_cnames[i],
            ename = brand_enames[i],
            img = '/static/img/goodslist/logo' + str(i+1) + '.jpg'
        )

    return HttpResponse('add brands ok')


# 添加楼层商品    模型已改，此函数作废
def add_floor_goods(reequest):
    # 名称列表
    name_list = ['魅族MX6(全网通)','三星新品C5','魅蓝Note3(全网通)','荣耀 8 全网通','苹果的iPhone 6S Plus','vivo X7 Plus']
    # 描述列表
    desc_list = ['PADE相位对焦','骁龙八核 更有惊艳粉色','金属机身 指纹解锁','好手感 令人无法拒绝','唯一的不同,处处都相同','赠豪华大礼包']
    # 价格列表
    price_list = [1998,2998,948,991,2324,1243]

    count = 0
    for i in range(1,5):            # 1F - 4F
        for j in range(6):          # 6个商品
            good = FloorGood()
            good.product_id = 10086 + count
            count += 1
            good.name = name_list[j]
            good.desc = desc_list[j]
            good.price = price_list[j]
            k = j + 1
            good.img = '/static/img/%df/%d.jpg' % (i,k)
            good.save()

    return HttpResponse('add ok')


# 添加楼层      模型已改，此函数作废
def add_floor(reequest):
    for i in range(1,5):
        goods = FloorGood.objects.all()[(i-1)*6 : i*6]
        floor = Floor()
        floor.img1 = '/static/img/%df/mainsell.jpg' % i
        floor.img2 = '/static/img/1f/lun.jpg'
        floor.good1 = goods[0]
        floor.good2 = goods[1]
        floor.good3 = goods[2]
        floor.good4 = goods[3]
        floor.good5 = goods[4]
        floor.good6 = goods[5]
        floor.save()

    return HttpResponse('add floor ok')

# 添加分类
def add_class(request):
    # 兄类
    types = '平板电视 迷你音响 电视盒子 烤箱 电水壶 蒸蛋器 酸奶机 电火锅 咖啡机 豆浆机 电饭煲 多士炉 料理/榨汁机'
    type_list = types.split(' ')
    for type in type_list:
        atype = BrotherType()
        atype.name = type
        atype.parent_id = 33
        atype.save()


    # 爷类
    # types_str = '手机配件/移动设备;笔记本/平板/品牌整机;摄影摄像/数码配件;游戏电玩/游戏本;DIY硬件/外设配件/网络设备;智能生活/智能设备/智能投影;家用设备/办公设备;生活电器/个护/家用电器'
    #
    # i = 0
    # j = 1
    # for type_list in types_str.split(';'):
    #     i += 1
    #     for type in type_list.split('/'):
    #         j += 1
    #         atype = GrandType()
    #         atype.name = type
    #         atype.id = j
    #         atype.ancestral_id = i
    #         atype.save()

    # 祖类
    # types = ['电脑','照相机','游戏设备','硬件','智能设备','设备','电器']
    # for type in types:
    #     atype = AncestralType()
    #     atype.name = type
    #     atype.save()

    return HttpResponse('okk')