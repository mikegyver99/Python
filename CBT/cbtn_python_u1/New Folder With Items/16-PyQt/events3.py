import sys
from PyQt4 import QtGui

class MyForm(QtGui.QWidget):
	
	def __init__(self):
		super(MyForm, self).__init__()
		vbox = QtGui.QVBoxLayout()

		self.lcd = QtGui.QLCDNumber()

		slider = QtGui.QSlider()
		slider.valueChanged.connect(self.lcd.display)

		vbox.addWidget(self.lcd)
		vbox.addWidget(slider)
	

		self.setLayout(vbox)
		self.setGeometry(300,300,250,150)
		self.setWindowTitle('My Form')
		self.show()


app = QtGui.QApplication(sys.argv)
mainWindow = MyForm()
status = app.exec_()
sys.exit(status)