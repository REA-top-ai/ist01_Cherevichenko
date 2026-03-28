def add_money(amount, client_name, client_balance):
    client_balance += amount
    print(f'{client_name} added {amount}. Balance is {client_balance}')

    return client_balance

def payments(amount, client_name, client_balance):
    if client_balance >= amount:
        client_balance -= amount
        print(f'{client_name} pay {amount}. Balance is {client_balance}')
    else:
        print(f'Not enough money. Balance is {client_balance}')

    return client_balance


if __name__ == '__main__':
    client1 = 'Alice'
    client1_balance = 1000

    client2 = 'Bob'
    client2_balance = 500

    client1_balance = add_money(500, client1, client1_balance)
    client2_balance = payments(300, client2, client2_balance)