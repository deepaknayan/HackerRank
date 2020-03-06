'''
You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------

The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).

Input Format

Only one line of input containing , the size of the rangoli.

Constraints


Output Format

Print the alphabet rangoli in the format explained above.

Sample Input

5
Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''

def print_rangoli(size):
    # your code goes here
    max_width = (size * 2 - 1) * 2 - 1
    iter_list_first = list(range(size, 0, -1))# + list(range(2, size + 1))
    counter = 0
    for i in iter_list_first:
        if i < size:
            char_list = list(range(size, size - counter, -1)) + list(range(size - counter, size + 1))
            my_string = ('-'.join([chr(96 + j) for j in char_list]))
        else:
            my_string = chr(96 + i)
        counter += 1
        padding = '-' * int((max_width - len(my_string)) / 2)
        my_string = padding + my_string + padding
        print(my_string)

    iter_list_second = list(range(1, size))
    for i in iter_list_second:
        char_list = list(range(size, i, -1)) + list(range(i + 2, size + 1))
        my_string = ('-'.join([chr(96 + j) for j in char_list]))
        padding = '-' * int((max_width - len(my_string)) / 2)
        my_string = padding + my_string + padding
        print(my_string)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)