import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from iFlyForm import Ui_iFlyForm
from PyQt5.QtGui import QIcon

from utils.FilePath import resource_path


class IFlyController(QMainWindow, Ui_iFlyForm):
    def __init__(self):
        super(IFlyController, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("iFly...")
        self.setWindowIcon(QIcon(resource_path("resources/images/fly.png")))
        self.status=self.statusBar();
        self.status.showMessage("这是消息",5000)
        # self.showMaximized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path("resources/images/fly.png")))

    window = IFlyController()
    window.showMaximized()
    app.exec()
    # sys.exit()
