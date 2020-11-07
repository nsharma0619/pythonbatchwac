age = int(input())
line2 =  input().split(" ")
for i in range(len(line2)):
    line2[i] = int(line2[i])
max_height = max(line2)
count_candel = 0

for i in line2:
    if i==max_height:
        count_candel+=1
print(count_candel)