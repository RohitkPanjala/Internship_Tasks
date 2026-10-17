# Problem 2: You are given a string. Split the string on a " " (space) delimiter and join it using a - hyphen.
# HackerRank Link: 
# https://www.hackerrank.com/challenges/python-string-split-and-join/problem


def split_and_join(line):
   
    line = line.split()
    line = "-".join(line)
    
    return line
    
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
