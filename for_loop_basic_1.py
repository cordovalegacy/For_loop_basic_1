for i in range(0, 151):
    print(i)

for i in range(5, 1000, 5):
    print(i)

for i in range(1, 101):
    if i % 5:
        print('Coding')
    else:
        print('Coding Dojo')

sum = 0
for i in range(1, 500000, 2):
    sum += i
print(sum)

for i in range(2018, 0, -4):
    if i%2==0:
        print(i)

lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)