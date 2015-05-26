from PyQt5 import QtWidgets

from UiControllers import UiMainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = UiMainWindow()
    window.show()
    app.exec_()
