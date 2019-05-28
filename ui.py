from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QLineEdit, QCheckBox, QLabel, QGroupBox, QHBoxLayout, QFormLayout, QMainWindow
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import pyqtSlot, QRect, QCoreApplication
import inspect
from core import Veriables_Calculation, get_all_components
from data import components


class MainApp(QWidget):

    def __init__(self):
        super().__init__()
        # attributes for sub-initialization in iniUI
        self.list_of_classes = None
        self.dot_value = None
        self.width_value = None
        self.signed = None
        self.x_min, self.x_mid, self.x_max = None, None, None
        self.y_result1, self.y_result2, self.y_result3 = None, None, None

        # main class atributes
        self.setObjectName('Window')
        self.title = 'Calculation App'
        self.window_width = 350
        self.window_high = 300
        self.initUI()
        self.show()

    def initUI(self):
        # buttons
        self.setWindowTitle(self.title)
        self.setFixedSize(self.window_width, self.window_high)
        calculate_button = QPushButton(self)
        exit_button = QPushButton(self)
        calculate_button.setText('Calculate')
        exit_button.setText('Exit')
        group_calc_exit = QGroupBox(self)
        h_box = QHBoxLayout(self)
        h_box.addWidget(calculate_button)
        h_box.addWidget(exit_button)
        group_calc_exit.setLayout(h_box)
        group_calc_exit.setGeometry(QRect(10, 250, 330, 40))

        # sub-initialize list of classes
        self.list_of_classes = QComboBox(self)
        self.list_of_classes.setGeometry(140, 20, 200, 25)
        self.list_of_classes.addItems(get_all_components(components))

        # sub-initialize dot
        self.dot_value = QLineEdit(self)
        self.dot_value .setPlaceholderText('Dot')
        self.dot_value .setValidator(QIntValidator(1, 10))
        self.dot_value .setGeometry(10, 20, 100, 25)

        # sub-initialize width
        self.width_value = QLineEdit(self)
        self.width_value.setPlaceholderText('Width')
        self.width_value.setValidator(QIntValidator(1, 10))
        self.width_value.setGeometry(10, 60, 100, 25)

        # sub-initialize signed
        self.signed = QCheckBox(self)
        signed_label = QLabel(self)
        signed_label.setGeometry(30, 95, 90, 25)
        signed_label.setText('Signed/Unsigned')
        self.signed.setTristate(on=False)
        self.signed.setGeometry(10, 100, 15, 15)
        self.signed.setCheckState(0)

        # sub-initialize x-values
        self.x_min = QLineEdit(self)
        self.x_min.setReadOnly(True)
        self.x_mid = QLineEdit(self)
        self.x_mid.setReadOnly(True)
        self.x_max = QLineEdit(self)
        self.x_max.setReadOnly(True)
        result_box = QGroupBox(self)
        result_box.setTitle('X-values')
        vbox = QFormLayout(self)
        r1 = QRect(10, 120, 120, 120)
        vbox.addRow('&XMIN', self.x_min)
        vbox.addRow('&XMID', self.x_mid)
        vbox.addRow('&XMAX', self.x_max)
        result_box.setGeometry(r1)

        # sub initialize y-values
        self.y_result1 = QLineEdit(self)
        self.y_result1.setReadOnly(True)
        self.y_result2 = QLineEdit(self)
        self.y_result2.setReadOnly(True)
        self.y_result3 = QLineEdit(self)
        self.y_result3.setReadOnly(True)
        y_box = QGroupBox(self)
        y_box.setTitle('Y-values')
        yv_box = QFormLayout(self)
        y_box.setGeometry(QRect(140, 120, 200, 120))
        yv_box.addRow('Y for X_MIN', self.y_result1)
        yv_box.addRow('Y for X_MID', self.y_result2)
        yv_box.addRow('Y for X_MAX', self.y_result3)
        result_box.setLayout(vbox)
        y_box.setLayout(yv_box)

        # clicked actions
        exit_button.clicked.connect(self.exit)
        calculate_button.clicked.connect(self.calculate)

    @pyqtSlot()
    def calculate(self):
        if self.width_value.text() is not '':
            result = Veriables_Calculation().get_width_variable(width=int(self.width_value.text()), signed=bool(self.signed.checkState()))
            if self.list_of_classes.currentText() == 'Not selected':
                self.x_min.setText(str(result['x_min']))
                self.x_mid.setText(str(result['x_mid']))
                self.x_max.setText(str(result['x_max']))
            else:
                # TODO Handle exception when dot == NONE
                for name, obj in (inspect.getmembers(components, inspect.isclass)):
                    if self.list_of_classes.currentText() == name:
                        y = obj().calculations(result, int(self.dot_value.text()))
                        self.x_min.setText(str(result['x_min']))
                        self.x_mid.setText(str(result['x_mid']))
                        self.x_max.setText(str(result['x_max']))
                        self.y_result1.setText(str(y[0]))
                        self.y_result2.setText(str(y[1]))
                        self.y_result3.setText(str(y[2]))
        else:
            pass

    @pyqtSlot()
    def exit(self):
        QCoreApplication.instance().quit()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_app = MainApp()
    sys.exit(app.exec_())
