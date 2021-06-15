# ******************* LAMBDA ***********************
# def square(x) :
#     return x**2
# if body+if+condition+else+else body

# print((lambda x :  "odd" if x%2 else "even")(55))

# average_ = (lambda a, b, c : a**2, b**2, c**2)(3,4,5)
# print((lambda a, b, c : a**2, b**2, c**2)(3,4,5))

# my_list = [1,2,3,4]
# for i in my_list :
#     print(i, ":", (lambda x : "odd" if i%2 else "even")(my_list))

# hipotenus = lambda a, b : a**2 + b**2
# print(hipotenus(3,4))

# iterable = "keles"
# reverser = lambda x : x[::-1]
# print((reverser(iterable)))

#**************************** map function************************
# iterable = [1,2,3,4,5]
# result = map(lambda x : x**2 , iterable)
# # for i in result :
# #     print(i)
# print(list(result))
#******
# def kare(x) :
#     return x ** 2
# result = map(kare, iterable)
# print(*result)

# iterable_2 = ["bunyamin", "keles", "selahattin"]
# result_2 = map(len, iterable_2)
# print(* result_2)

# letter1 = ["o","t","s","b"]
# letter2 = ["n","w","i","e"]
# letter3 = ["e","o","x","s"]
# no = map(lambda x,y,z : x+y+z, letter1, letter2, letter3)
# # print(list(no))
# print(*no, sep="-")


# no = map(zip, letter1, letter2 ,letter3)
# for i in no :
#     for j in i :
#         print(j)