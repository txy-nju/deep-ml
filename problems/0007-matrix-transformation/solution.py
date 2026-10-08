import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	if np.linalg.det(np.array(S))==0 or np.linalg.det(np.array(A))==0:
		return -1
	return np.linalg.inv(np.array(T))@np.array(A)@np.array(S)