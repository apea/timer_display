import sys
import time
import os
from PySide import QtGui, QtCore

class Timer:

 def __init__(self):
 
  self._timeOrigin = time.time()
  self.comppt = int(self._timeOrigin-time.time())

class Display(QtGui.QWidget):

 def __init__(self):
 
  super(Display, self).__init__()

  self.initUI()

 def initUI(self):
 
  lcd = QtGui.QLCDNumber(self)
  
  box = QtGui.QVBoxLayout()
  box.addWidget(lcd)
  
  self.setLayout(box)

  timer_display=Timer()
  self.show()
  
def main():

 app=QtGui.QApplication(sys.argv)
 ex=Display()
 sys.exit(app.exec_())
 
if __name__=='__main__':
 main() 