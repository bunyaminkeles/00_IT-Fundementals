sentence = "ey edip adana'da, pide ye!"
list_sentence = list(sentence)
list_sentence_plain = [i for i in sentence if i.isalnum()]
if list_sentence_plain == list(reversed(list_sentence_plain)):
    print('"'+sentence + '" is a palindrome')
else:
    print("not")

inputt =  "ey edip adana'da, pide ye!".lower()
print('palindrone' if [*filter(lambda x :x.isalpha(), inputt)]==\
    [*filter(lambda x :x.isalpha(), reversed(inputt))] else 'degil')


sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
print(17*'- ')
for i in sudoku:
    print(f'{i[0:3]} | {i[3:6]} | {i[6:9]}')
    if sudoku.index(i)%3==2:
        print(17*'- ')

count = 0
print("- - - - - - - - - - - - - - - ")
for i in sudoku:
    for j in range(9):
        print(i[j], " ", end="")
        if (j+1) == 9 : 
            print()
            count+=1
            if count%3==0 and count!=0 :
                print("- - - - - - - - - - - - - - - ")
        if (j+1) % 3 == 0 and j != 0 and j!=8: 
             print("| ", end="")