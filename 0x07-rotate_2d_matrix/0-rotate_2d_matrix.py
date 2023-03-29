#usr/bin/python3

def rotate_2d_matrix(matrix):
	'''rotate n x n matrix 90 degrees clockwise '''

	left, right = 0, len(matrix) -1

	while left < right:
		for i in range(right - left):
			top, bottom = right, left
			topLeft = matrix[top][left + i]
			matrix[top][left + i] = matrix[bottom - i][left]
			matrix[bottom - i][left] = matrix[bottom][right - i]
			matrix[bottom][right] = matrix[top + i][right]
			matrix[top + i][right] = topLeft

		right -= 1
		left += 1