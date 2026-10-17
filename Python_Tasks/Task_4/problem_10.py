# Problem 10: In this challenge, the user enters a string and a substring. Print the number of times that the substring occurs in the given string from left to right.
# HackerRank Link: 
# https://www.hackerrank.com/challenges/find-a-string/problem


def count_substring(string, sub_string):
    count = 0
    window_size = len(sub_string)

    for i in range(len(string) - window_size + 1):
        window = string[i:i + window_size]

        if window == sub_string:
            count += 1

    return count


string = input().strip()
sub_string = input().strip()
count = count_substring(string, sub_string)
print(count)