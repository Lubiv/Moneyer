import pandas as pd
from Transaction import *
from datetime import date

class Balance:

    def __init__(self, arg):
        if isinstance(arg, float):
            self.balance = pd.DataFrame({"title": "initial", "amount": [arg], "isExpense": "", "dateTime": ""})
        elif isinstance(arg, str):
            self.load(arg)


    def save(self):
        self.balance.to_csv('%s.csv' % date.today().strftime("%m-%y"), index = False)

    def load(self, path):        
        self.balance = pd.read_csv(path)

    def add(self, transaction):
        self.balance.loc[len(self.balance.index)] = transaction.as_dict()