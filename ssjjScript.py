import time

import numpy as np
import pyautogui
import win32api
import win32con
from utils.imgSimilarity import *
'''
Sleep [暂停秒数]
KeyDown [按什么键] 
KeyUp [松开什么键]
MouseDown [按下鼠标LEFT或RIGHT]
MouseUp [松开鼠标LEFT或RIGHT]

MouseMove [相对移动X坐标] [相对移动Y坐标]

MouseAbsoluteMove [绝对移动X坐标] [绝对移动Y坐标]

WhenSimilarity [相似度判断条件] [匹配图片位置] [执行的脚本文件]
'''
screenSize = pyautogui.size()
similarityDirPath = "similarity/"
def Sleep(sleepTime):
    print("睡眠"+sleepTime[0])
    time.sleep(float(sleepTime[0]))
def KeyDown(args):
    try:
        pyautogui.keyDown(args[0])
    except:
        print("键盘按下键出了问题,但跳过了")
def KeyUp(args):
    try:
        pyautogui.keyUp(args[0])
    except:
        print("键盘松开键出了问题，但跳过了")
def MouseDown(args):
    try:
        pyautogui.mouseDown(button=args[0])
    except:
        print("鼠标按下键出了问题,但跳过了")
def MouseUp(args):
    try:
        pyautogui.mouseUp(button=args[0])
    except:
        print("鼠标松开键出了问题,但跳过了")
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
def MouseAbsoluteMove(args):
    try:
        win32api.SetCursorPos((int(args[0]),int(args[1])))
    except:
        print("问题不大")
def WhenSimilarity(args):
    condition = args[0]
    imgPath = similarityDirPath+args[1]
    execFile = args[6]
    startX = int(args[2])
    startY = int(args[3])
    imgWidth = int(args[4])
    imgHeight = int(args[5])
    screenImg = pyautogui.screenshot(region=[startX, startY, imgWidth, imgHeight])
    sourceImgAHash = dHash(cv2.imread(imgPath))
    screenImgAHash = dHash(np.array(screenImg))
    difference = cmpHash(sourceImgAHash,screenImgAHash)
    n = int(condition[1:])
    print("预期:"+condition+"   "+"差值:"+str(difference))
    if condition.startswith('<') and difference < n:
        exec(scriptDir+"/"+execFile)
    if condition.startswith('>') and difference > n:
        exec(scriptDir+"/"+execFile)
def capture(args):
    startX = int(args[0])
    startY = int(args[1])
    width = int(args[2])
    height = int(args[3])
    img = pyautogui.screenshot(region=[startX,startY,width,height])
    img.save("capture/"+str(int(time.time()))+".jpg")
scriptDir = "script"
scriptMainFile = scriptDir+"/main.ssjj"
def exec(filePath):
    file = open(filePath, "r",encoding="utf-8")
    step = 1
    for line in file.readlines():
        line = line.replace("\n", '')  # 除掉回车
        strs = line.split(' ')  # 分割内容
        action = strs[0]  # 要干的动作
        strs = strs[1:]  # 动作参数
        if line.startswith('#'):
            continue
        if action == "Sleep":
            Sleep(strs)
        elif action == "KeyDown":
            KeyDown(strs)
        elif action == "KeyUp":
            KeyUp(strs)
        elif action == "MouseDown":
            MouseDown(strs)
        elif action == "MouseUp":
            MouseUp(strs)
        elif action == "MouseMove":
            MouseMove(strs)
        elif action == "MouseAbsoluteMove":
            MouseAbsoluteMove(strs)
        elif action == "Import":
            exec(scriptDir+"/"+strs[0])
        elif action == "for":#执行脚本中的for循环
            for idx in range(int(strs[0])):
                exec(scriptDir+"/"+strs[1])
        elif action == "WhenSimilarity":
            WhenSimilarity(strs)
        elif action == "capture":
            capture(strs)
        else:
            print(filePath+"未知参数" + str(step) + "行")
        step += step
    file.close()
if __name__ == "__main__":
    print("开始执行脚本")
    while True:
        exec(scriptMainFile)