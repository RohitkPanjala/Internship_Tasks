# Problem 5: Read an integer $n$. Without using any string methods, print the string 123...n (e.g., if $n = 3$, print 123).
# HackerRank Link: 
# https://www.hackerrank.com/challenges/python-print/problem



n = int(input())

st = ""
for i in range(1,n+1):
    st+=str(i)


print(st)