import pandas as pd
from Transaction import *

class Balance:

    def __init__(self, transactions, initial):
        self.balance = pd.DataFrame(Transaction("initial", initial, False, ""), [1], ["title", "amount", "isExpence", "dateTime"])

        for transaction in transactions:
            self.add(transaction)


    def add(self, transaction):
        if transaction.isExpense:
            self.expense.append(transaction)
            self.expensesum += transaction.amount
        else:
            self.income.append(transaction)
            self.incomesum += transaction.amount
        
    def save(self):
        self.balance = pd.DataFrame(Transaction("initial", 1, False, ""), [1], ["title", "amount", "isExpence", "dateTime"])

    def load(self):
        #implementation of the loading the balance from svc
        return 0