import sys
from PyQt4 import QtGui

class MyForm(QtGui.QWidget):

	def __init__(self):
		super(MyForm, self).__init__()

		lbl = QtGui.QLabel('My First UI Element!', self)




app = QtGui.QApplication(sys.argv)
mainWindow = MyForm()
status = app.exec_()
sys.exit(status)