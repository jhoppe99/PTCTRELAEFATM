import logging
from pathlib import Path

from src.computations.matrix_creation import H0andH1matrixes, EplusEminusOplusOminusMatrixes
from src.computations.matrix_operations import calculate_determinant
from src.computations.eigenvalues_and_eigenvectors import get_eigenvalue_and_eigenvector
from src.computations.sort_determinants import sort_energies


_logger = logging.getLogger(__name__)


def app(A: float, B: float, C: float, J: float, output_file_path: Path) -> None:
    eigenvalues_with_matrixes = dict()
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

    e_minus = fac_mat.get_e_minus_matrix2(arr=e_plus)
    eigvalue_emin, eigvector_emin = get_eigenvalue_and_eigenvector(e_minus)
    _logger.info("FOR MATRIX EMINUS:\n%s", e_minus)
    _logger.info("EIGENVALUE IS: %s AND EIGENVECTOR: %s", eigvalue_emin, eigvector_emin)
    for val in eigvalue_emin.tolist():
        eigenvalues_with_matrixes[val] = "E_minus"

    o_plus = fac_mat.get_o_plus_matrix(arr=H_1)
    eigvalue_oplus, eigvector_oplus = get_eigenvalue_and_eigenvector(o_plus)
    _logger.info("FOR MATRIX OPLUS:\n%s", o_plus)
    _logger.info("EIGENVALUE IS: %s AND EIGENVECTOR: %s", eigvalue_oplus, eigvector_oplus)
    for val in eigvalue_oplus.tolist():
        eigenvalues_with_matrixes[val] = "O_plus"

    o_minus = fac_mat.get_o_minus_matrix(arr=H_1)
    eigvalue_ominus, eigvector_ominus = get_eigenvalue_and_eigenvector(o_minus)
    _logger.info("FOR MATRIX OMINUS:\n%s", o_minus)
    _logger.info("EIGENVALUE IS: %s AND EIGENVECTOR: %s", eigvalue_ominus, eigvector_ominus)
    for val in eigvalue_ominus.tolist():
        eigenvalues_with_matrixes[val] = "O_minus"

    _logger.info("Finall dict: %s", eigenvalues_with_matrixes)
    final_outpus = sort_energies(eigenvalues_with_matrixes)
    with open(output_file_path, 'a') as file:
        file.write("ROTATIONAL CONSTANTS (IN UNITS OF EV)\n")
        file.write(f"AXX={A}   BXX={B}   CXX={C}\n")
        file.write(f"VALUE OF THE ANGULAR MOMENTUM J={J}\n")
        file.write(f"--------------------------------------------\n")
        file.write("TAU        ENERGY [EV]                 MATRIX\n")
        file.write(f"--------------------------------------------\n")
        for otp in final_outpus:
            file.write(f"{otp[0]}         {otp[1]}         {otp[2]}\n")
