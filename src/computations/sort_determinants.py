import re
from typing import Dict, Tuple, List
import logging
import numpy as np


_logger = logging.getLogger(__name__)


def sort_energies(eigenvals_with_matrix: Dict[float, str]) -> List[Tuple[int, float, str]]:
    """"""
    all_outputs: List[Tuple[int, float, str]] = []
    
    eigenvalues = sorted(list(eigenvals_with_matrix.keys()))
    start_idx = int((len(eigenvalues)-1)*(-1)*(0.5))
    stop_idx = int((len(eigenvalues)+1)*(0.5))
    

    energy_range = range(start_idx, stop_idx)
    for x, eigvalue in zip(energy_range, eigenvalues):
        _logger.info("%s ---> %s ---> %s", x, eigvalue, eigenvals_with_matrix[eigvalue])
        all_outputs.append((x, eigvalue, eigenvals_with_matrix[eigvalue]))

    return all_outputs