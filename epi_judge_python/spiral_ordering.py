from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    l = len(square_matrix)
    returnResult = [0 for x in range(l*l)]

    currLoop = 1
    row = 0
    col = 0

    # this will be our direction
    d = 1

    for i in range(l*l):
    	returnResult[i] = square_matrix[col][row]

    	if d == 1:
    		if row == l - currLoop:
    			d = 2
    	elif d == 2:
    		if col == l - currLoop:
    			d = 3
    	elif d == 3:
    		if row == currLoop - 1:
    			d = 4
    	else:
    		if col == currLoop:
    			d = 1
    			currLoop += 1

    	if d == 1:
    		row += 1
    	elif d == 2:
    		col += 1
    	elif d == 3:
    		row -= 1
    	else:
    		col -= 1


    return returnResult


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
