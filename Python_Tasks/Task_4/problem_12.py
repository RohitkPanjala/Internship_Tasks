# Problem 12: Given an array of plant heights, calculate the average of all the unique plant heights using a Python set.
# HackerRank Link: 
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem



def average(arr):
    s = set(arr)

    avg = sum(s)/len(s)

    return avg


arr = list(map(int, input().split()))
result = average(arr)
print(result)