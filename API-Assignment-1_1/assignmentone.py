# This Python file uses the following encoding: utf-8
import sys
import json
import requests
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader
# import partial
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
# from ui_form import Ui_AssignmentOne

class AssignmentOne(QWidget):
    def __init__(self):
        super(AssignmentOne, self).__init__()
        loader = QUiLoader()
        self.ui=loader.load('D:/Python-For-Deployment-course/assignments/Assignment_1/form.ui')
        self.ui.show()
        
        self.m=["mashhad", "tehran", "khorammabad", "tabriz", "shiraz"]
        
        self.ui.btn_1.clicked.connect(self.weather)
        
    def weather(self):
        a= self.ui.Board.text()
        for i in self.m:
            
            if a==self.m[0]:
                response = requests.get("https://goweather.herokuapp.com/weather/Mashhad")
                report =json.loads(response.text)
                # report = {'temperature': '17 °C',
                #             'wind': '11 km/h',
                #             'description': 'Partly cloudy',
                #             'forecast': [{'day': '1', 'temperature': '+14 °C', 'wind': '24 km/h'},
                #             {'day': '2', 'temperature': '+9 °C', 'wind': '15 km/h'},
                #             {'day': '3', 'temperature': '+11 °C', 'wind': '17 km/h'}]}
                weather_report_1 = "temp:" " " + report["temperature"]
                weather_report_2 = "sky:"" " + report["description"] 
                weather_report_3 = "wind:"" " + report["wind"]   
                self.ui.lineEdit.setText(str(weather_report_1))
                self.ui.lineEdit_2.setText(str(weather_report_2))
                self.ui.lineEdit_3.setText(str(weather_report_3))
            else: 
                self.ui.Board.setText(str('این که شهر  نیست داااش'))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = AssignmentOne()
    
    sys.exit(app.exec())
