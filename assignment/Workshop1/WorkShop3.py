import os
clear = lambda: os.system("cls")
clear()

# def query(s):
#     while "()" in s or "{}" in s or '[]' in s:
#         s = s.replace("()", "").replace('{}', "").replace('[]', "")
#     return s == ''
# print(query(('(){}[]({[]})')))

#List = [10,20,23,22,17,30]
# List = [9, 11, 8, 5, 7, 10]
# #List = [1,6,19,59,30,60]
# min_L =min(List)
# while min(List) < List[0]:
#   List.pop(0)
# profit =max(List)-min_L
# print(profit)

# #*****************************
# def buy_and_sell(arr):
#     max_profit = 0
#     for i in range(len(arr) - 1):
#         for j in range(i, len(arr)):
#             buy_price, sell_price = arr[i], arr[j]
#             max_profit = max(max_profit, sell_price - buy_price)
#     return max_profit

# #*****************************
# def buy_and_sell(array):
#     temp = 0
#     for i in range(len(array)-1):
#         for j in range(i+1, len(array)):
#             if (array[i] < array[j]) and (array[j] - array[i] > temp):
#                 temp = array[j] - array[i]
#     return temp
# # print(buy_and_sell([9, 7, 16, 11, 8, 5, 7, 10]))
# print(buy_and_sell([9, 11, 8, 5, 7, 10, 1, 9]))

#******************************* HİSSE SENEDİ *******************
arr = []
def buy_and_sell(arr):
    current_max, max_profit = 0, 0
    for price in reversed(arr):
        current_max = max(current_max, price)
        potential_profit = current_max - price
        max_profit = max(max_profit, potential_profit)
    return max_profit
buy_and_sell([1, 9, 46, 88, 65, 44])

# #*-************************** MORS ALFABESİ*****************

# encoding_dict = {
#   'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#   'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#   'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#   'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
#   '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#   '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#   '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
#   ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
#   '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
# }
# def encode_morse(text):
#     stack = []
#     for i in text:
#         stack.append(encoding_dict[i.upper()])
#     return " ".join(stack)

