from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(self, balance=0):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def with_draw(self, amount):
        pass
