sayı = int(input("sayı giriniz:"))
i = 1
while 0 < sayı:
    i *= sayı
    sayı -=1
print(i)

letters1 = ["a", "b", "c", "d", "f", "g", "a", "a", "c", "f", "g", "s"]
letters2 = ("adadadafsdfagearfdsasd")
print(max([(letters1.count(x), x) for x in set(letters1)]))
print(min([(letters2.count(x), x) for x in set(letters2)]))


numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
y = max([(numbers.count(x), x) for x in set(numbers)])
print(f"the most frequent number is {y[1]} and it was {y[0]} times repeated")

my_list = {1, 2, 4,}
my_list.append("1")
print(my_list)

aaa = [1,2,3,4,4,4,5,5,5,5,6,6,7,5,1,2,6,5]
eee = max([(aaa.count(a), a) for a in set(aaa)])
print(eee)

aaa = [1,2,3,4,4,4,5,5,5,5,6,6,7,5,1,2,6,5]
bbb = [1,2,2,3,4,5,5,6,7]
ddd = aaa.intersection(bbb)

print(aaa)
bbb.remove(5)
print(bbb)
bbb.add(7)
print(bbb)
ccc = {1,2,3,4,4,5,5,6}
ddd = set((1,2,3,4,5))

print(len(set('listen to the voice of enlisted')))

numbers = {}

numbers['x'] = 12
numbers['y'] = 4
numbers.update({'z': 3})

print(numbers['x'] + numbers['y'] + numbers['z']**2)

letters = ['a', 'b', 'c', 'd', 'f']
letters.insert(4, 'e')
print(letters)

numbers_10 = [10, 30, 40, 50, 60, 70, 80, 90, 100]
numbers_10.insert(1, 20)
print(numbers_10)

fruits_vegetables = ["fruit", "vegetable", ["apple", "banana", ["mango", "avocado"]], ["spinach", "brocoli"]]
print(fruits_vegetables[3][0])


family_members = ['Meghan', 'Tom', 'Nicole', 'Tim']
print(tuple(family_members))

empty_seat = 14
if empty_seat > 3:  # in this case, 14>3=True, so the body will execute
    print('there is still seat to sit')

x = 6
y = 9
print ("is x equal to y?                 :" , x == y)
print ("is x not equal to y?             :" , x != y)
print ("is x less than y?                :" , x < y)
print ("is x greater than y?             :" , x > y)
print ("is x less than or equal to y?    :" , x <= y)
print ("is x greater than or equal to y? :" , x >= y)

course = 'clarusway'
if course == "clarusway":
    print("you guaranteed the job")
else:
    print("think about it again")

number = 5
if number <= 3:    
    print("Number is smaller than or equal to 3") 
else:  # Optional clause (you can only have one else)
    print("Number is bigger than 3")

weight = 80
if weight > 100:
    print("That's too heavy!")
elif weight > 75:
    print("I can lift that!")
else:
    print("That's too light!")


audience = "baby"

if audience == "kid":
    print("it is free to go to cinema")
elif audience == "teen":
    print("discounted price!")
elif audience == "adult":
    print("normal price")
else:
    print("No such audience, stay at your home!")

number = 23
if number >= 10:
    print("The number is equal or greater than 10")
else:
    print("The number is less than 10")

audience_group = 'kid', 'teen', 'adult'
audience = "teen"
if audience in audience_group:
    if audience == "kid":
        print("it is free to go to cinema")
    elif audience == "teen":
        print("discounted price!")
    else: # audience == "adult":
        print("normal price")
else:
    print("No such audience, stay at your home!")


score = int (input("Enter your score :"))

if score >= 90:
    if score >= 95:
        Score_letter="A+"
    else:
        Score_letter="A"
elif score >= 80:
    if score >= 85:
        Score_letter="B+"
    else:
        Score_letter="B"
else:
    Score_letter="below B"

print ("Your degree: %s" % Score_letter)