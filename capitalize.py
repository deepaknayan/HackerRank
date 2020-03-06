'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

chris alan
Sample Output

Chris Alan
'''

def solve(s):
    # Separator ' ' was used to ensure that spaces also remain after splitting
    # the string

    # Capitalize the first character of string (if first character is numeric
    # the function simply ignore it.)
    temp = s.split(' ')
    temp = [i.capitalize() for i in temp]

    print(' '.join(temp))

if __name__ == '__main__':
    s = input()
    solve(s)
