import random
lst = []
for i in range(9):
    number = random.randint(0,101)
    lst.append(number)
print(lst)
S = 0
f = open("file.txt", "w")
for i in range(9):
    if(i % 2 == 0):
        f.write(str(lst[i]) + ' ')
        S = S + lst[i]
f.write('\n' + str(S))
f.close()
