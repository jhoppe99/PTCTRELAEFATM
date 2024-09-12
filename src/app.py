import logging

from src.computations.matrix_creation import BasicMatrixes, FactorizedSubmatrices
from src.computations.matrix_operations import DetOfMatrixCalculation
import src.computations.eigenvalues_and_eigenvectors as eig


_logger = logging.getLogger(__name__)


def app(A: float, B: float, C: float, J: float) -> None:
    h_matrixes = BasicMatrixes(A, B, C, J)
    H_0 = h_matrixes.create_H0_matrix()
    H_1 = h_matrixes.create_H1_matrix()
    _logger.info("The H_0 matrix looks like:\n%s", H_0)
    _logger.info("The H_1 matrix looks like:\n%s", H_1)

    e_plus = FactorizedSubmatrices.create_e_plus_matrix(arr=H_0)
    eig.get_eigenvalue_and_eigenvector(e_plus)
    det_obj1 = DetOfMatrixCalculation(arr=e_plus)
    det_of_e_plus = det_obj1.calculate_determinant()

    e_minus = FactorizedSubmatrices.create_e_minus_matrix(arr=H_1)
    eig.get_eigenvalue_and_eigenvector(e_minus)
    det_obj2 = DetOfMatrixCalculation(arr=e_minus)
    det_of_e_minus = det_obj2.calculate_determinant()

    o_plus = FactorizedSubmatrices.create_o_plus_matrix(arr=H_1)
    eig.get_eigenvalue_and_eigenvector(o_plus)
    det_obj3 = DetOfMatrixCalculation(arr=o_plus)
    det_of_o_plus = det_obj3.calculate_determinant()

    _logger.info("DETERMINANTS OF E_PLUS -> %s | E_MINUS -> %s | O_PLUS -> %s", det_of_e_plus, det_of_e_minus, det_of_o_plus)
