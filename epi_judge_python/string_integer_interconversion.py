from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    if x == 0:
        return "0"
    string = ""
    negative = x < 0
    if negative:
        x *= -1
    while x >= 1:
        curr = int(x % 10)
        x = int(x/10)

        if curr == 0:
            string = "0" + string
        elif curr == 1:
            string = "1" + string
        elif curr == 2:
            string = "2" + string
        elif curr == 3:
            string = "3" + string
        elif curr == 4:
            string = "4" + string
        elif curr == 5:
            string = "5" + string
        elif curr == 6:
            string = "6" + string
        elif curr == 7:
            string = "7" + string
        elif curr == 8:
            string = "8" + string
        elif curr == 9:
            string = "9" + string

    if negative:
        string = "-" + string

    return string

def string_to_int(s):
    negative = 1
    numb = 0
    for char in s:
        if char == "-":
            negative = -1
        elif char == "0":
            numb = numb * 10
        elif char == "1":
            numb = numb * 10 + 1
        elif char == "2":
            numb = numb * 10 + 2
        elif char == "3":
            numb = numb * 10 + 3
        elif char == "4":
            numb = numb * 10 + 4
        elif char == "5":
            numb = numb * 10 + 5
        elif char == "6":
            numb = numb * 10 + 6
        elif char == "7":
            numb = numb * 10 + 7
        elif char == "8":
            numb = numb * 10 + 8
        elif char == "9":
            numb = numb * 10 + 9
    return numb*negative


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
