#********************************************** == , < , > , not , TRUE/FALSE döndürür

# echo_word = lambda x, y : (x * y)
# echo_word("hello", 3)

# number_list = [1,2,3,4,5]
#  def kare(x) :
#      return x * 3
# result = list(map(lambda x : x * 3, number_list))
# print(result)

#*************************************************************
# first_ten = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
  
# even = filter(lambda x : x%2 == 0, first_ten) 
# print(type(even))  # it's 'filter' type, 
#                    # in order to print the result,
#                    # we'd better convert it into the list type

# print('Even numbers are :', list(even))

#*************************************************************

# vowel_list = ['a', 'e', 'i', 'o', 'u']
# first_ten = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
  
# vowels = filter(lambda x: True if x in vowel_list else False, first_ten) # filter(lambda x: x in vowel_list, first_ten) 

# print('Vowels are :', list(vowels))

#******************************

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# less_six = filter(lambda x: True if x >= 6 in number_list else False, number_list)
# print(*less_six)

#*****************************************************

# def modular_function(n):
#     return lambda x: x ** n
    
# power_of_2 = modular_function(2)  # first sub-function derived from def
# power_of_3 = modular_function(3)  # second sub-function derived from def
# power_of_4 = modular_function(4)  # third sub-function derived from def

# print(power_of_2 (2))  # 2 to the power of 2
# print(power_of_3 (2))  # 2 to the power of 3
# print(power_of_4 (2))  # 2 to the power of 4

#*****************************************************
# def functioner(emoji = None) :
#     return lambda message : print(message, emoji)

# print_smile = functioner(":)")
# print_smile(66)

# print_sad = functioner(":(")
# print_sad (77)

#*****************************************************

# def repeater(n):
#     return lambda x: x * n
    
# repeat_2_times = repeater(2)  # repeats 2 times
# repeat_3_times = repeater(3)  # repeats 3 times
# repeat_4_times = repeater(4)  # repeats 4 times

# print(repeat_2_times('alex '))
# print(repeat_3_times('lara '))
# print(repeat_4_times('linda '))

#*****************************************************

# nums1 = [9,6,7,4]
# nums2 = [3,6,5,8]

# xx = map(lambda x, y : (x +y )/2, nums1, nums2)
# print(* xx)

#*************************

# words1 = ["You", "much", "hard"]
# words2 = ["i", "you", "he"]
# words3 = ["love", "ate", "works"]

# my_words = map(lambda x, y, z : x +" "+ y + " "+ z, words2, words1, words3)
# for i in my_words :
#     print(i)

#*************************

# words = ["apple", "swim", "clock", "me", "kiwi", "banana"]
# for i in filter(lambda x : len(x) < 5, words) :
#     print(i)

#*************************

# def func_generator(n) :
#     return lambda x: n(x)


# kls_print = func_generator(print)
# kls_bool = func_generator(bool)
# kls_sorted = func_generator(sorted)

# kls_print("keles")
# kls_print("dsfafa fasdad")

# import math as matematik
# a = matematik.pi
# b = matematik.factorial(4)
# c = matematik.log10(1000)
# print((a, b, c))


# from math import pi, log10, factorial

# import string
# a = string.punctuation
# b = string.digits
# print(a,",", b)
# dir(string)

#*******************************************

# import datetime
# a = datetime.datetime.now()
# print(a)
#*******************************************
# from datetime import date
# birth = date(571, 4, 22)
# death = date(632, 6, 8)
# c = date.toordinal(death) - date.toordinal(birth)
# print(c)
# print(death-birth)
#*******************************************
from random import choice

city = ["stockholm", "çorum", "mardin","yozgat"]
print(choice(city))