# list = expression for item in iterable

#* for loop
# squares = list()
# for i in range(1,11):
#   squares.append(i * i)
# print(squares)

#* list comprehension
# print(squares)
# squares = [i * i for i in range(1,11)]

students = [90, 78, 34, 55, 87, 32, 99]

# passed_students = list(filter(lambda x: x >= 60, students))

passed_students = [i for i in students if i >= 60]

pass_status = ['Pass' if i > 60 else 'Fail' for i in students]

print(passed_students)
print(pass_status)