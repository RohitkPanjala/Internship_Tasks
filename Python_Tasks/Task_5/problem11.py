# Problem 11: You are given a string s and width w.
# Your task is to wrap the string into a paragraph of w width .
# HackerRank Link:
# https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap

def wrap(string, max_width):
    s = textwrap.wrap(string,max_width)
    
    return "\n".join(s)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
