import sys
from PySide import QtGui, QtCore

class Display(QtGui.QWidget):

 def __init__(self):
 
  super(Display, self).__init__()
  self.initUI()

 def initUI(self):
  self.lcd = QtGui.QLCDNumber(self)
  
  box = QtGui.QVBoxLayout()
  box.addWidget(self.lcd)
  
  self.setLayout(box)
  self.time=0
  self.timer = QtCore.QBasicTimer()
  self.timer.start(1000, self)
  self.show()
  
 def timerEvent(self, e):
  self.time = self.time + 1
  self.lcd.display(self.time)
  
def main():
 app = QtGui.QApplication(sys.argv)
 ex = Display()
 sys.exit(app.exec_())
 
if __name__=='__main__':
 main() 
