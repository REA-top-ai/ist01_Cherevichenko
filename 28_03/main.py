from client_classes import DepositBankAccount, BankAccount, Client

def main():
    client1 = DepositBankAccount('Alice')
    client2 = DepositBankAccount('Bob')
    
    client1.add_money(200)
    client2.add_money(500)
    client1.payments(150)
    client2.payments(500)

if __name__ == '__main__':
    main()