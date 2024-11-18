import logging
from pathlib import Path
from typing import List, Tuple

from src.computations.matrix_creation import (
    H0andH1matrixes,
    EplusEminusOplusOminusMatrixes,
)
from src.computations.eigenvalues_and_eigenvectors import get_eigenvalue_and_eigenvector
from src.computations.sort_determinants import sort_energies


_logger = logging.getLogger(__name__)

J_even = {"E_plus": "A", "E_minus": "B_z", "O_minus": "B_x", "O_plus": "B_y"}
J_odd = {"E_plus": "B_z", "E_minus": "A", "O_minus": "B_y", "O_plus": "B_x"}


def _application_loop(
    A: float,
    B: float,
    C: float,
    J: float,
    save_H_matrices: bool,
    save_submatrices: bool,
    output_file_path: Path,
) -> None:
    """"""
    eigenvalues_with_matrixes = dict()
    eigenvalues_with_eigenvectors = dict()

    h_matrixes = H0andH1matrixes(A, B, C, J)
    H_0 = h_matrixes.get_H0_matrix()
    H_1 = h_matrixes.get_H1_matrix()
    _logger.info("The H_0 matrix looks like:\n%s", H_0)
    _logger.info("The H_1 matrix looks like:\n%s", H_1)

    fac_mat = EplusEminusOplusOminusMatrixes(A, B, C, J)

    e_plus = fac_mat.get_e_plus_matrix(arr=H_0)
    eigvalue_eplus, eigvector_eplus = get_eigenvalue_and_eigenvector(e_plus)
    _logger.info("FOR MATRIX EPLUS:\n%s", e_plus)
    _logger.info("EIGENVALUE IS: %s AND EIGENVECTOR: %s", eigvalue_eplus, eigvector_eplus)
    for val in eigvalue_eplus.tolist():
        eigenvalues_with_matrixes[val] = "E_plus"
    for val, vect in zip(eigvalue_eplus.tolist(), eigvector_eplus.tolist()):
        eigenvalues_with_eigenvectors[val] = vect

    e_minus = fac_mat.get_e_minus_matrix2(arr=e_plus)
    eigvalue_emin, eigvector_emin = get_eigenvalue_and_eigenvector(e_minus)
    _logger.info("FOR MATRIX EMINUS:\n%s", e_minus)
    _logger.info("EIGENVALUE IS: %s AND EIGENVECTOR: %s", eigvalue_emin, eigvector_emin)
    for val in eigvalue_emin.tolist():
        eigenvalues_with_matrixes[val] = "E_minus"
    for val, vect in zip(eigvalue_emin.tolist(), eigvector_emin.tolist()):
        eigenvalues_with_eigenvectors[val] = vect

    o_plus = fac_mat.get_o_plus_matrix(arr=H_1)
    eigvalue_oplus, eigvector_oplus = get_eigenvalue_and_eigenvector(o_plus)
    _logger.info("FOR MATRIX OPLUS:\n%s", o_plus)
    _logger.info("EIGENVALUE IS: %s AND EIGENVECTOR: %s", eigvalue_oplus, eigvector_oplus)
    for val in eigvalue_oplus.tolist():
        eigenvalues_with_matrixes[val] = "O_plus"
    for val, vect in zip(eigvalue_oplus.tolist(), eigvector_oplus.tolist()):
        eigenvalues_with_eigenvectors[val] = vect

    o_minus = fac_mat.get_o_minus_matrix(arr=H_1)
    eigvalue_ominus, eigvector_ominus = get_eigenvalue_and_eigenvector(o_minus)
    _logger.info("FOR MATRIX OMINUS:\n%s", o_minus)
    _logger.info("EIGENVALUE IS: %s AND EIGENVECTOR: %s", eigvalue_ominus, eigvector_ominus)
    for val in eigvalue_ominus.tolist():
        eigenvalues_with_matrixes[val] = "O_minus"
    for val, vect in zip(eigvalue_ominus.tolist(), eigvector_ominus.tolist()):
        eigenvalues_with_eigenvectors[val] = vect

    _logger.info("EIGENVALUES DICT:\n%s\nEIGENVECT DICT:\n%s", eigenvalues_with_matrixes, eigenvalues_with_eigenvectors)
    final_outputs = sort_energies(eigenvalues_with_matrixes)

    with open(output_file_path, "a") as f:
        f.write("------------------------------------------------------------------------\n")
        if save_H_matrices:
            f.write("\n")
            f.write("H_0 matrix:\n")
            f.write(str(H_0) + "\n")
            f.write("H_1 matrix:\n")
            f.write(str(H_1) + "\n")
        if save_submatrices:
            f.write("\n")
            f.write("E_plus matrix:\n")
            f.write(str(e_plus) + "\n")
            f.write("E_minus matrix:\n")
            f.write(str(e_minus) + "\n")
            f.write("O_plus matrix:\n")
            f.write(str(o_plus) + "\n")
            f.write("O_minus matrix:\n")
            f.write(str(o_minus) + "\n")

    if J % 2 == 0:
        _write_outputs_to_file(output_file_path, final_outputs, is_j_even=True)
    else:
        _write_outputs_to_file(output_file_path, final_outputs, is_j_even=False)


def _write_outputs_to_file(
    output_file_path: Path, final_outputs: List[Tuple[int, float, str]], is_j_even: bool
) -> None:
    with open(output_file_path, "a") as f:
        f.write("\n")
        for otp in final_outputs:
            if is_j_even:
                f.write(f"{otp[0]}         {otp[1]:.6f}                     {otp[2]}          {J_even[otp[2]]}\n")
            else:
                f.write(f"{otp[0]}         {otp[1]:.6f}                     {otp[2]}          {J_odd[otp[2]]}\n")


def app(
    A: float,
    B: float,
    C: float,
    J: float,
    IJ: bool,
    save_H_matrices: bool,
    save_submatrices: bool,
    output_file_path: Path,
) -> None:
    """Application main entrtpoint"""
    with open(output_file_path, "a") as f:
        f.write("ROTATIONAL CONSTANTS (IN UNITS OF EV)\n")
        f.write(f"AXX={A}   BXX={B}   CXX={C}\n")
        f.write(f"VALUE OF THE ANGULAR MOMENTUM J={J}\n")
        f.write("---------------------------------------------------------------------\n")
        f.write("TAU        ENERGY [EV]                 MATRIX          IR\n")

    if IJ:
        for j in range(0, J + 1):
            _application_loop(A, B, C, j, save_H_matrices, save_submatrices, output_file_path)
    else:
        _application_loop(A, B, C, J, save_H_matrices, save_submatrices, output_file_path)
