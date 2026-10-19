# Problem 1 - Find if the number is even or odd using if elif else
# HackerRank Link:
# https://www.hackerrank.com/challenges/py-if-else/problem


if __name__ == '__main__':
    n = int(input().strip())
    
    if n%2==1:
        print("Weird")
    elif n%2==0 and 2<=n<=5:
        print("Not Weird")
    elif n%2==0 and 6<=n<=20:
        print("Weird")
    elif n%2==0 and n>20:
        print("Not Weird")    
