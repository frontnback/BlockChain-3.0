
# initialize our empty blockchain list
# holds value of blockchain list
blockchain = []

def get_last_blockchain_value():
# returns the last value of the blockchain
    if len(blockchain) < 1:
        #nothing to return so we use the null/none value
        return None
    return blockchain[-1]
# this function accepts 2 arguments
# one required on (transaction_amount) and 1 optional 1 (last_transaction)
#the optional 1 is opitonal bc it has a default value => [1]

def add_transaction(transaction_amount, last_transaction=[1]):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])
# append a new value as well as the last blockchain value to the blockchain
# arguments [1]:transaction_amount: amount should be added
# arguments [2]:last_transaction: the last blockchain transaction(default [1])
def get_transaction_value():
    # returns the input of the user (a new transaction amount) as a float
    user_input = float(input('Your transaction amount please: '))
    return user_input

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)

#get the first transaction input and add the value to the blockchain
# output the blockchain list to the console
# while loop allows to add as many blockchains as possible
while True:
    print('Please choose ')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('4: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice =='h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    #continue can be used to keep prgm from ending, choice will also never register
    else:
        print('Input was invalid, please enter a new value from list')
    print('Choice registered!')

print('Done!')
