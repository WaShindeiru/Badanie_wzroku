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
    lecture_matrix = np.array([
        [float('inf'), 5, 4, 6, 6],
        [8, float('inf'), 5, 3, 4],
        [4, 3, float('inf'), 3, 1],
        [8, 2, 5, float('inf'), 6],
        [2, 2, 7, 0, float('inf')]])

    print(f"Macierz z wykładu: \n {lecture_matrix} \n")
    reduced_matrix_value = reduce_matrix(lecture_matrix)

    print(f"Macierz zredukowana: \n {lecture_matrix} \n")

    random_matrix = np.random.randint(1, 15, size=(6, 6)).astype('float')
    np.fill_diagonal(random_matrix, float('inf'))

    print(f"Macierz losowa: \n {random_matrix} \n")
    reduced_random_matrix_value = reduce_matrix(random_matrix)

    print(f"Macierz zredukowana: \n {random_matrix}")


if __name__ == "__main__":
    main()