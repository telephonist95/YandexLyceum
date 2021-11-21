import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.update_result()

    def update_result(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT coffee_info.id, coffee_info.sort, roast.title, "
                             "grinding.title, coffee_info.description, coffee_info.price, coffee_info.size "
                             "FROM coffee_info "
                             "INNER JOIN grinding ON coffee_info.grinding_id = grinding.id "
                             "INNER JOIN roast ON coffee_info.roast_id = roast.id").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        titles = ("id", "сорт", "степень обжарки", "помолка", "описание", "цена", "объём")
        self.tableWidget.setHorizontalHeaderLabels(titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
