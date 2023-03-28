# Ramzi Jarad
# Python Basics Assignment 06
# OOP quiz - Creat bank account class
import random


class BankAccount:
    def __init__(self, full_name, age):
        self.id = random.randint(100000, 999999)
        self.full_name = full_name
        self.age = age
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")

    def __str__(self):
        return f"Account ID: {self.id}\nFull Name: {self.full_name}\nAge: {self.age}\nBalance: {self.balance}"

account = BankAccount("Ramzi Jarad", 35)
account.deposit(1000)
account.withdraw(500)
print(account)