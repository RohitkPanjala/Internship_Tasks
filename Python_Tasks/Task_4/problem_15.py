# Problem 15: You are given n words. Some words may repeat. Output the number of distinct words and their occurrence counts in the order of their first appearance.
# HackerRank Link: 
# https://www.hackerrank.com/challenges/word-order/problem



n = int(input())

words = {}

for i in range(n):
    word = input().strip()

    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(len(words))
print(*words.values())
