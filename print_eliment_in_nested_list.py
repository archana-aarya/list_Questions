#Question 9.print the eliments in nested list.

list = [[1,2,3,20,],[5,6,7,1]]
i = 0
sum = 0
while i<len(list):
    j = 0
    while j<len(list[i]):
        print(list[i][j])
        j = j + 1
    i = i+1
