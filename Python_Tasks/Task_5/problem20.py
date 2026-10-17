# Problem 20 - Piling Up
# HackerRank Link: 
# https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

def can_pile(blocks):
    blocks = deque(blocks)
    last = float('inf')

    while blocks:
        if blocks[0] >= blocks[-1]:
            cube = blocks.popleft()
        else:
            cube = blocks.pop()

        if cube > last:
            return "No"

        last = cube

    return "Yes"


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        blocks = list(map(int, input().split()))
        print(can_pile(blocks))
