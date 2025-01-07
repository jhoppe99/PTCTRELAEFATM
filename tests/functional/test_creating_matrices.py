import pytest
import numpy as np

from computations.matrix_creation import H0andH1matrices, EplusEminusOplusOminusSubmatrices


def test_creating_h0_and_h1_matrices() -> None:
    """_summary_"""
    # GIVEN
    A = 0.115100e-02
    B = 0.345600e-02
    C = 0.179900e-02
    J = 2
    h1_and_h0_matrices = H0andH1matrices(A=A, B=B, C=C, J=J)
    e_plus_minus_o_plus_minus = EplusEminusOplusOminusSubmatrices(A=A, B=B, C=C, J=J)
    e_plus_expected = np.array([[1.382100e-02, -3.992377e-03], [-3.992377e-03, 1.180300e-02]])
    e_minus_expected = np.array([[1.180300e-02]])
    o_plus_expected = np.array([[9.859000e-03]])
    o_minus_expected = np.array([[1.677400e-02]])

    # WHEN
    h0 = h1_and_h0_matrices.get_H0_matrix()
    h1 = h1_and_h0_matrices.get_H1_matrix()
    e_plus = e_plus_minus_o_plus_minus.get_e_plus_submatrix(h0)
    e_minus = e_plus_minus_o_plus_minus.get_e_minus_submatrix(e_plus)
    o_plus = e_plus_minus_o_plus_minus.get_o_plus_submatrix(h1)
    o_minus = e_plus_minus_o_plus_minus.get_o_minus_submatrix(h1)

    # THEN
    assert round(e_plus[0][0], 6) == round(e_plus_expected[0][0], 6)
    assert round(e_plus[0][1], 6) == round(e_plus_expected[0][1], 6)
    assert round(e_plus[1][0], 6) == round(e_plus_expected[1][0], 6)
    assert round(e_plus[1][1], 6) == round(e_plus_expected[1][1], 6)
    assert round(e_minus[0][0], 6) == round(e_minus_expected[0][0], 6)
    assert round(o_plus[0][0], 6) == round(o_plus_expected[0][0], 6)
    assert round(o_minus[0][0], 6) == round(o_minus_expected[0][0], 6)
