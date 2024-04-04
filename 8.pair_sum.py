#You have been given an integer array/list(ARR) and a number 'num'. Find and return the total number of pairs in the array/list which sum to 'num'.
#Note:
#Given array/list can contain duplicate elements. 
#Input format :
#The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

#First line of each test case or query contains an integer 'N' representing the size of the first array/list.

#Second line contains 'N' single space separated integers representing the elements in the array/list.

#Third line contains an integer 'num'.
#Output format :
#For each test case, print the total number of pairs present in the array/list.

#Output for every test case will be printed in a separate line.
#Constraints :
#1 <= t <= 10^2
#0 <= N <= 10^4
#0 <= num <= 10^9

#Time Limit: 1 sec
#Sample Input 1:
#1
#9
#1 3 6 2 5 4 3 2 4
#7
#Sample Output 1:
#7
#Sample Input 2:
#2
#9
#1 3 6 2 5 4 3 2 4
#12
#6
#2 8 10 5 -2 5
#10
#Sample Output 2:
#0
#2


#Explanation for Input 2:
#Since there doesn't exist any pair with sum equal to 12 for the first query, we print 0.

#For the second query, we have 2 pairs in total that sum up to 10. They are, (2, 8) and (5, 5).

from sys import stdin
import bisect


def pairSum(arr, n, num):
    arr.sort()
    x, c = 0, 0
    for i in range(n-1):
        x = num-arr[i]

        # Lower bound from i+1
        y = bisect.bisect_left(arr, x, i+1, n)

        # Upper bound from i+1
        z = bisect.bisect(arr, x, i+1, n)
        c = c+z-y
    return c


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
    num = int(stdin.readline().strip())
    result.append(pairSum(arr, n, num))

    t -= 1

for i in range(len(result)):
    print(result[i])
