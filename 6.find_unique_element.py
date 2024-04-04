from sys import stdin


def findUnique(arr, si, n):
    xor = arr[0]
    for i in range(1,n):
        xor = xor ^ arr[i]
    return xor


def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


t = int(stdin.readline().strip())
result = []
while t > 0:
    arr, n = takeInput()
    result.append(findUnique(arr, 0, n))
    t -= 1

for i in range(len(result)):
    print(result[i])
