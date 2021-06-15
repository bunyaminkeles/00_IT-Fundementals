import os

clear = lambda: os.system("cls")
clear()
#******************************************************************


# variable = "global"


# def func_outer():

#     variable = "enclosing outer local"

#     def func_inner():

#         variable = "enclosing inner local"

#         def func_local():

#             variable = "local"

#             print(variable)

#         func_local()

#     func_inner()
 

# func_outer()  # prints 'local' defined in the innermost function

# print(variable)  # 'global' level variable holds its value

#************************************************************************

# def enclosing_func1():

#     x = 'outer variable'

#     def enclosing_func2():

#         nonlocal x  # its inner-value can be used in the outer scope

#         x = 'inner variable'

#         print("inner:", x)

#     enclosing_func2()

#     print("outer:", x)


# enclosing_func1() 


# def myfunc1():
#   x = "hi"
#   def myfunc2():
#       nonlocal x
#       x = "hello"
#   myfunc2() 
#   return x
# print(myfunc1())
# #***********************************

# def get_initial(name) :
#     return name [0:1].upper()

#***********************************

# def get_initial(name) :
#     initial = name [0:1].upper()
#     return initial
# first_name = input("Enter your first name: ")
# first_name_initial = get_initial(first_name)
# print("Your first initial is :" + first_name_initial)

#*****************

# def brothers(bro1, bro2, bro3):
#     print('Here are the names of brothers :')
#     print(bro1, bro2, bro3, sep='\n')
# family = ['tom', 'sue', 'tim']
# brothers(*family)

#*****************************************
# genius = ("Bill", "Rossum", "Guido van", "Gates")
# def merger(gn1, gn2, gn3, gn4) :
#     print(f"For me, {gn1} {gn4} {gn3} {gn2} are geniusus")
# merger(*genius)

#**************************************************************
# def gene(x = "Bunyamin", y = "Beyza"):  # defined by positional args
#     print(x, "belongs to Generation X")
#     print(y, "belongs to Generation Y")
# dict_gene = {'y' : "Bunyamin", 'x' : "Keles"}
# gene(**dict_gene)  # we call the function by a single argument(variable)

#***************************************************************************************

# coup = [("mary", "rye"), ("bella", "fred"), ("linda", "roland")]
# dict_couple = {
#     "bride": ["mary", "bella", "linda"],
#     "groom" : ["rye", "fred", "rolan"]}

# # def couples(bride, groom) :
# #     couple_list = []
# #     for x in zip(bride, groom) :
# #         couple_list.append(x)
#     return couple_list

# def couples(bride, groom) :
#     return [x for x in zip(bride,groom)]
# couples(**dict_couple)

# friends = {"ahmed" :44, "yasir" : 35, "burak" : 16}

# def meaner (ahmed, yasir, burak) :
#     average = (ahmed + yasir + burak) / 3
#     print("The average of their age is :", average)
# meaner(** friends)
#************************
x = "({}[{}])"
def isValid(s) :
    while "()" in s or "[]" in s or "{}" in s :
        s = s.replace("()" ,"").replace("[]", "").replace("{}", "")
        return s == ""
isValid(x)



