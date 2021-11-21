import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import QRectF
from UI import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)
        self.count = 3

    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        for i in range(self.count):
            pen = QPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)), 5)
            qp.setPen(pen)
            r = randint(50, 100)
            rect = QRectF(randint(0, self.width() - r), randint(0, self.height() - r), r, r)
            qp.drawEllipse(rect)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
