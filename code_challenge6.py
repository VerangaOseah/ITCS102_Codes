#code challenge 6
number = 1
size = int(input("Enter size: "))
for x in range (0,size):
    for y in range (x):
            print(number, end = " ")
            number += 1
    print(" ")