# to set its row and column to be 0 if any matrix value is zero

def matrix(matrix):
	row = [0] * 4
	column = [0] * 4
	for rowc in matrix:
		i = 0
		for value in rowc:
			if value == 0:
				row[i] = 1
				column[i] = 1
			i += 1
	j = 0
	for value in row:
		if value == 1:
			for i in range(4):
					matrix[j][i] = 0
		j += 1
	j = 0
	for value in column:
		if value == 1:
			for i in range(4):
					matrix[i][j] = 0
		j += 1
	print matrix

Matrixv = [[1 for y in range(4)] for x in range(4)]
Matrixv[2][2] = 0
matrix(Matrixv)