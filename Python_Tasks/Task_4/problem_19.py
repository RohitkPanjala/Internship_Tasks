# Problem 19: Solve a shoe shop inventory problem using collections.Counter() where a shopkeeper has a certain number of shoes of different sizes and a list of customer desired sizes with prices. Calculate total earnings.
# HackerRank Link: 
# https://www.hackerrank.com/challenges/collections-counter/problem


X = int(input())
shoes = list(map(int, input().split()))

N = int(input())

total = 0

for i in range(N):
    size, price = map(int, input().split())

    if size in shoes:
        total += price
        shoes.remove(size)

print(total)
