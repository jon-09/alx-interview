#!/usr/bin/python3
""" function make change """

import sys

def makeChange(coins, total):
	""" return fewest number of coins needed to meet total """
	if (total == 0):
		return 0

	count = sys.maxsize

	for i in range(0, len(coins)):
		if (coins[i] <= total):
			prevCount = makeChange(coins, total - coins[i])
			if (prevCount + 1 < count and prevCount != sys.maxsize):
				count = prevCount + 1


	return count

