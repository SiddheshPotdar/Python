
#* Square pattern
# for i in range(5):
#   for j in range(5):
#     print("*", end=' ')
#   print()

#* Increasing triangle
# for i in range(5):
#   for j in range(i+1):
#     print("*", end=' ')
#   print()

#* Decreasing triangle
# for i in range(5):
#   for j in range(5-i):
#     print("*", end=' ')
#   print()

#* Right triangle
# for i in range(5):
#   for j in range(5-i):
#     print(" ", end=' ')
#   for k in range(i+1):
#     print("*", end=' ')
#   print()

#* Left triangle
# for i in range(5):
#   for j in range(i+1):
#     print(" ", end=' ')
#   for k in range(5-i):
#     print("*", end=' ')
#   print()

#* HIll pattern
# for i in range(5):
#   for j in range(5-i):
#     print(" ", end=' ')
#   for k in range(i+1):
#     print("*", end=' ')
#   for l in range(i):
#     print("*", end=' ')
#   print()

#* Reverse pyramid
# for i in range(5):
#   for j in range(i+1):
#     print(" ", end=' ')
#   for k in range(5-i):
#     print("*", end=' ') 
#   for l in range(5-i-1):
#     print("*", end=' ')
#   print()

#todo: Diamond pattern
# for i in range(5):
#   for j in range(5-i):
#     print(" ", end=' ')
#   for k in range(i+1):
#     print("*", end=' ')
#   for l in range(i):
#     print("*", end=' ')
#   print()
# for i in range(4):
#   for j in range(i+2):
#     print(" ", end=' ')
#   for k in range(4-i):
#     print("*", end=' ') 
#   for l in range(4-i-1):
#     print("*", end=' ')
#   print()


#! bbs
for i in range(4):
  for j in range(4-i):
    print(" ", end=' ')
  for k in range(i+1):
    print(i-k+1, end=' ')
  for l in range(i):
    print(l+2, end=' ')
  print()