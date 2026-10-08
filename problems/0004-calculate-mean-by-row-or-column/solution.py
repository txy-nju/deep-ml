import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode is 'column':
		return np.array(matrix).mean(axis=0).tolist()
	else:
		return np.array(matrix).mean(axis=1).tolist()