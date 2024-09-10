import logging
import numpy as np
import numpy.linalg as linalg

logger = logging.getLogger(__name__) 

def get_eigenvalue_and_eigenvector(matrix: np.array) -> None:
    """
    """
    eigenvalues, eigenvectors = linalg.eigh(matrix)
    
    logger.info("For matrix: %s -> eigenvalue is: %s | eigenvector: %s", matrix, eigenvalues, eigenvectors)
