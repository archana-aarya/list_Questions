
#Question 2. find the maximum number from this list.

# Code likho jo iss list mein se maximum dhund kar ke print kare.
 
numbers = [40, 23, 100, 12, 5, 300, 900, 10, 7,800] # Iss list ke liye aapke program ka output 70 hona chaiye.

max = 0

index = 0

while index < len(numbers):

    if numbers[index] > max:

        max = numbers[index]

    index = index + 1
    
print(max)

