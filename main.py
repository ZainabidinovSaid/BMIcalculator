import sys
from PyQt6.QtWidgets import QApplication
from mywindow import BMIcalculator

if __name__ == "__main__":
   app = QApplication(sys.argv)
   window = BMIcalculator()
   window.show()
   app.exec()