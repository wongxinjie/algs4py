from datetime import datetime
from decimal import Decimal


class Transaction:
    __slots__ = ('who', 'when', 'amount')

    def __init__(self, who=None, when=None, amount=None):
        self.who = who
        self.when = when
        self.amount = amount

    def load(self, transaction):
        try:
            who, when, amount = transaction.split('-')
            self.who = who.strip()
            self.when = datetime.strptime(when, "%Y%m%d%H%M%S")
            self.amount = Decimal(float(amount))
        except:
            raise ValueError(
                "Transaction data format is `name-YYMMDDhhmmss-00.00`"
            )
        return self

    def __repr__(self):
        return "{}-{}-{}".format(
            self.who, self.when.strftime("%Y%m%d%H%M%S"), float(self.amount)
        )

    def __eq__(self, other):
        return (self.who == other.who and self.when == other.when and
                self.amount == other.amount)

    def __hash__(self):
        print(self)
        return hash(self.who) ^ hash(self.when) ^ hash(self.amount)

    def __gt__(self, other):
        return self.amount > other.amount

    def __lt__(self, other):
        return self.amount < other.amount
