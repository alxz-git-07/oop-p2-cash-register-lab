#!/usr/bin/env python3


class CashRegister:
    def __init__(
        self,
        discount=0,
    ):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) and not 0 <= value <= 100:
            print("Not valid discount")
        self._discount = value

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.append(item)

        transaction = {"item": item, "price": price, "quantity": quantity}
        self.previous_transactions.append(transaction)

    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply")
            return
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        self.previous_transactions.pop()

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("No transaction to void")
            return
        rm_last_tx = self.previous_transactions.pop()
        rm_cost = rm_last_tx["price"] * rm_last_tx["quantity"]
        self.total -= rm_cost

        if rm_last_tx["item"] in self.items:
            self.items.remove(rm_last_tx["item"])
