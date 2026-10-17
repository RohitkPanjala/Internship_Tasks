# Problem 14: Apply the .add() operation on sets to find the total number of distinct country stamps collected.
# HackerRank Link: 
# https://www.hackerrank.com/challenges/py-set-add/problem


n = int(input())

countries = set()

for i in range(n):
    country = input().strip()
    countries.add(country)

print(len(countries))
