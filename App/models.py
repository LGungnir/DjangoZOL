from django.db import models

class User(models.Model):
    username = models.CharField(max_length=32,unique=True)          # 用户名
    phone = models.CharField(max_length=11,unique=True)             # 手机号
    password = models.CharField(max_length=32)                      # 密码
    money = models.FloatField(max_length=32,default=0.00)           # 充钱


# 大轮播图
class Banner(models.Model):
    img = models.CharField(max_length=255)


# 小轮播图
class Lun(models.Model):
    img = models.CharField(max_length=255)


# 团购
class Tuan(models.Model):
    img = models.CharField(max_length=255)


# 首页楼层
class Floor(models.Model):
    img = models.CharField(max_length=255)                         # miansell 左侧大图
    img2 = models.CharField(max_length=255)                        # mianlist 上面大图


# 首页展现的商品
class FloorGood(models.Model):
    product_id = models.IntegerField()                            # 编号  对应json的id
    a = models.CharField(max_length=128)                          # 名称  对应json的a
    p = models.CharField(max_length=255)                          # 描述  对应json的p
    price = models.IntegerField(default=0)                        # 价格
    img = models.CharField(max_length=255)                        # 图片
    floor = models.ForeignKey(Floor,on_delete=models.CASCADE,default=1)


# 祖类
class AncestralType(models.Model):
    name = models.CharField(max_length=32)

# 爷类
class GrandType(models.Model):
    name = models.CharField(max_length=32)
    ancestral = models.ForeignKey(AncestralType, on_delete=models.CASCADE)

# 父类
class ParentType(models.Model):
    name = models.CharField(max_length=32)
    grand = models.ForeignKey(GrandType, on_delete=models.CASCADE)

# 兄类
class BrotherType(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey(ParentType, on_delete=models.CASCADE)


# 品牌
class Brand(models.Model):
    cname = models.CharField(max_length=32,unique=True)             # 中文名称
    ename = models.CharField(max_length=32,unique=True)             # 英文名称
    img = models.ImageField(max_length=255,upload_to='./static/img/brands', default='/static/img/default.jpg')      # logo图片

    def __str__(self):
        return self.cname


# 商品(现专指手机)
class Good(models.Model):
    name = models.CharField(max_length=32)                          # 名字
    price = models.FloatField(default=1)                            # 价格
    feature = models.CharField(max_length=255)                      # 特性 (多对多)
    network = models.CharField(max_length=32,default='全网通')      # 网络类型
    color = models.CharField(max_length=32,default='黑色')          # 颜色
    ram = models.CharField(max_length=32,default='8')               # 运行内存
    rom = models.CharField(max_length=32,default='128')             # 只读内存
    img = models.ImageField(max_length=255,upload_to='./static/img/goods',default='/static/img/default.jpg')   # 图片 upload_to 添加相对路径
    desc = models.CharField(max_length=512,default='')              #把前面的所有属性包括的总描述

    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)       # 品牌 (手机：品牌 = n:1)
    type = models.ForeignKey(BrotherType,on_delete=models.CASCADE)  # 兄类

    def __str__(self):
        return self.brand.cname + ' ' + self.name


# 购物车
class Cart(models.Model):
    good = models.ForeignKey(Good,on_delete=models.CASCADE)         # 商品
    user = models.ForeignKey(User,on_delete=models.CASCADE)         # 用户
    num = models.IntegerField(default=1)                            # 商品数量
    color = models.CharField(max_length=32,default='黑色')          # 商品颜色
    ram = models.IntegerField(default=8)                            # 商品运行内存
    rom = models.IntegerField(default=128)                          # 商品只读内存
    is_select = models.BooleanField(default=True)                   # 勾选状态


# 收货信息
class Receive(models.Model):
    person = models.CharField(max_length=32)                        # 收货人
    phone = models.CharField(max_length=11)                         # 收货电话
    address = models.CharField(max_length=255)                      # 收货地址
    user = models.ForeignKey(User,on_delete=models.CASCADE)         # 所属用户


# 订单
class Order(models.Model):
    order_id = models.CharField(max_length=255,unique=True)         # 订单编号
    order_create = models.DateTimeField(auto_now_add=True)          # 订单的创建时间
    order_price = models.FloatField(default=0)                      # 订单价格
    # 订单状态： 0表示未支付， 1表示已支付，2表示待评价，3已退款，4订单已取消,...
    order_status = models.IntegerField(default=0)                   # 订单状态
    user = models.ForeignKey(User,on_delete=models.CASCADE)         # 订单所属的用户
    receive = models.ForeignKey(Receive,on_delete=models.CASCADE,null=True)  # 收货信息


# 订单商品表
class OrderGoods(models.Model):
    goods = models.ForeignKey(Good,on_delete=models.CASCADE)        # 商品
    order = models.ForeignKey(Order,on_delete=models.CASCADE)       # 所属订单
    num = models.IntegerField()                                     # 商品数量
    color = models.CharField(max_length=32, default='黑色')         # 商品颜色
    ram = models.IntegerField(default=8)                            # 商品运行内存
    rom = models.IntegerField(default=128)                          # 商品只读内存


