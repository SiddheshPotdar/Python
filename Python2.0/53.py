# sort() method = used in list
# sort() function = used in iterables


#! list
# students = ['Tom', 'John', 'Oggy', 'Ruby', 'Jack']

# # students.sort()
# students.sort(reverse=True)

# for i in students:
#   print(i)


#! tuple
# students = ('Tom', 'John', 'Oggy', 'Ruby', 'Jack')

# sorted_students = sorted(students)

# for i in sorted_students:
#   print(i)

#!
students = [('Tom', 'B', 22),
            ('John', 'D', 32),
            ('Ruby', 'A', 35),
            ('Oggy', 'C', 19),
            ('Jack', 'F', 25)
            ]

# grade = lambda grades: grades[1]
# students.sort(key=grade)

age = lambda ages: ages[2]
students.sort(key = age)

for i in students:
  print(i)