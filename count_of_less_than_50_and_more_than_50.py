#Question 6. print count of the eliments which is less then 50 and which is more than 50.

student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]

list_length = len(student_marks)

index = 0

a = []

b = []

less_than50 = 0

more_than50 = 0

while index < list_length:

    marks = student_marks[index]

    if marks < 50:

        less_than50 = less_than50 + 1

        a.append(marks)

    else:

        more_than50 = more_than50 + 1

        b.append(marks)

    index = index + 1

print("Count marks of more then 50:", more_than50 ,"and more than 50 marks eliment of this list:" , b)

print("Count marks of less than 50:", less_than50 , "and less than 50 marks eliment of this list:" , a)