# lis = [5, 3, 2, 6]

# print(lis[2])

# print(lis)
# # lis[1] = 4

# # lis.append(5)

# del(lis[1])

# print(lis)

# print(len(lis))
# lis.sort()
# print(lis)




# lis = [1, 5, [56, 54, 8, [5, 2, 3]], 57]

# print(lis[2][3][1])

# lis = [1 ,2, 3, 4, 5, 6, 7, 8, 9]

# print(lis[2:5])

# print(lis[2:])

# print(lis[:5])

# print(lis[2:7:2])

# print(lis[-2:-8:-1])

# print(lis[-2:2:-1])



#list comprehension

lis = [1, 988,65, 65,64564, 659589, 65656, 564698]

# even = []

# for i in lis:
#     if(i%2==0):
#         even.append(i)
# print(even)

even = [i for i in lis if i%2==0]

print(even)