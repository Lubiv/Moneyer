class Transaction:

    def __init__(self, title, amount, isExpense, dateTime):
        self.title = title
        self.amount = amount
        self.isExpense = isExpense
        self.dateTime = dateTime

    def as_dict(self):
        return {"title": self.title, "amount": self.amount, "isExpense": self.isExpense, "dateTime": self.dateTime}