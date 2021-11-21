import time

import cv2
import numpy as np
import pyautogui
import win32api
import win32con


def aHash(img):
    # 缩放为8*8
    img = cv2.resize(img, (8, 8), interpolation=cv2.INTER_CUBIC)


    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # s为像素和初值为0，hash_str为hash值初值为''
    s = 0
    hash_str = ''
    # 遍历累加求像素和
    for i in range(8):
        for j in range(8):
            s = s + gray[i, j]
    # 求平均灰度
    avg = s / 64
    # 灰度大于平均值为1相反为0生成图片的hash值
    for i in range(8):
        for j in range(8):
            if gray[i, j] > avg:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str


# 差值感知算法
def dHash(img):
    # 缩放8*8
    img = cv2.resize(img, (9, 8), interpolation=cv2.INTER_CUBIC)
    # 转换灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hash_str = ''
    # 每行前一个像素大于后一个像素为1，相反为0，生成哈希
    for i in range(8):
        for j in range(8):
            if gray[i, j] > gray[i, j + 1]:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str


# Hash值对比
def cmpHash(hash1, hash2):
    n = 0
    # hash长度不同则返回-1代表传参出错
    if len(hash1) != len(hash2):
        return -1
    # 遍历判断
    for i in range(len(hash1)):
        # 不相等则n计数+1，n最终为相似度
        if hash1[i] != hash2[i]:
            n = n + 1
    return n
# time.sleep(2)
# #img1 = cv2.imread('similarity//gongye7.jpg')
# im = pyautogui.screenshot(region=[0,0,1920,1080])
# im.save("similarity//gongye11111112.jpg")
# img1 = np.array(im)
#
# img2 = cv2.imread('similarity//gongye11111111.jpg')
# hash1 = aHash(img1)
# hash2 = aHash(img2)
# print(hash1)
# print(hash2)
# n = cmpHash(hash1, hash2)
# print ('均值哈希算法相似度：' + str(n))
#
# hash1 = dHash(img1)
# hash2 = dHash(img2)
# print(hash1)
# print(hash2)
# n = cmpHash(hash1, hash2)
# print ('差值哈希算法相似度：' + str(n))

def MouseMove(args):
    xLen = int(args[0])
    yLen = int(args[1])
    # xPosion,yPosion = pyautogui.position()
    # if(xPosion+xLen) > screenSize.width:
    #     xLen = screenSize.width-xPosion
    # if(yPosion+yLen) > screenSize.height:
    #     yLen = screenSize.height-yPosion
    try:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, xLen,yLen)
    except:
        print("问题不大")
def MouseDown(args):
    pyautogui.mouseDown(button=args[0])
def MouseUp(args):
    pyautogui.mouseUp(button=args[0])
def MouseAbsoluteMove(args):
    try:
        win32api.SetCursorPos((int(args[0]),int(args[1])))
    except:
        print("问题不大")
time.sleep(2)
print(win32api.GetCursorPos())
MouseAbsoluteMove(["100","100"])
print(win32api.GetCursorPos())
# ————————————————
# 版权声明：本文为CSDN博主「Ev.小强」的原创文章，遵循CC
# 4.0
# BY - SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https: // blog.csdn.net / u011397539 / article / details / 82982499