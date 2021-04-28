from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices):
	curr_smallest = prices[0]
	max_profit = 0
	for price in prices:
		if price-curr_smallest > max_profit:
			max_profit = price-curr_smallest
		if price < curr_smallest:
			curr_smallest = price
	return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
