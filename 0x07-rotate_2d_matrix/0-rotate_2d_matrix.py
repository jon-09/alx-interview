#!/usr/bin/python3

"""rotate 2d matrix """

def rotate_2d_matrix(matrix):

	""" rotate n x n matrix 90 degrees clockwise
	"""

l = len(matrix)
for layer in range(n // 2):
	first, last, offset = layer, l - 1 - layer, 0
	for i in range(first, last):
		top = matrix[first, last]
		matrix[first][i] = matrix[last - offset][first]
		matrix[last - offset][first] = matrix[last][last - offset]
		matrix[last][last - offset] = matrix[i][last]
		matrix[i][last] = top
		offset += 1