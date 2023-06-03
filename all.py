# 创建跨文件全局列表


def _init():  # 初始化
    global mingzi  # 传输名字
    global urlming  # 传输url
    global over1  # 传输删除指令
    global zhan01  # 传输是删除按钮还是更改按钮执行
    global vvvip  # vip识别
    global urlexe  # 网站exe传输
    global url_loc  # 存入网站还是本地的指令
    global know_name  # 存入数据,知道到时候数据存入GitHub哪个txt文件中
    global zh_cre  # 将账号内容转移到creat, 用于检测账号是否被注册过 & 找回账号密码配对
    global mim_cre  # 找回账号密码配对
    global check_back_home  # 检测是否要返回登陆界面
    global check_WIFI_detroy  # 检测是否不保存直接退出程序
    mingzi = []
    urlming = []
    over1 = []
    zhan01 = []
    vvvip = []
    urlexe = []
    url_loc = []
    know_name = []
    zh_cre = []
    mim_cre = []
    check_back_home = []
    check_WIFI_detroy = [100]


def len1():
    return len(urlming)


# 存储要更改的按钮文本
def set_value(value):
    mingzi.append(value)


# 存储要更改的按钮用途
def set_value2(value):
    urlming.append(value)


def set_over1(value):
    over1.append(value)


def set_shan01(value):
    zhan01.append(value)


# 获得按钮文本
def get_value(defValue=None):
    try:
        return mingzi[0]
    except KeyError:
        return defValue


# 获得按钮用途
def get_value2(defValue=None):
    try:
        return urlming[0]
    except KeyError:
        return defValue


def get_over1(defValue=1):
    try:
        if len(over1) > 0:
            return over1[0]
    except KeyError:
        return defValue


def get_shan01(defValue=2):
    try:
        if len(zhan01) > 0:
            return zhan01[0]
    except KeyError:
        return defValue


# 删除按钮文本(保持纯净，便于下次调用)
def shan1():
    if len(mingzi) > 0:
        del mingzi[0]


# 删除按钮用途(便于下次调用)
def shan2():
    if len(urlming) > 0:
        del urlming[0]


def vvvip1(good):
    vvvip.append(good)


def vvvip2():
    return len(vvvip)


def urlget(u):
    if len(urlexe) > 0:
        urlexe.clear()
    urlexe.append(u)


def get_urlexe(defValue=None):
    try:
        return urlexe[0]
    except KeyError:
        return defValue


def check_urlexe():
    return len(urlexe)


def set_url_loc(got):
    if len(url_loc) > 0:
        url_loc.clear()
    url_loc.append(got)


def get_url_loc(defValue=None):
    try:
        return url_loc[0]
    except KeyError:
        return defValue


def Know4(value):
    know_name.append(value)


def know1():
    return know_name[0]


def zh_cre_qu(value):
    zh_cre.clear()
    zh_cre.extend(value)


def zh_cre_verify():
    return zh_cre


def mim_cre_qu(value):
    mim_cre.clear()
    mim_cre.extend(value)


def mim_cre_verify():
    return mim_cre


def check_home1(value):
    check_back_home.append(value)


def check_home2():
    return len(check_back_home)


def check_home3():
    check_back_home.clear()


def check_out1(value):
    check_WIFI_detroy.append(value)


def check_out2():
    return check_WIFI_detroy[0]


def check_out3():
    check_WIFI_detroy.clear()
