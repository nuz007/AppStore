from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from QAppWidget import QAppWidget
import os,sys
app=QApplication(sys.argv)
q1=QAppWidget("ZYH文件加密神器","com.zyh.crypter","目前只能下载1.0版本。一款能够轻松加密文件夹,保护您的数据安全。2.0更新内容:※1、可以主动设置密码 ※2、优化用户界面 ※3、去除encryptkey文件机制 ※4、解决了程序不完全退出的问题","https://zyhos.github.io/8bd8.github.io/app/crypt-linux-1.0.deb","deb")
q2=QAppWidget("QQ For Linux","linuxqq","腾讯QQ linux3.0 似乎现在开放了，任何人都可以登陆公测群号：664124315","https://mirrors.sdu.edu.cn/spark-store-repository//store/chat/linuxqq/linuxqq_3.0.0-571_amd64.deb","deb")
q3=QAppWidget("QQ For Linux","linuxqq","腾讯QQ linux3.0 似乎现在开放了，任何人都可以登陆公测群号：664124315","https://dldir1.qq.com/qqfile/qq/QQNT/c005c911/linuxqq_3.0.0-571_x86_64.rpm","rpm")
q4=QAppWidget("QQ For Linux","linuxqq","腾讯QQ linux3.0 似乎现在开放了，任何人都可以登陆公测群号：664124315","https://dldir1.qq.com/qqfile/qq/QQNT/c005c911/linuxqq_3.0.0-571_x86_64.AppImage","AppImage")
q5=QAppWidget("微信 Windows最新版","WechatSetup","微信，是一个生活方式。","https://dldir1.qq.com/weixin/Windows/WeChatSetup.exe","exe")
q6=QAppWidget("微信 苹果最新版","WechatMac","微信，是一个生活方式。","https://dldir1.qq.com/weixin/mac/WeChatMac.dmg","dmg")



window=QWidget()
vbox=QVBoxLayout()
window.setLayout(vbox)
vbox.addWidget(q1)
vbox.addWidget(q2)
vbox.addWidget(q3)
vbox.addWidget(q4)
vbox.addWidget(q5)
vbox.addWidget(q6)
window.show()

os._exit(app.exec())