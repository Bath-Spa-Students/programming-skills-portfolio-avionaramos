#Write a python program that takes courses marks as input and then calculates average of all the
#courses. After calculating the average, calculate the percentage of a student using total marks. Assume
#the total of all the courses marks is 500 or take the total marks from the user as input.

courses = int(input("Enter the number of course: "))
marks = int(input("Enter the total marks: "))

mark = [float(input(f"Enter marks for course {i + 1}: ")) for i in range(courses)]

#Calculate the average
average = sum(mark) / courses

percentage = (sum(mark)/ (courses * marks)) * 100

print(f"The average marks is: {average}")
print(f"The percentage is : {percentage}%")

