#You have been given two integer arrays/list(ARR1 and ARR2) of size N and M, respectively. You need to print their intersection; An intersection for this problem can be defined when both the arrays/lists contain a particular value or to put it in other words, when there is a common value that exists in both the arrays/lists.
#Note :
#Input arrays/lists can contain duplicate elements.

#The intersection elements printed would be in ascending order.


#Input format :
#The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

#The first line of each test case or query contains an integer 'N' representing the size of the first array/list.

#The second line contains 'N' single space separated integers representing the elements of the first the array/list.

#The third line contains an integer 'M' representing the size of the second array/list.

#The fourth line contains 'M' single space separated integers representing the elements of the second array/list.
#Output format :
#For each test case, print the intersection elements in a row, separated by a single space.

#Output for every test case will be printed in a separate line.
#Constraints :
#1 <= t <= 10^2
#0 <= N <= 10^6
#0 <= M <= 10^6

#Time Limit: 1 sec 
#Sample Input 1 :
#2
#6
#2 6 8 5 4 3
#4
#2 3 4 7 
#2
#10 10
#1
#10
#Sample Output 1 :
#2 3 4
#10
#Sample Input 2 :
#1
#4
#2 6 1 2
#5
#1 2 3 4 2
#Sample Output 2 :
#1 2 2
#Explanation for Sample Output 2 :
#Since, both input arrays have two '2's, the intersection of the arrays also have two '2's. The first '2' of first array matches with the first '2' of the second array. Similarly, the second '2' of the first array matches with the second '2' if the second array.

from sys import stdin


def intersection(arr1, arr2, n, m):
    arr1.sort()
    arr2.sort()
    arr3 = []
    i, j = 0, 0
    
    while i < n and j < m:
        if arr1[i] == arr2[j]:
            arr3.append(arr1[i])
            i += 1
            j += 1
            
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return arr3


def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def check(t):
    if t > 0:
        arr1, n = takeInput()
        arr2, m = takeInput()
        check(t-1)
        arr3 = intersection(arr1, arr2, n, m)
        for i in range(len(arr3)):
            print(arr3[i], end = " ")
        print("")


t = int(stdin.readline().strip())
check(t)
