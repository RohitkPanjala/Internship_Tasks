# Problem 6 - Print the list of integers from 1 through n as a string, without spaces.
# HackerRank Link:
# https://www.hackerrank.com/challenges/python-print/problem


if __name__ == '__main__':
    n = int(input())
    st = ""
    for i in range(1,n+1):
        st+=str(i)
        
    print(st)    
