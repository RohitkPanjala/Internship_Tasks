# Problem 19 - Merge the Tools!

# Consider the following:

# A string, s, of length n where n is a positive integer.

# An integer, k, where k is a factor of n.

# We can split s into n/k substrings where each substring, tᵢ, consists of a contiguous block of k characters in s.

# Then, use each tᵢ to create a string, uᵢ, such that:

# The characters in uᵢ are a subsequence of the characters in tᵢ.

# Any repeated occurrence of a character is removed from the string, such that each character in uᵢ occurs exactly once. In other words, if a character at some index in tᵢ occurs at a previous index in tᵢ, do not include that character again in uᵢ.

# Given s and k, print n/k lines where each line contains the string uᵢ.

# Function Description

# Complete the merge_the_tools function in the editor below.

# merge_the_tools has the following parameters:

# string s: the string to analyze

# int k: the size of substrings to analyze

# Prints

# Print each subsequence on a new line. There will be n/k lines. No return value is expected.

# HackerRank:
# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub = string[i:i+k]
        result = ""

        for ch in sub:
            if ch not in result:
                result += ch

        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
