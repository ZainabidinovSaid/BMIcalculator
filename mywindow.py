import os
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QPushButton,QLabel

class BMIcalculator(QMainWindow):
   def __init__(self):
       super().__init__()
       self.input1 = QLineEdit(self)
       self.input2 = QLineEdit(self)
       self.label3 = QLabel(self)
       self.button1 = QPushButton(self)

       ui_path = os.path.join(os.path.dirname(__file__), "bmicalculator.ui")
       uic.loadUi(ui_path, self)
       self.button1.clicked.connect(self.calculate_bmi)

   def calculate_bmi(self):
       try:
           weight = float(self.input1.text())
           height = float(self.input2.text()) / 100  # Convert cm to meters
           bmi = weight / (height ** 2)

           # Set text and color based on BMI category
           if bmi < 18.5:
               self.label3.setStyleSheet("background-color: yellow; font-weight: bold;")
               category = "Underweight"
           elif 18.5 <= bmi < 25:
               self.label3.setStyleSheet("background-color: green; color: white; font-weight: bold;")
               category = "Normal weight"
           elif 25 <= bmi < 30:
               self.label3.setStyleSheet("background-color: orange; color: white; font-weight: bold;")
               category = "Overweight"
           else:
               self.label3.setStyleSheet("background-color: red; color: white; font-weight: bold;")
               category = "Obese"

           self.label3.setText(f"BMI: {bmi:.1f} ({category})")
       except ValueError:
           self.label3.setText("Invalid Input")
           self.label3.setStyleSheet("background-color: lightgray;")