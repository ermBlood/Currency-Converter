import sys
import requests
import json
import re
from datetime import datetime
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Main.UI.main_window import Ui_mw_Main

class MainWindow(qtw.QWidget, Ui_mw_Main):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.status_code = None
        self.valid_amount = None
        self.valid_currency = None

        self.load_currencies_lists()

        self.pb_Convert.clicked.connect(self.run)
        self.le_InputValue.returnPressed.connect(self.run)

        
    def run(self):
        
        self.reload()
        self.input_validating()

        print(self.valid_amount)
        print(self.valid_currency)
        
        if (self.valid_amount != False) and (self.valid_currency != False):
            self.convert_currency()
        self.get_status()
            

    def reload(self):

        print("\nRELOAD\n")

        self.status_code = None
        self.valid_amount = None
        self.valid_currency = None

        self.le_InputValue.setFocus()

    
    def input_validating(self):

        input_value = self.le_InputValue.text().strip().replace(" ", "").upper()
        

    #AMOUNT SECTION
                
        input_amount = re.split("[^0-9.,]", input_value)

        while "" in input_amount:
            input_amount.remove("")

        if len(input_amount) == 1:
            self.valid_amount = input_amount[0]
        else:
            self.status_code = "invalid_amount"
            self.valid_amount = False


        if len(re.findall("[,.]", input_amount[0])) > 0:
        #is there any of [,.] ?

            #prevention to
            if len(re.findall(
                r"^[,.]|"                 # ,.1000
                r"[,.]$|"                 # 1000,.
                #r"[,.][0-9]{1}$|"         # 1,.0
                r"[.][0-9]{2}+[0-9]|"     # 1.000+
                r"[,][0-9]{3}+[0-9]|"     # 1,0000+
                r"[,.][,.]|"              # .. ,,
                r"[,.][0-9][,.]|"         # ,.0,.
                r"[,.][0-9]{2}[,.]|"      # ,.00,.
                r"[.].+[,.]|"             # .+.,
                r"[,].+[,][0-9]{1}$|"     # 1,000,0
                r"[,].+[,][0-9]{2}$|"     # 1,000,00
                r"[0-9]{4},[0-9]{2}+[0-9]"# 1000,000
                , input_amount[0])) > 0:
                self.status_code = "invalid_amount"
                self.valid_amount = False
        

    #CURRENCY SYMBOL SECTION
            
        currency_symbol = re.split("[0-9.,]", input_value)
            #potencial currency
        
        while "" in currency_symbol:
            currency_symbol.remove("")

        if len(currency_symbol) == 1:
            #if potencial currency detected            
            self.valid_currency = self.find_currency_by_symbol(currency_symbol)
            if self.valid_currency != False:
                self.cb_InputCurrency.setCurrentIndex(self.cb_OutputCurrency.findText(self.valid_currency))
                #set right item currency into input combo box

        elif len(currency_symbol) > 1:
            self.valid_currency = False

        if self.valid_currency == None:
            self.valid_currency = self.cb_InputCurrency.currentText()
           

    def find_currency_by_symbol(self, currency_symbol):
        # Function to find currency by symbol

        with open("supported_currencies.json", encoding="utf-8") as file:
            currency_data = json.load(file)

        for key, value in currency_data.items():
            symbols = value["symbols"]
            if currency_symbol[0] in symbols:
                return key

        self.status_code = "invalid_currency"    
        return False
            #if currency is not found


    def valid_amount_formating(self):

        formated_amount = self.valid_amount

        #if one "," is there and not as floating point, replace it with "."
        if len(re.findall("[,]", formated_amount)) == 1 and (len(re.findall("[,][0-9]{1}$|[,][0-9]{2}$", formated_amount)) == 1):
            formated_amount = formated_amount.replace(",", ".")
        
        #if "," still there, delete it
        if len(re.findall("[,]", formated_amount)) > 0:
            formated_amount = formated_amount.replace(",", "")

        return formated_amount

     
    def convert_currency(self):

        headers= {"apikey": "fca_live_DFWRlBKAKDksrqpckRt7d1wCqtmX3cJy4nkng6xg"}
        payload = {}

        url = f"https://api.freecurrencyapi.com/v1/latest?apikey={headers["apikey"]}&\
            currencies={self.cb_OutputCurrency.currentText()}&base_currency={self.valid_currency}"

        response = requests.request("GET", url, headers=headers, data = payload)

        print(response)
        print(response.json())

        self.status_code = response.status_code
        result = response.json()

        output = round((result["data"][self.cb_OutputCurrency.currentText()]*float(self.valid_amount_formating())), 2)
        #round[OutputCurrAmount x InputAmount), 2]
        output = str(output) + " " + self.cb_OutputCurrency.currentText()
        #just formating
        self.le_OutputValue.setText(str(output))

        
    def get_status(self):

        with open("error_codes.json") as error_codes:
            error_code = json.load(error_codes)

        self.l_Message.setText(f"{error_code[str(self.status_code)]} at {datetime.now().strftime("%H:%M:%S on %d. %m. %Y")}")


    def load_currencies_lists(self):

        with open("supported_currencies.json", encoding="utf-8") as file:
            currency_data = json.load(file)

        for key, value in currency_data.items():
            self.cb_InputCurrency.addItem(key)
            self.cb_OutputCurrency.addItem(key)
        
        self.cb_OutputCurrency.setCurrentIndex(1)





#####   NAME MAIN   #####

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    

    sys.exit(app.exec())