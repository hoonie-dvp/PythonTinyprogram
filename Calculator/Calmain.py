import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QPushButton


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Easy Calculator')
        self.setGeometry(300, 300, 800, 700)
        
        self.line_cal = QLineEdit(self)
        self.line_cal.setPlaceholderText('Enter your calculation here')
        self.line_cal.move(50, 50)
        self.line_cal.resize(600, 50)

        cal_btn = QPushButton('Calculate', self)
        cal_btn.move(650, 50)
        cal_btn.resize(150, 50)

        self.show()

    def Calmain(self):
        expr = self.line_cal.text()
    

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

