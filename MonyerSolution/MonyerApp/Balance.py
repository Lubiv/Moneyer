import pandas as pd
from Transaction import *

class Balance:

    def __init__(self, initial):
        self.balance = pd.DataFrame({"title": "initial", "amount": [initial], "isExpense": "", "dateTime": ""})

    def save(self):
        self.balance.to_csv('test.csv', index = False)

    def load(self, path):        
        self.balance = pd.read_csv(path)

    def add(self, transaction):
        self.balance.loc[len(self.balance.index)] = transaction.as_dict()