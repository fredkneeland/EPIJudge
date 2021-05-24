from test_framework import generic_test


def power(x: float, y: int) -> float:
	if y == 0:
		return 1
		
	result = x
	for _ in range(abs(y)-1):
		result *= x

	if y < 0:
		return 1 / result
	return result


if __name__ == '__main__':
	exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
										power))
