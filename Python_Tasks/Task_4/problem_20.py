# Problem 20: Given an array of n integers and two disjoint sets A and B of m integers, calculate your total happiness. Add 1 for every array element present in set A and subtract 1 for every element present in set B.
# HackerRank Link: 
# https://www.hackerrank.com/challenges/no-idea/problem

n, m = map(int, input().split())

arr = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0

for i in arr:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1

print(happiness)
