# 生死狙击挂机脚本

这是一个生死狙击的挂机脚本,需要你在script文件夹下编写你的动作

* 目前脚本可支持操作

```
Sleep [暂停秒数]
KeyDown [按什么键] 
KeyUp [松开什么键]
MouseDown [按下鼠标LEFT或RIGHT]
MouseUp [松开鼠标LEFT或RIGHT]
MouseMove [相对移动X坐标] [相对移动Y坐标]
MouseAbsoluteMove [绝对移动X坐标] [绝对移动Y坐标]
WhenSimilarity [相似度判断条件] [匹配图片位置] [执行的脚本文件] #用于在指定图片跟屏幕相似的情况下执行指定脚本
Import [脚本文件] #用于引入操作的模块
capture [屏幕截图起始X坐标] [屏幕截图起始Y坐标] [屏幕截图截止X坐标] [屏幕截图截止Y坐标]
for [执行次数] [脚本文件] #循环执行脚本文件
```

* 注:脚本里已经有工业7的挂机脚本和工业区急速脚本,使用工业区急速脚本需要翎羽,工业7需要破空

~~但是工业7视乎不太稳定的亚子,网络波动都会造成时间错轴(0v0)~~

*使用方法

如果你要运行脚本

```
python ssjjScript.py
```

如果你想获取屏幕上的某点坐标

```
python getMousePoint.py
```