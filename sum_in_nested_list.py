#Question 11.find sum of the eliments in nested list.

list = [[1,3,4,],[4,5,6,]] 
i=0
while i<=len(list):
    j=0
    sum=0
    while j<len(list):
        sum=sum+list[j][i]
        j=j+1
    i=i+1
    print("this is the sum of this number:",sum)