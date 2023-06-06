import matplotlib as plt
import numpy as np
import pandas as pd
import pytest


class VersionCheck:
    def __init__(self, are_versions_ok: bool):
        self.are_versions_ok = are_versions_ok

    def check_dependencies_version(self):
        if (np.__version__ == "1.24.2"
            and pd.__version__ == "1.5.3"
            and plt.__version__ == "3.7.1"
            and pytest.__version__ == "7.2.2"):
            self.are_versions_ok = True
            return self.are_versions_ok
        else:
            self.are_versions_ok = False
            return self.are_versions_ok

    def print_version_checker_output(self):
        self.check_dependencies_version()
        if self.are_versions_ok is True:
            return "All dependencies have been downloaded in proper versions!"
        else:
            return "One or more of dependencies has wrong version!"


class DetOfMatrixCalculation:
    def __init__(self, arr: np.array) -> None:
        self.arr = arr

    def calculate_determinant(self) -> float:
        determinant = np.linalg.det(self.arr)
        return determinant
