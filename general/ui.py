from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QTextEdit, QLineEdit, QCheckBox, QLabel, QGroupBox, QVBoxLayout, QGridLayout, QFormLayout
from PyQt5.QtGui import QIcon, QValidator, QIntValidator
from PyQt5.QtCore import pyqtSlot, QRect, QPoint
import data.components


class MainApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName('Window')
        self.title = 'Calculation App'
        self.window_width = 400
        self.window_high = 300
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.window_width, self.window_high)

        # list of classes
        # list_of_classes = QComboBox(self)
        # list_of_classes.setGeometry(10, 120, 120, 25)
        # list_of_classes.addItems(data.components.get_all_components())
        # dot
        dot_value = QLineEdit(self)
        dot_value.setPlaceholderText('Dot')
        dot_value.setValidator(QIntValidator(1, 10))
        dot_value.setGeometry(10, 20, 100, 25)

        # width
        width_value = QLineEdit(self)
        width_value.setPlaceholderText('Width')
        width_value.setValidator(QIntValidator(1, 10))
        width_value.setGeometry(10, 60, 100, 25)

        # signed
        signed = QCheckBox(self)
        signed_label = QLabel(self)
        signed_label.setGeometry(30, 95, 90, 25)
        signed_label.setText('Signed/Unsigned')
        signed.setTristate(on=False)
        signed.setGeometry(10, 100, 15, 15)
        signed.setCheckState(0)

        #result

        x_min = QLineEdit(self)
        x_min.setReadOnly(True)
        x_mid = QLineEdit(self)
        x_mid.setReadOnly(True)
        x_max = QLineEdit(self)
        x_max.setReadOnly(True)
        result_box = QGroupBox(self)
        result_box.setTitle('Results')
        vbox = QFormLayout(self)
        r1 = QRect(10, 140, 140, 120)
        vbox.addRow('&XMIN', x_min)
        vbox.addRow('&XMID', x_mid)
        vbox.addRow('&XMAX', x_max)
        result_box.setGeometry(r1)

        result_box.setLayout(vbox)











if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_app = MainApp()
    sys.exit(app.exec_())
