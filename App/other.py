import hashlib
import random
import uuid


# 没用到路由的函数
# 生成随机的4位验证码
def random_code():
    string = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    code = ""
    for i in range(4):
        code += random.choice(string)
    return code

# 随机颜色
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

# 生成唯一的uuid
def get_uid():
    return str(uuid.uuid4())


# md5
def my_md5(s):
    m = hashlib.md5()
    m.update(s.encode())
    return m.hexdigest()