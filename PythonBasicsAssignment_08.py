# Ramzi Jarad
# Python Basics Assignment 08
# Create bank account class and Transaction Class

import random
from datetime import datetime

class Transaction:
    def __init__(self, trans_type, amount):
        self.id = random.randint(1000, 9999)
        self.type = trans_type
        self.amount = amount
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class BankAccount:
    def __init__(self, full_name, age):
        self.id = random.randint(100000, 999999)
        self.full_name = full_name
        self.age = age
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount for deposit")
            return

        self.balance += amount
        transaction = Transaction("Deposit", amount)
        self.transactions.append(transaction)
        print("\n\t", "##" * 10)
        print("Deposit of", amount, "successful")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount for withdrawal")
            return
        if self.balance < amount:
            print("Insufficient balance")
            return
        self.balance -= amount
        transaction = Transaction("Withdrawal", amount)
        self.transactions.append(transaction)
        print("\n\t", "##" * 10)
        print("Withdrawal of", amount, "successful")

    def get_balance(self):
        return self.balance

    def get_transactions_history(self):
        for transaction in self.transactions:
            print("\n\t", "##"*10)
            print("Transaction ID:", transaction.id)
            print("Transaction Type:", transaction.type)
            print("Transaction Amount:", transaction.amount)
            print("Transaction Date:", transaction.date)
            print("\n")

    def __str__(self):
        return f"\nAccount ID: {self.id}\nFull Name: {self.full_name}\nAge: {self.age}\nBalance: {self.balance}"



account = BankAccount("Ramzi Jarad", 29)
account.deposit(1000)
account.withdraw(500)
print("\n\t", "##"*10, account)
account.get_transactions_history()
