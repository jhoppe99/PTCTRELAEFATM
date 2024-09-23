from typing import Tuple
import logging
import numpy as np
import numpy.linalg as linalg

logger = logging.getLogger(__name__) 

def get_eigenvalue_and_eigenvector(matrix: np.array) -> Tuple[np.array, np.array]:
    """
    """
    eigenvalues, eigenvectors = linalg.eig(matrix)
    return eigenvalues, eigenvectors
