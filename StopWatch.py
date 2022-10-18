from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5 import QtCore,QtGui 
import sys
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stopwatch')
        self.setGeometry(100,100,500,500)
        self.UiComponents()
        self.show()
    def UiComponents(self):
        self.count=0
        self.flag = False
        self.label= QLabel(self)
        self.label.setGeometry(100,50,300,250)
        self.label.setText(str(self.count))
        self.label.setFont(QFont('Verdana',30))
        self.label.setStyleSheet("border : 6px solid black")
        self.label.setAlignment(Qt.AlignCenter)
        start = QPushButton("Start",self)
        start.setGeometry(180,320,150,50)
        start.pressed.connect(self.Start)
        start = QPushButton("Pause",self)
        start.setGeometry(180,370,150,50)
        start.pressed.connect(self.Pause)
        start = QPushButton("Reset",self)
        start.setGeometry(180,420,150,50)
        start.pressed.connect(self.Reset)
        timer= QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(100)
        #class - helps make out a blueprint of the applications to complete it
        #object- instance of class, without it the class wont run
        #constructor- it is to be called on its own, __init__ is its identity, and works only after the objects loads finally!!
    def showtime(self):
        if self.flag:
            self.count+=1
            text= str(self.count/10)
            self.label.setText(text)
    def Start(self):
        self.flag= True
    def Pause(self):
        self.flag= False
    def Reset (self):
        self.flag = False
        self.count =0
        self.label.setText(str(0))
App = QApplication(sys.argv)
window= Window()
sys.exit(App.exec())
