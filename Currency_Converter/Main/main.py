import sys
import requests
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Main.UI.main_window import Ui_mw_Main

class MainWindow(qtw.QWidget, Ui_mw_Main):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_Convert.clicked.connect(self.convert_currency)

        
    def convert_currency(self):

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={self.cb_OutputCurrency.currentText()}&from={self.cb_InputCurrency.currentText()}&amount={self.le_InputAmount.text()}"

        payload = {}
        headers= {
        "apikey": "TVeSAhOa6ota8Hv0rUuU1jCPTNkEaFdV"
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        status_code = response.status_code
        result = response.json()

        output = round(result["result"], 2)

        self.le_OutputAmount.setText(str(output))










#####   NAME MAIN   #####

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    

    sys.exit(app.exec())