import pytest
import numpy as np

from computations.sort_determinants import sort_energies
from computations.eigenvalues_and_eigenvectors import get_eigenvalue_and_eigenvector

eigenvalues_with_matrix = dict()

eplus_eigenval = get_eigenvalue_and_eigenvector(
    np.array([[1.382100e-02, -3.992377e-03], [-3.992377e-03, 1.180300e-02]])
)
for val in eplus_eigenval[0]:
    eigenvalues_with_matrix[val] = "E_plus"
eminus_eigenval = get_eigenvalue_and_eigenvector(np.array([[1.180300e-02]]))
for val in eminus_eigenval[0]:
    eigenvalues_with_matrix[val] = "E_minus"
oplus_eigenval = get_eigenvalue_and_eigenvector(np.array([[9.859000e-03]]))
for val in oplus_eigenval[0]:
    eigenvalues_with_matrix[val] = "O_plus"
ominus_eigenval = get_eigenvalue_and_eigenvector(np.array([[1.677400e-02]]))
for val in ominus_eigenval[0]:
    eigenvalues_with_matrix[val] = "O_minus"


def test_sort_energies() -> None:
    # GIVEN/WHEN
    results = sort_energies(eigenvalues_with_matrix)
    # THEN
    assert results[0][0] == -2
    assert round(results[0][1], 8) == 0.00869409
    assert results[0][2] == "E_plus"

    assert results[1][0] == -1
    assert round(results[1][1], 8) == 0.00985900
    assert results[1][2] == "O_plus"

    assert results[2][0] == 0
    assert round(results[2][1], 7) == 0.0118030
    assert results[2][2] == "E_minus"

    assert results[3][0] == 1
    assert round(results[3][1], 7) == 0.0167740
    assert results[3][2] == "O_minus"

    assert results[4][0] == 2
    assert round(results[4][1], 7) == 0.0169299
    assert results[4][2] == "E_plus"
