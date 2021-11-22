# ssjj挂机脚本

这是一个很简单的ssjj的挂机脚本,需要你在script文件夹下编写你的动作

~~其实你也可以编写自己的Python脚本~~

* 目前脚本可支持操作

```
Sleep [暂停秒数]
KeyDown [按什么键] 
KeyUp [松开什么键]
MouseDown [按下鼠标LEFT或RIGHT]
MouseUp [松开鼠标LEFT或RIGHT]
MouseMove [相对移动X坐标] [相对移动Y坐标]
MouseAbsoluteMove [绝对移动X坐标] [绝对移动Y坐标]
WhenSimilarity [相似度判断条件] [匹配图片位置] [执行的脚本文件] [循环匹配多少秒] #用于在指定图片跟屏幕相似的情况下执行指定脚本,匹配图片默认在similarity
Import [脚本文件] #用于引入操作的模块
capture [屏幕截图起始X坐标] [屏幕截图起始Y坐标] [屏幕截图图片X轴长度] [屏幕截图图片Y轴长度] #截图后在capture文件夹下
for [执行次数] [脚本文件] #循环执行脚本文件
```

* 注:脚本里已经有工业7的挂机脚本和工业区急速脚本,使用工业区急速脚本需要翎羽,工业7需要破空,请根据自己的伤害以及武器调整,有宙斯的话那必须爽爽的!!!也用不着转向了

使用此脚本请选择一个良好的网络环境!!!否则掉线会引起时间错轴!!!

*使用方法

如果你要运行脚本

```
python ssjjScript.py
```

如果你想获取屏幕上的某点坐标

```
python getMousePoint.py
```