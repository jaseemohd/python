# ------------------------------------
# Question 1
# Print all Python keywords
# ------------------------------------

import keyword

print("Question 1")
print(keyword.kwlist)


# ------------------------------------
# Question 2
# ------------------------------------

print("\nQuestion 2")

x = 10
print("Value:", x)
print("Type:", type(x))


# ------------------------------------
# Question 3
# ------------------------------------

print("\nQuestion 3")

numbers = (10, 20, 30, 40)

print("Tuple:", numbers)
print("Second Element:", numbers[1])
print("Last Element:", numbers[-1])


# ------------------------------------
# Question 4
# ------------------------------------

print("\nQuestion 4")

num = "123"
result = int(num) + 10

print("Result:", result)


# ------------------------------------
# Question 5
# ------------------------------------

print("\nQuestion 5")

float_num = 45.78
int_num = int(float_num)

print("Float:", float_num)
print("Integer:", int_num)


# ------------------------------------
# Question 6
# ------------------------------------

print("\nQuestion 6")

str1 = "Hello"
str2 = "World"

new_string = str1 + " " + str2

print("Joined String:", new_string)
print("Length:", len(new_string))


# ------------------------------------
# Question 7
# ------------------------------------

print("\nQuestion 7")

flag = True

print("Value:", flag)
print("Type:", type(flag))


# ------------------------------------
# Question 8
# ------------------------------------

print("\nQuestion 8")

t = (10, 20, 30, 40, 50)

print("Length of Tuple:", len(t))


# ------------------------------------
# Question 9
# ------------------------------------

print("\nQuestion 9")

language = "Python"
version = 3.13

result = language + str(version)

print(result)


# ------------------------------------
# Question 10
# ------------------------------------

print("\nQuestion 10")

student_name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
city = input("Enter City: ")
course = input("Enter Course Name: ")

sub1 = float(input("Enter Marks in Subject 1: "))
sub2 = float(input("Enter Marks in Subject 2: "))
sub3 = float(input("Enter Marks in Subject 3: "))

total = sub1 + sub2 + sub3
percent = total / 3

print("\nStudent Name:", student_name)
print("Age:", age)
print("City:", city)
print("Course:", course)
print("Percentage:", percent)


# ------------------------------------
# Question 11
# ------------------------------------

print("\nQuestion 11")

subjects = ["Python", "SQL", "Excel", "Tableau"]

# a
print("Complete List:", subjects)

# b
print("First Subject:", subjects[0])
print("Last Subject:", subjects[-1])

# c
subjects.insert(1, "Power BI")
print("After Inserting:", subjects)

# d
subjects.remove("Excel")
print("After Removing Excel:", subjects)

# e
new_subjects = subjects.copy()
print("Copied List:", new_subjects)

# f
new_subjects.sort()
print("Sorted List:", new_subjects)

# g
print("Is Excel Present?", "Excel" in new_subjects)


# ------------------------------------
# Question 12
# ------------------------------------

print("\nQuestion 12")

attendance = True
assignment_submitted = False

# a
print("attendance or assignment_submitted =",
      attendance or assignment_submitted)

# b
print("attendance and assignment_submitted =",
      attendance and assignment_submitted)

# c
print("not attendance =", not attendance)
