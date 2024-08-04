
food = ['hotdog','burger','sandwich']

#creating 2D list 

stuff = [
    ['naan','wheat','potato'],
    ['ipad','phone','laptop'],
    ['pen','pencil','staple']
]

#printing on 2D lists

print(stuff)
print(stuff[1][1])
print(stuff[2][2])

#number of items in 2D list 
#rows

print(len(stuff))

#columns

print(len(stuff[0]))

#printing individual items 1 by 1

for row in range(len(stuff)):
    for column in range(len(stuff[0])):
        print(stuff[row][column],end=' ')
    print()

#asking user to make a 2d list

userRow = int(input("how many rows do you want? "))
userCol = int(input("how many columns do you want? "))
metrics = []

for row in range(userRow):
    rowList = []
    for column in range(userCol):
        userItem = int(input("what numbers do you want to add? "))
        rowList.append(userItem)
    metrics.append(rowList)

print(metrics)

#2D list operations: +, -, *, /

matrix1 = [
    [1, 2],
    [6, 3]
]

matrix2 = [
    [7, 9],
    [8, 5]
]

matrixAdd = [
    [0, 0],
    [0, 0]
]

matrixSub = [
    [0, 0],
    [0, 0]
]

matrixMult = [
    [0, 0],
    [0, 0]
]

matrixDiv = [
    [0, 0],
    [0, 0]
]

for row in range(2):
    for column in range(2):
        matrixAdd[row][column] = matrix1[row][column] + matrix2[row][column]

print(matrixAdd)

for row in range(2):
    for column in range(2):
        matrixSub[row][column] = matrix1[row][column] - matrix2[row][column]

print(matrixSub)

for row in range(2):
    for column in range(2):
        matrixMult[row][column] = matrix1[row][column] * matrix2[row][column]

print(matrixMult)

for row in range(2):
    for column in range(2):
        matrixDiv[row][column] = matrix1[row][column] / matrix2[row][column]\

print(matrixDiv)