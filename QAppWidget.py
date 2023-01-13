from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#from qtdownloader import QDownloadDialog
import os,sys,requests

class QtDownloadThreading_class(QThread):
    sinOut = pyqtSignal(int)
    def __init__(self,url,filepath,apptype):
        super().__init__()
        self.url=url
        self.filepath=sys.path[0]+"/"+filepath+"."+apptype

    def run(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
        self.headdata=requests.head(url=self.url,headers=self.headers)
        self.size = int(self.headdata.headers.get('Content-Length'))
        self.data=requests.get(self.url, headers=self.headers, stream=True)
        if self.size<4194304:self.chunk=2048*1#4M
        elif self.size<16777216:self.chunk=2048*4#16M
        elif self.size<67108864:self.chunk=2048*16#64M
        elif self.size<268435456:self.chunk=2048*64#256M
        elif self.size<1073741824:self.chunk=2048*256#1GB
        elif self.size<4294967296:self.chunk=2048*1024#4GB
        else: self.chunk=2048*4096
        self.tmpi=0
        with open(self.filepath, mode='wb') as f:
            print(self.chunk)
            for x in self.data.iter_content(chunk_size=self.chunk):
                f.write(x)
                self.tmpi+=self.chunk
                self.sinOut.emit(int((self.tmpi/self.size)*100))
        os.system("explorer "+sys.path[0])


class QAppWidget(QWidget):
    def __init__(self,appname,packagename,retail,downloadlink,apptype):
        super().__init__()
        self.grid=QGridLayout()
        self.appname,self.packagename,self.retail,self.downloadlink,self.apptype=appname,packagename,retail,downloadlink,apptype
        self.setLayout(self.grid)
        self.download=QtDownloadThreading_class(downloadlink,packagename,apptype)
        self.ui()
    def ui(self):
        pass
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
        self.headdata=requests.head(url=self.downloadlink,headers=self.headers)
        self.xsize = int(self.headdata.headers.get('Content-Length'))
        if self.xsize<1024:self.size=self.xsize
        elif self.xsize<1048576:self.size="%.2fKB" % float(self.xsize/1024)
        elif self.xsize<1073741824:self.size="%.2fMB" % float(self.xsize/1048576)
        else:self.size="%.2fGB" % float(self.xsize/1073741824)
        self.iconlabel=QLabel()
        self.iconlabel.setPixmap(QPixmap(f"{sys.path[0]}/data/{self.packagename}"))#.scaled(128,128)
        self.iconlabel.setFixedSize(128,128)
        self.iconlabel.setScaledContents(True)
        self.grid.addWidget(self.iconlabel,0,0,4,4)
        self.grid.addWidget(QLabel("<b style=\"font-size:14pt\">"+self.appname+"</b>"+"        大小："+self.size+"        包名："+self.packagename+"        格式："+self.apptype),0,4,1,1)
        if len(self.retail)<=50:self.rretail=self.retail+"  "*(50-len(self.retail))
        else:self.rretail=self.retail[:47]+"…"
        self.retaillabel=QLabel(self.rretail)
        self.grid.addWidget(self.retaillabel,1,4)
        self.prog=QProgressBar()
        self.grid.addWidget(self.prog,2,4)
        self.button=QPushButton("下载")
        self.button.clicked.connect(self.slotStart)
        self.download.sinOut.connect(self.slotAdd)
        self.grid.addWidget(self.button,3,4)

    def slotAdd(self,i):
        self.button.setEnabled(False)
        self.prog.setValue(i)
        if i>=100:
            self.prog.setValue(100)
            QMessageBox.information(QWidget(),"信息","下载完成",QMessageBox.Ok)
    def slotStart(self):self.download.start()
