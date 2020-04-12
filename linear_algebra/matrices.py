#Here, we will provide basic functionality for matrix operations

def shape(A):
	""" return the num_rows, num_columns"""
	num_rows = len(A)
	num_columns = len(A[0]) if A else 0
	return num_rows, num_columns

def get_row(A, i):
	""" return jth row as a list """
	return A[i]

def get_column(A, j):
	""" return the jth column """
	return [A_i[j] for A_i in A]

def make_matrix(num_rows, num_columns, entry_fn):
	""" return the matrix 
	whose A(i, j) entry is entry_fn(i, j)"""
	return [[entry_fn(i, j) for j in range(num_columns)] for i in range(num_rows)]

def unit_fn(i, j):
	return 1 if i == j else 0


"""convert given list data into matrix form """
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
 (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

def friendship_fn(i, j):
	return 1 if (i, j) in friendships else 0

friendships_matrix = make_matrix(9, 9, friendship_fn)

print(friendships_matrix)
