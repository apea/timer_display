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
  self.setGeometry(300, 300, 290, 150)
  self.time=0
  self.timer = QtCore.QBasicTimer()
  self.timer.start(1000, self)
  self.show()
  
 def timerEvent(self, e):
  self.time = self.time + 1
  self.lcd.display(self.showTime())
  
 def showTime(self):
  self.sec = self.time%60
  self.min = self.time//60
  
  if self.min < 10 and self.min > 0:
   self.showmin = '0' + str(self.min)
  elif self.min == 0:
   self.showmin = "00"
  else:  
   self.showmin = str(self.min)
  
  if self.sec < 10 and self.sec > 0:
   self.showsec = '0' + str(self.sec)
  elif self.sec == 0:
   self.showsec = "00" 
  else:  
   self.showsec = str(self.sec)
   
  self.show = self.showmin + ':' + self.showsec
  
  return self.show
  
def main():
 app = QtGui.QApplication(sys.argv)
 ex = Display()
 sys.exit(app.exec_())
 
if __name__=='__main__':
 main() 
