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

        self.pb_Convert.clicked.connect(self.run)
        self.le_InputValue.returnPressed.connect(self.run)

        
    def run(self):

        self.reload()
        self.input_validating()
        print(self.valid_amount)
        print(self.valid_currency)



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
                self.valid_amount = False
        
        

        #1000
        #1000,00
        #1000.00
        #1,000
        #1,000.00

    #CURRENCY SYMBOL SECTION
            
        currency_symbol = re.split("[0-9.,]", input_value)
            #potencial currency
        while "" in currency_symbol:
            currency_symbol.remove("")

        if len(currency_symbol) == 1:
            self.valid_currency = self.find_currency_by_symbol(currency_symbol)
        elif len(currency_symbol) > 1:
            self.valid_currency = False
           

    def find_currency_by_symbol(self, currency_symbol):
        # Function to find currency by symbol

        with open("test.json") as file:
            currency_data = json.load(file)

        for key, values in currency_data.items():

            if currency_symbol[0] in values:
                return key
            
        return False
            #if currency is not found




        

        
        

    ''''
    def is_input_valid(self):      #check if input value is valid, then call convert method
        
        self.l_Message.setText("Processing..")

        if self.input_value_mod().strip() == "":
            self.status_code = "empty_value"
        
        elif any(char.isdigit() for char in self.input_value_mod()) == False:
            self.status_code = "no_digit"

        else:
            try:
                self.convert_currency()
            except:
                self.status_code = "wrong_format"

        self.get_status()

      
    def input_value_mod(self):
        
        InputValue = self.le_InputValue.text().upper()
        InputValue = InputValue.replace("KČ", "CZK").replace("€", "EUR").replace("EURO", "EUR").replace("$", "USD")

        return InputValue

    
    def get_input_amount(self):

        InputValue = self.input_value_mod()

        if InputValue == "":
            self.status_code = "no_value"            

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

        
        """

        currencies = ["EUR", "USD", "CZK"]

        InputValue = self.input_value_mod()

        for curr in currencies:
            if InputValue.find(curr) >= 0:
                self.cb_InputCurrency.setCurrentText(curr)
                return curr  # Return the found currency (for the get_input_amount)

        return ""  # Return an empty string if no currency is found (I don't understand why that's necessary)

        
        InputValue = self.le_InputValue.text().upper()
        
        
    '''

        
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

        print(response.json())

        self.status_code = response.status_code
        result = response.json()

        output = round((result["data"][self.cb_OutputCurrency.currentText()]*float(self.get_input_amount())), 2)     #round[OutputCurr x InputAmount), 2]
        output = str(output) + " " + self.cb_OutputCurrency.currentText()       #just formating
        self.le_OutputValue.setText(str(output))

        self.le_InputValue.setFocus()

        self.get_status()


    def get_status(self):

        with open("error_codes.json") as error_codes:
            error_code = json.load(error_codes)

        self.l_Message.setText(f"{error_code[str(self.status_code)]} at {datetime.now().strftime("%H:%M:%S on %d. %m. %Y")}")








#####   NAME MAIN   #####

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    

    sys.exit(app.exec())