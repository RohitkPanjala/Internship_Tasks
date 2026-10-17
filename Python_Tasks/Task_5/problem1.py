# Problem 1: Given the participants' score sheet for your University Sports Day, store them in a list and find the score of the runner-up (the second highest score).
# HackerRank Link: 
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())
arr = map(int, input().split())

lst2 = []

for i in arr:
    if i not in lst2:
        lst2.append(i)
lst2.sort()
print(lst2[-2])


