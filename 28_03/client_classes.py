from abc import ABC, abstractmethod
import time


def log_transaction(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f'transaction start at {start_time} end at {end_time}')

        return result
    return wrapper

        

class BankAccount(ABC):

    @abstractmethod
    def add_money(self, amount):
        pass


class DepositBankAccount(BankAccount):
    def __init__(self, client_name):
        self.__client_name = client_name
        self.__balance = 0
    
    @log_transaction
    def add_money(self, amount):
        self.__balance += amount
        print(f'{self.__client_name} added {amount}. Balance is {self.__balance}')

    @log_transaction
    def payments(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f'{self.__client_name} pay {amount}. Balance is {self.__balance}')
        else:
            print(f'Not enough money. Balance is {self.__balance}')

    def get_balance(self):
        return self.__balance


class Client:
    def __init__(self, name):
        self.name = name
        self.accounts = list()

    def create_bank_account(self):
        new_account = DepositBankAccount(self.name)
        self.accounts.append(new_account)
    
