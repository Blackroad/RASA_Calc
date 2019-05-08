from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import data.components



class MainApp(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Calculation App'
        self.window_width = 400
        self.window_high = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.window_width, self.window_high)

       #create list
        list_of_classes = QComboBox(self)
        list_of_classes.addItems(data.components.get_all_components())
        self.show()







if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_app = MainApp()
    sys.exit(app.exec_())