from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidget
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QComboBox, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from PIL import Image
import sqlite3
import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('coffe.ui', self)
        self.b = sqlite3.connect("Coffee.db")
        self.cur = self.b.cursor()

        self.result = self.cur.execute('''SELECT * FROM Cofeok''').fetchall()
        print(self.result)

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                                                    'описание вкуса', 'цена', 'объем упаковки'])
        for i in range(len(self.result)):
            for j in range(7):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.result[i][j])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
