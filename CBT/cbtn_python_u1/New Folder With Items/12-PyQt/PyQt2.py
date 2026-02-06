import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

w = QtGui.QWidget()
w.resize(250,150)
w.move(300,300)
w.setWindowTitle('My First GUI App!')
w.setToolTip("This is the tooltip")
w.show()

w2 = QtGui.QWidget()
w2.show()

status = app.exec_()
sys.exit(status)