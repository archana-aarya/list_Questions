#Question 10 Find squere of the eliment in given list.

list = [[1,2,3,4,],[5,6,7,8],[9,10],[11,12]]
i = 0
while i<len(list):
    j = 0
    while j<len(list[i]):
        print("this is the squere of this number:-",list[i][j]*list[i][j])
        j = j + 1
    i = i+1