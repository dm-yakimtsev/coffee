import sys
from ui import Ui_Form
import sqlite3
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem


class Coffee(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.load_table)

    def load_table(self):
        con = sqlite3.connect("coffee_db.sqlite")
        cur = con.cursor()
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.tableWidget.setColumnCount(
            self.tableWidget.columnCount() + 1)
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("name"))
        self.tableWidget.setColumnCount(
            self.tableWidget.columnCount() + 1)
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("roasting"))
        self.tableWidget.setColumnCount(
            self.tableWidget.columnCount() + 1)
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("ground/grains"))
        self.tableWidget.setColumnCount(
            self.tableWidget.columnCount() + 1)
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("discription"))
        self.tableWidget.setColumnCount(
            self.tableWidget.columnCount() + 1)
        self.tableWidget.setHorizontalHeaderItem(5, QTableWidgetItem("cost"))
        self.tableWidget.setColumnCount(
            self.tableWidget.columnCount() + 1)
        self.tableWidget.setHorizontalHeaderItem(6, QTableWidgetItem("volume"))

        result = cur.execute("""SELECT * FROM coffee""").fetchall()

        for i, row in enumerate(result):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
