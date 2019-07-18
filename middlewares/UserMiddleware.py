from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect,reverse
from django.utils.deprecation import MiddlewareMixin
import re

from App.models import User


class UserLoginMiddleware(MiddlewareMixin):
    def process_request(self,request):

        # 是否登录也没关系的列表(首页，商品列表，商品详情)
        path_list1 = ['/','/ZOL/',
                      # r'^/ZOL/goodsearch/(.+\/){6}',
                      # r'^/ZOL/gooddetail/\d+/',
                      '/ZOL/goodsearch/',
                      '/ZOL/gooddetail/'
                      ]

        # 以下的必须登录才能操作
        # render(用于显示数据)
        path_list2 = ['/ZOL/cart/',
                      # r'/ZOL/postorder/[-\w]+/',
                      '/ZOL/postorder/',
                      '/ZOL/receiveinfo/',
                      '/ZOL/api/',
                      '/ZOL/pay/',
                      '/ZOL/notify/',
                      '/ZOL/result/',
                      '/ZOL/order/',
                      '/ZOL/littleskip/',
                      ]

        # ajax(用于处理数据)
        path_list3 = [
                      '/ZOL/addcart/',
                      '/ZOL/numadd/',
                      '/ZOL/numreduce/',
                      '/ZOL/gooddel/',
                      '/ZOL/selectchange/',
                      '/ZOL/allselect/',
                      '/ZOL/addorder/',
                      '/ZOL/orderaddreceive/',
                      '/ZOL/buynow/',
                      ]

        path_list = path_list2 + path_list3


        # 若使用正则后面匹配的情况过多，但头部的都一样，因而取头部进行匹配
        if request.path not in ['/','/ZOL/']:
            req_path  = '/'.join(request.path.split('/')[:3]) + '/'
        else:
            req_path = request.path


        # 使用正则匹配，略麻烦
        # if request.path == path_list1[0] or request.path == path_list1[1] or \
        #     re.match(path_list1[2],request.path) or re.match(path_list1[3],request.path):
        #     try:
        #         user_id = request.session.get('user_id')
        #         user = User.objects.get(id=user_id)
        #         request.user = user
        #     except:
        #         pass

        if req_path in path_list1:
            try:
                user_id = request.session.get('user_id')
                user = User.objects.get(id=user_id)
                request.user = user
            except:
                pass

        elif req_path in path_list:
            # 是否登录
            user_id = request.session.get('user_id')
            if not user_id:
                if req_path in path_list2:
                    return redirect(reverse('ZOL:login'))
                else:
                    data = {
                        'status': 0,
                        'msg': '您尚未登录， 请先登录!'
                    }
                    return JsonResponse(data)
            else:
                try:
                    user_id = request.session.get('user_id')
                    user = User.objects.get(id=user_id)
                    request.user = user
                except:
                    if req_path in path_list1:
                        return redirect(reverse('ZOL:login'))
                    else:
                        data = {
                            'status': -2,
                            'msg': '用户不存在!'
                        }

                        return JsonResponse(data)
