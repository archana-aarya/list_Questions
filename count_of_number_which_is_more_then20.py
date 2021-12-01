
#Question 5. print the count number which is more then 20 or less than 40 by list.

#question is :- Code likho jo di gayi list mein jo number 20 se bade hai aur 40 se chote hai unhe count kare. Aur firr unka count print kare.
 
numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7, 26, 27, 34, 24] 

index = 0

count = 0

list2 = []

length = len(numbers)

while index<length:

    if numbers[index] < 40 and numbers[index] > 20:

        list2.append(numbers[index])

        count = count+1

    index = index + 1

print("eliments of in this list which is more than 20 and less than 40 :" , list2)

print("count of numbers which is more then 20 and less than 40 :", count)