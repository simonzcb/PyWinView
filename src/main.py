import sys
from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from MainForm import Ui_MainWindow
from utils.FilePath import resource_path


class MainOP(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainOP, self).__init__()
        self.setupUi(self)

        self.maindata = {}

        self.maindata["date"] = self.dateEdit.text()
        self.maindata["date"] = datetime.strptime(self.maindata["date"], '%Y/%m/%d')
        self.dateEdit.dateChanged.connect(self.onDateChanged)

        act = QAction(self)  # 定义一个行为
        act.setIcon(QIcon(resource_path('resources/images/ic.png')))  # 设置行为icon，
        print(resource_path('resources/images/ic.png'))
        act.triggered.connect(self.wenjian)  # 绑定行为槽函数
        self.lineEdit_1.addAction(act, QLineEdit.TrailingPosition)  # 将该行为添加到lineEdit最右端

        act2 = QAction(self)  # 定义一个行为
        act2.setIcon(QIcon(resource_path('resources/images/ic.png')))  # 设置行为icon，
        act2.triggered.connect(self.outdir)  # 绑定行为槽函数
        self.lineEdit_2.addAction(act2, QLineEdit.TrailingPosition)  # 将该行为添加到lineEdit最右端

        self.convertBtn.clicked.connect(self.zhuanhuan)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(int(newLeft), int(newTop))

        # MainWindow= QMainWindow()
        # ui=MainForm.Ui_MainWindow()
        # ui.setupUi(MainWindow)
        # self.ui.showMsg.released.connect(onReleased,ui)

        # self.ui.pushButton.clicked.connect(functools.partial(convert, ui))

    def onDateChanged(self):
        self.maindata["date"] = datetime.strptime(self.dateEdit.text(), '%Y/%m/%d')

    def outdir(self):
        self.maindata["outPath"] = QFileDialog.getExistingDirectory(None, "输出文件夹", "C:/")  # 返回选中的文件夹路径
        # QFileDialog.getOpenFileName()  # 返回选中的文件路径
        # QFileDialog.getOpenFileNames()  # 返回选中的多个文件路径
        # QFileDialog.getSaveFileName()  # 存储文件

        self.lineEdit_2.setText((QtCore.QCoreApplication.translate("tile", self.maindata["outPath"])))
        print(self.maindata)

    def wenjian(self):
        self.maindata["wenjian"] = QFileDialog.getOpenFileName(None, "选取文件", "C:/", "CSV文件(*.csv)")
        # 返回选中的文件夹路径
        if (self.maindata["wenjian"][0] == ""):
            return
        self.maindata["wenjian"] = self.maindata["wenjian"][0]
        pathMixName = self.maindata["wenjian"].split('/')  # 将fn按照/切分
        pathx = "/".join(pathMixName[0:len(pathMixName) - 1])  # 假设切分后有n部分，将前n-1部分用/重新拼接，就是文件的路径
        namex = pathMixName[len(pathMixName) - 1]  # 最后一个就是文件名
        print(pathx, namex)
        self.maindata["wenjianname"] = namex
        self.lineEdit_1.setText(self.maindata["wenjian"])

        print(self.maindata)

    def zhuanhuan(self):
        print(self.maindata)

    # def convert(ui):
    #     input = ui.lineEdit.text()
    #     ui.opt_area.setText(input)
    #
    # def onReleased(self, object):
    #     QMessageBox.information(self, "提示信息", "来提升了")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainOP()
    window.center()
    window.show()
    # window.showMaximized()
    sys.exit(app.exec())
