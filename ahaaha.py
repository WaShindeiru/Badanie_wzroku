import numpy as np

def reduce_matrix_by_rows(matrix):
    value = 0
    size = matrix.shape[0]

    for row_index in range(size):
        row = matrix[row_index]
        min_value = np.min(row)
        value += min_value

        matrix[row_index, :] -= min_value

    return value

def reduce_matrix_by_column(matrix):
    value = 0
    size = matrix.shape[0]

    for column_index in range(size):
        column = matrix[:, column_index]
        min_value = np.min(column)
        value += min_value

        matrix[:, column_index] -= min_value

    return value

def reduce_matrix(matrix):
    lower_bound = reduce_matrix_by_rows(matrix)
    lower_bound += reduce_matrix_by_column(matrix)

    return lower_bound

def main():
    matrix_aha = np.array([
        [5, 2, 3, 2, 7],
        [6, 8, 4, 2, 5],
        [6, 4, 3, 7, 2],
        [6, 9, 0, 4, 0],
        [4, 1, 2, 4, 0]])

    value = reduce_matrix(matrix_aha)

    print(matrix_aha)
    print(value)


if __name__ == "__main__":
    main()