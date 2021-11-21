import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog


class AddEditForm(QDialog):
    def __init__(self, parent=None, is_edit: bool = False, coffee_id: int = 0):
        super().__init__(parent)
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.coffee_id = coffee_id

        cur = self.con.cursor()
        self.roastEdit.addItems(map(lambda x: str(x[0]), cur.execute("SELECT title FROM roast").fetchall()))
        self.grindingEdit.addItems(map(lambda x: str(x[0]), cur.execute("SELECT title FROM grinding").fetchall()))

        if is_edit:
            self.pushButton.clicked.connect(self.edit)
        else:
            self.pushButton.clicked.connect(self.add)

    def edit(self):
        cur = self.con.cursor()
        roast_id = cur.execute(f'SELECT id FROM roast '
                               f'WHERE title = "{self.roastEdit.currentText()}"').fetchall()[0][0]
        grinding_id = cur.execute(f'SELECT id FROM grinding '
                                  f'WHERE title = "{self.grindingEdit.currentText()}"').fetchall()[0][0]

        cur.execute(f'''UPDATE coffee_info SET sort = "{self.sortEdit.text()}", roast_id = {roast_id}, 
        grinding_id = {grinding_id}, description = "{self.descriptionEdit.text()}", price = {self.priceEdit.value()}, 
        size = {self.sizeEdit.value()} WHERE id = {self.coffee_id}''')

        self.con.commit()
        self.con.close()
        self.parentWidget().update_result()
        self.close()

    def add(self):
        cur = self.con.cursor()
        roast_id = cur.execute(f'SELECT id FROM roast '
                               f'WHERE title = "{self.roastEdit.currentText()}"').fetchall()[0][0]
        grinding_id = cur.execute(f'SELECT id FROM grinding '
                                  f'WHERE title = "{self.grindingEdit.currentText()}"').fetchall()[0][0]

        cur.execute(f'''INSERT INTO coffee_info(sort, roast_id, grinding_id, description, price, size)
        VALUES("{self.sortEdit.text()}", {roast_id}, {grinding_id}, 
        "{self.descriptionEdit.text()}", {self.priceEdit.value()}, {self.sizeEdit.value()})''')

        self.con.commit()
        self.con.close()
        self.parentWidget().update_result()
        self.close()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.update_result()

        self.pushButton.clicked.connect(self.add_event)
        self.pushButton_2.clicked.connect(self.edit_event)

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

    def add_event(self):
        add_form = AddEditForm(self)
        add_form.exec()

    def edit_event(self):
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]
        if ids:
            edit_form = AddEditForm(self, True, int(ids[0]))
            edit_form.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
