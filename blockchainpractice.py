# blockchain = [[1]]
#
# def add_value():
#     blockchain.append([blockchain[-1],5.3])
#     print(blockchain)
#
# add_value()
# add_value()
# add_value()


# [1, [1, 5.3]]
# [1, [1, 5.3], [1, 5.3]]
# [1, [1, 5.3], [1, 5.3], [1, 5.3]]

# blockchain.append([blockchain[-1],5.3])
# [1, [1, 5.3]]
# [1, [1, 5.3], [[1, 5.3], 5.3]]
# [1, [1, 5.3], [[1, 5.3], 5.3], [[[1, 5.3], 5.3], 5.3]]



# blockchain = [[1]]
#
# def get_last_blockchain_value():
#     return blockchain[-1]
#
# def add_value(transaction_amount):
#     blockchain.append([get_last_blockchain_value(), transaction_amount])
#     print(blockchain)
#
# add_value(2)
# add_value(3)
# add_value(5)
#
# print blockchain

# [[1], [[1], 2]]
# [[1], [[1], 2], [[[1], 2], 3]]
# [[1], [[1], 2], [[[1], 2], 3], [[[[1], 2], 3], 5]]
# [[1], [[1], 2], [[[1], 2], 3], [[[[1], 2], 3], 5]]



# blockchain = []
#
# def get_last_blockchain_value():
#     return blockchain[-1]
#
# def add_value(transaction_amount, last_transaction=[1]):
#     blockchain.append([last_transaction, transaction_amount])
#     print (blockchain)
#
# add_value(2)
# add_value(3)
# add_value(5)
#
# print blockchain

# [[[1], 2]]
# [[[1], 2], [[1], 3]]
# [[[1], 2], [[1], 3], [[1], 5]]
# [[[1], 2], [[1], 3], [[1], 5]]
