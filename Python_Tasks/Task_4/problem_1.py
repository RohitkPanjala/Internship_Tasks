# Problem 1: Given an integer, n, perform the following conditional actions:
# - If n is odd, print Weird
# - If n is even and in the inclusive range of 2 to 5, print Not Weird
# - If n is even and in the inclusive range of 6 to 20, print Weird
# - If n is even and greater than 20, print Not Weird

# HackerRank Link: 
# https://www.hackerrank.com/challenges/py-if-else/problem


def evn_odd(n):
    if n%2!=0:
        return "Weird"
    elif n%2==0 and 2 <= n <= 5:
        return "Not Weird"
    elif n%2==0 and 6<=n<=21:
        return "Weird"
    elif n%2==0 and n >20:
        return "Not Weird"


x = evn_odd(3)
print(x)

y= evn_odd(22)
print(y)    