
# students_name = ["saloni", "neeraj", "ashish", "deepak", "saloni"]





# for i in students_name:
#     print(i)


# for i in range(1, 10, 2):
#     print(i)


# lis = ["5", "6", "8"]

# print(lis)
# for i in range(len(lis)):
#     lis[i] = int(lis[i])

# print(lis)

# n = int(input())
# if n%2 == 0:
#     if n in range(2,6):
#         print("Not Weird")
#     elif(n in range(6,21)):
#         print("Weird")
#     else:
#         print("Not Weird")
# else:
#     print("Weird") 

# *
# **
# ***
# ****
# *****
# ******

n = int(input())
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print("")


# n = int(input())
# for i in range(1, n+1):
#     print("*"*i)