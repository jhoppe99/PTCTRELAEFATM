
from matrix_creation import BasicMatrixes, FactorizedSubmatrices
import eigenvalues_and_eigenvectors as eig
import logging

logger = logging.getLogger(__name__)

A = 0.115100E-02
B = 0.345600E-02
C = 0.179900E-02
J = 5


def app() -> None:
    h_matrixes = BasicMatrixes(A, B, C, J)
    H_0 = h_matrixes.create_H0_matrix()
    H_1 = h_matrixes.create_H1_matrix()
    print(H_0)
    e_plus = FactorizedSubmatrices.create_e_plus_matrix(arr=H_0)
    print(e_plus)
    eig.get_eigenvalue_and_eigenvector(e_plus)
    print("----------------------------------------------------")
    print(H_1)
    e_minus = FactorizedSubmatrices.create_e_minus_matrix(arr=H_1)
    print(e_minus)
    eig.get_eigenvalue_and_eigenvector(e_minus)
    print("----------------------------------------------------")
    o_plus = FactorizedSubmatrices.create_o_plus_matrix(arr=H_1)
    print(H_1)
    print(o_plus)
    eig.get_eigenvalue_and_eigenvector(o_plus)


def main() -> None:
    logging.basicConfig(format="[%(asctime)s][%(name)s][%(levelname)s] - %(message)s", datefmt="%d/%m/%Y %I:%M:%S", level=logging.INFO)
    logger.info("Hello from new ASYMTOP app!")
    app()
    logger.info("Finishing run...")


if __name__ == "__main__":
    main()
