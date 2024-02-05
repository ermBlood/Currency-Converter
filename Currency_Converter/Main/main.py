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

        self.le_InputValue.setFocus()

        
    def input_value_mod(self):
        
        InputValue = self.le_InputValue.text().upper()
        InputValue = InputValue.replace("KČ", "CZK").replace("€", "EUR").replace("EURO", "EUR").replace("$", "USD")

        return InputValue

    
    def get_input_amount(self):

        InputValue = self.input_value_mod()

        if self.is_currency_in_input():  # Remove the unnecessary self argument here (??? chat GPT, what???)
            InputValue = InputValue.replace(self.get_input_currency(), "")    # remove currency from it

        if InputValue.count("."):  # format US currency notation - remove ","
            InputValue = InputValue.replace(",", "")
            
        if "," in InputValue:
            if len(InputValue[InputValue.index(",")+1:]) >= 3 and InputValue[InputValue.index(",")+1:InputValue.index(",")+4].isdigit():        # 1,000 to 1000
                InputValue = InputValue.replace(",", "")

        InputValue = InputValue.replace(",", ".")  # format CZK(etc) currency notation - replace "," with "."
        InputValue = InputValue.replace(" ", "")  # remove spaces

        return InputValue
    

    def is_currency_in_input(self):

        InputValue = self.le_InputValue.text().upper().replace(".", "").replace(",", "")
        return not InputValue.isdigit()
    

    def get_input_currency(self):

        currencies = ["EUR", "USD", "CZK"]

        InputValue = self.input_value_mod()

        for curr in currencies:
            if InputValue.find(curr) >= 0:
                self.cb_InputCurrency.setCurrentText(curr)
                return curr  # Return the found currency (for the get_input_amount)

        return ""  # Return an empty string if no currency is found (I don't understand why that's necessary)

        
    def convert_currency(self):

        if self.is_currency_in_input():
            self.get_input_currency()

        url = f"https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_DFWRlBKAKDksrqpckRt7d1wCqtmX3cJy4nkng6xg&currencies={self.cb_OutputCurrency.currentText()}&base_currency={self.cb_InputCurrency.currentText()}"

        payload = {}
        headers= {
        "apikey": "fca_live_DFWRlBKAKDksrqpckRt7d1wCqtmX3cJy4nkng6xg"
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        print(response)

        status_code = response.status_code
        result = response.json()

        output = round((result["data"][self.cb_OutputCurrency.currentText()]*float(self.get_input_amount())), 2)     #round[OutputCurr x InputAmount), 2]
        output = str(output) + " " + self.cb_OutputCurrency.currentText()       #just formating
        self.le_OutputValue.setText(str(output))


        self.l_Message.setNum(status_code)      #Error code
        









#####   NAME MAIN   #####

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    

    sys.exit(app.exec())