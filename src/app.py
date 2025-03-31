import logging
from pathlib import Path
import re
from typing import Dict, List, Tuple

import numpy as np

from src.computations.matrix_creation import (
    H0andH1matrices,
    EplusEminusOplusOminusSubmatrices,
)
from src.computations.eigenvalues_and_eigenvectors import (
    get_eigenvalue_and_eigenvector,
)
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
    """Application main loop.

    Args:
        A (float): rotational constant along x axis
        B (float): rotational constant along y axis
        C (float): rotational constant along z axis
        J (float): value of the total angular quantum number
        save_H_matrices (bool): writes H0 and H1 matices to output file
        save_submatrices (bool): writes E+, E-, O+, O- submatrices to ouput file
        output_file_path (Path): path to the output file
    """
    eigenvalues_with_matrixes = dict()
    eigenvalues_with_eigenvectors = dict()

    h_matrixes = H0andH1matrices(A, B, C, J)
    H_0 = h_matrixes.get_H0_matrix()
    H_1 = h_matrixes.get_H1_matrix()
    _logger.info("The H_0 matrix looks like:\n%s", H_0)
    _logger.info("The H_1 matrix looks like:\n%s", H_1)

    fac_mat = EplusEminusOplusOminusSubmatrices(A, B, C, J)

    e_plus = fac_mat.get_e_plus_submatrix(arr=H_0)
    eigvalue_eplus, eigvector_eplus = get_eigenvalue_and_eigenvector(e_plus)
    _logger.info("FOR SUBMATRIX EPLUS:\n%s", e_plus)
    _logger.info(
        "EIGENVALUES ARE:\n%s\nAND EIGENVECTORS:\n%s",
        eigvalue_eplus,
        eigvector_eplus,
    )
    for val in eigvalue_eplus.tolist():
        eigenvalues_with_matrixes[val] = "E_plus"
    for val, vect in zip(eigvalue_eplus.tolist(), eigvector_eplus.T):
        eigenvalues_with_eigenvectors[val] = vect

    e_minus = fac_mat.get_e_minus_submatrix(arr=e_plus)
    eigvalue_emin, eigvector_emin = get_eigenvalue_and_eigenvector(e_minus)
    _logger.info("FOR SUBMATRIX EMINUS:\n%s", e_minus)
    _logger.info(
        "EIGENVALUES ARE:\n%s\nAND EIGENVECTORS:\n%s",
        eigvalue_emin,
        eigvector_emin,
    )
    for val in eigvalue_emin.tolist():
        eigenvalues_with_matrixes[val] = "E_minus"
    for val, vect in zip(eigvalue_emin.tolist(), eigvector_emin.T):
        eigenvalues_with_eigenvectors[val] = vect

    o_plus = fac_mat.get_o_plus_submatrix(arr=H_1.copy())
    eigvalue_oplus, eigvector_oplus = get_eigenvalue_and_eigenvector(o_plus)
    _logger.info("FOR SUBMATRIX OPLUS:\n%s", o_plus)
    _logger.info(
        "EIGENVALUES ARE:\n%s\nAND EIGENVECTORS:\n%s",
        eigvalue_oplus,
        eigvector_oplus,
    )
    for val in eigvalue_oplus.tolist():
        eigenvalues_with_matrixes[val] = "O_plus"
    for val, vect in zip(eigvalue_oplus.tolist(), eigvector_oplus.T):
        eigenvalues_with_eigenvectors[val] = vect

    o_minus = fac_mat.get_o_minus_submatrix(arr=H_1.copy())
    eigvalue_ominus, eigvector_ominus = get_eigenvalue_and_eigenvector(o_minus)
    _logger.info("FOR SUBMATRIX OMINUS:\n%s", o_minus)
    _logger.info(
        "EIGENVALUES ARE:\n%s\nAND EIGENVECTORS:\n%s",
        eigvalue_ominus,
        eigvector_ominus,
    )
    for val in eigvalue_ominus.tolist():
        eigenvalues_with_matrixes[val] = "O_minus"
    for val, vect in zip(eigvalue_ominus.tolist(), eigvector_ominus.T):
        eigenvalues_with_eigenvectors[val] = vect

    _logger.info(
        "EIGENVALUES DICT:\n%s\nEIGENVECT DICT:\n%s",
        eigenvalues_with_matrixes,
        eigenvalues_with_eigenvectors,
    )
    final_outputs = sort_energies(eigenvalues_with_matrixes)

    with open(output_file_path, "a") as f:
        f.write(
            "------------------------------------------------------------------------\n"
        )
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
        _write_outputs_to_file(
            output_file_path,
            final_outputs,
            a=eigenvalues_with_eigenvectors,
            is_j_even=True,
        )
    else:
        _write_outputs_to_file(
            output_file_path,
            final_outputs,
            a=eigenvalues_with_eigenvectors,
            is_j_even=False,
        )


def _get_aknu(a: np.array, submatrix: str) -> List[str]:
    """Sort and prepare to be written to output file A(K, nu)
    for particular submatrix.

    Args:
        a (np.array): eigenvector for particular submatrix
        submatrix (str): submatrix name
    """
    aknu_list: List[str] = []

    if submatrix == "E_plus":
        k = 0
        for aknu in a:
            aknu_list.append(f"A( {k} 0 ) = {aknu:.6f}")
            k += 2
    if submatrix == "E_minus":
        k = 0
        for aknu in a:
            aknu_list.append(f"A( {k} 1 ) = {aknu:.6f}")
            k += 2
    if submatrix == "O_plus":
        k = 1
        for aknu in a:
            aknu_list.append(f"A( {k} 0 ) = {aknu:.6f}")
            k += 2
    if submatrix == "O_minus":
        k = 1
        for aknu in a:
            aknu_list.append(f"A( {k} 1 ) = {aknu:.6f}")
            k += 2

    return aknu_list


def _write_outputs_to_file(
    output_file_path: Path,
    energies: List[Tuple[int, float, str]],
    a: Dict[float, np.array],
    is_j_even: bool,
) -> None:
    """Write all outputs to the output file.

    Args:
        output_file_path (Path): path to output file
        energies (List[Tuple[int, float, str]]): sorted energy values
        a (Dict[float, np.array]): energy values with coresponding eigenvectors
        is_j_even (bool): indicates if J is even or odd
    """
    with open(output_file_path, "a") as f:
        f.write("\n")
        for otp in energies:
            if is_j_even:
                f.write(
                    f"{otp[0]}         {otp[1]:.6e}                     {otp[2]}          {J_even[otp[2]]}\n"
                )
                for aknu in _get_aknu(a[otp[1]], otp[2]):
                    f.write(f"{aknu:>88}\n")
            else:
                f.write(
                    f"{otp[0]}         {otp[1]:.6e}                     {otp[2]}          {J_odd[otp[2]]}\n"
                )
                for aknu in _get_aknu(a[otp[1]], otp[2]):
                    f.write(f"{aknu:>88}\n")


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
        f.write(
            "---------------------------------------------------------------------\n"
        )
        f.write("TAU        ENERGY [EV]                 MATRIX          IR\n")

    if IJ:
        for j in range(0, J + 1):
            _application_loop(
                A, B, C, j, save_H_matrices, save_submatrices, output_file_path
            )
    else:
        _application_loop(
            A, B, C, J, save_H_matrices, save_submatrices, output_file_path
        )
