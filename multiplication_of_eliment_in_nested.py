#Question 8. print the multipication of the elements in nested list.

list = [[1,2,3,2],[4,5 ,6,2 ]] 
i = 0
while i <=len(list):
    j = 0
    multiply = 1
    while j<len(list):
        multiply = list[j][i] * multiply
        j=j+1
    i = i + 1
    print("multiplication of this numbers",multiply)