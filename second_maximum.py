#Question 3. find the second maximum nuber .

numbers = [40, 23, 100, 12, 5, 300, 10, 7, 987, 800] # find second meximum.

max = 0

second_max = 0

index = 0

while index < len(numbers):

    if numbers[index] > max:

        second_max = max

        max = numbers[index]

    elif numbers[index] > second_max and max > second_max:

        second_max = numbers[index]
        
    index = index + 1

print("this is the maximum number of this list:",max)
    
print("this is the second maximum number of this list:",second_max)
