# Problem 20 - Validating phone numbers

# HackerRank Link -
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com

n = int(input())

for i in range(n):
    number = input()

    if len(number) == 10 and number[0] in "789" and number.isdigit():
        print("YES")
    else:
        print("NO")
