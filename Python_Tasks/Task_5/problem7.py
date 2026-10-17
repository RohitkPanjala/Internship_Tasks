# Problem 7: Given 2 sets of integers, find their symmetric difference and print the elements in ascending order, one per line.
# HackerRank Link: 
# https://www.hackerrank.com/challenges/symmetric-difference/problem

m = int(input())
a = set(map(int, input().split()))

n = int(input())
b = set(map(int, input().split()))

result = sorted(a.symmetric_difference(b))

for i in result:
    print(i)
