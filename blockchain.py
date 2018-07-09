
# initialize our empty blockchain list
blockchain = []

def get_last_blockchain_value():
# returns the last value of the blockchain
    return blockchain[-1]
# this function accepts 2 arguments
# one required on (transaction_amount) and 1 optional 1 (last_transaction)
#the optional 1 is opitonal bc it has a default value => [1]

def add_value(transaction_amount, last_transaction=[1]):
        blockchain.append([last_transaction, transaction_amount])
# append a new value as well as the last blockchain value to the blockchain
# arguments [1]:transaction_amount: amount should be added
# arguments [2]:last_transaction: the last blockchain transaction(default [1])
# returns the input of the user (a new transaction amount) as a float
def get_transaction_value():
    user_input = float(input('Your transaction amount please: '))
    return user_input

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


#get the first transaction input and add the value to the blockachain
tx_amount = get_user_input()
add_value(tx_amount)

# output the blockchain list to the console
# while loop allows to add as many blockchains as possible
while True:
    print('Please choose ')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    user_choice = get_user_choice()
    if user_choice
    tx_amount = get_user_input()
    add_value(tx_amount, get_last_blockchain_value())

    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)

print('Done!')
