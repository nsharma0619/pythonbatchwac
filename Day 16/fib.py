memory = [1, 1]

# def fibonacci(n):
#     if n==0 or n==1:
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)


def fibonacci(n):
    for i in range(n-1):
        memory.append(memory[len(memory)-1]+memory[len(memory)-2])
    print(memory)


fibonacci(100)
