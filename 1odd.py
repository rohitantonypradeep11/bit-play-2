def abc(arr):
    a = 0
    for element in arr:
        a = a^element
    return a
arr = []
n = int(input("enter the size of the arry"))
while n:
    num = int(input("enter a numbber"))
    arr.append(num)
    n = n-1
print(abc(arr))