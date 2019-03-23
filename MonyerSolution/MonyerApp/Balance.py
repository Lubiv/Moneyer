import pandas as pd
from Transaction import *

class Balance:

    def __init__(self, transactions, initial):
        self.balance = pd.DataFrame({"title": "initial", "amount": initial, "isExpense": "", "dateTime": ""})

        for i in range(transactions.count):
            self.balance.loc[1 + i] = transactions[i].as_dict();

        
    def save(self):
        balance.to_csv('test.csv');

    def load(self):        
        return pd.read_csv('test.csv')