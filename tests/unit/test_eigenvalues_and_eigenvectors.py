import numpy as np
import pytest

from computations.eigenvalues_and_eigenvectors import get_eigenvalue_and_eigenvector


matrix1 = np.array([[2.764200e-02, -8.927227e-03], [-8.927227e-03, 2.562400e-02]])
matrix2 = np.array([[2.562400e-02]])
matrix3 = np.array([[2.022250e-02, -4.463613e-03], [-4.463613e-03, 2.310150e-02]])
matrix4 = np.array([[3.405250e-02, -4.463613e-03], [-4.463613e-03, 2.310150e-02]])


@pytest.mark.parametrize(
    "input_matrix, expected_output",
    [
        (matrix1, [0.0356171, 0.0176489]),
        (matrix2, [0.0256240]),
        (matrix3, [0.0169720, 0.0263520]),
        (matrix4, [0.0356413, 0.0215127]),
    ],
)
def test_eigenvalue_and_eigenvector(input_matrix, expected_output) -> None:
    val, _ = get_eigenvalue_and_eigenvector(input_matrix)
    for inp, out in zip(val.tolist(), expected_output):
        assert round(inp, 7) == round(out, 7)
