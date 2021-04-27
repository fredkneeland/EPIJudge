from test_framework import generic_test


def parity(x):
    parity = 0
    while x > 0:
    	curr = x & 1
    	if curr == 1:
    		parity = parity ^ curr
    	x >>= 1
    return parity


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
