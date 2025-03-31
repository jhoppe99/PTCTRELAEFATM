from math import sqrt
import numpy as np


class H0andH1matrices:
    """Class for building H0 and H1 matrixes, which are base for further factorized submatrices."""

    def __init__(self, A: float, B: float, C: float, J: int) -> None:
        """Class constructor."""
        self.A = A
        self.B = B
        self.C = C
        self.J = J

    def _i_and_j_equal(self, i: int) -> float:
        """Calculate H_ii matrix element.

        Args:
            i (int): element position in matrix.

        Returns:
            float: value of matrix element on given position.
        """
        return 0.5 * (self.A + self.B) * (
            self.J * (self.J + 1) - (i * i)
        ) + self.C * (i * i)

    def _j_bigger_than_i_by_2(self, i: int) -> float:
        """Calculate H_i,i+2 matrix element.

        Args:
            i (int): element position in matrix.

        Returns:
            float: value of matrix element on given position.
        """
        return (
            0.25
            * (self.A - self.B)
            * sqrt(
                (self.J - i)
                * (self.J - i - 1)
                * (self.J + i + 1)
                * (self.J + i + 2)
            )
        )

    def _j_smaller_than_i_by_2(self, i: int) -> float:
        """Calculate H_i,i-2 matrix element.

        Args:
            i (int): element position in matrix.

        Returns:
            float: value of matrix element on given position
        """
        return (
            0.25
            * (self.A - self.B)
            * sqrt(
                (self.J + i)
                * (self.J + i - 1)
                * (self.J - i + 1)
                * (self.J - i + 2)
            )
        )

    def _create_matrix_base(self) -> None:
        """Create matrix base, with calculated all elements.

        This base will be further use to build H_0 and H_1 matrixes.

        Returns:
            np.array: matrix which will be used to create H_0 and H_1 matrixes
        """
        arr = np.zeros((abs(self.J + 1), abs(self.J + 1)), np.float64)
        for i in range(0, arr.shape[0]):
            for j in range(0, arr.shape[1]):
                if i == j:
                    arr[i][j] = self._i_and_j_equal(i=i)
                elif j == i + 2:
                    arr[i][j] = self._j_bigger_than_i_by_2(i=i)
                elif j == i - 2:
                    arr[i][j] = self._j_smaller_than_i_by_2(i=i)

        return arr

    def get_H0_matrix(self) -> np.array:
        """Get H0 matrix from modifying some elements of matrix base.

        Returns:
            np.array: H0 matrix
        """
        arr = self._create_matrix_base()
        if arr.shape[0] > 1 and arr.shape[1] > 1:
            arr[1][1] += self._j_smaller_than_i_by_2(1)
        if arr.shape[0] > 2 and arr.shape[1] > 2:
            arr[0][2] *= sqrt(2)
            arr[2][0] *= sqrt(2)

        return arr

    def get_H1_matrix(self) -> np.array:
        """Get H1 matrix for deleting first row and first column from matrix base.

        Returns:
            np.array: H1 matrix
        """
        arr = self._create_matrix_base()
        arr = np.delete(np.delete(arr, 0, axis=0), 0, axis=1)

        return arr


class EplusEminusOplusOminusSubmatrices:
    """Class containing methods creating submatices."""

    def __init__(self, A: float, B: float, C: float, J: int) -> None:
        """Class constructor."""
        self.A = A
        self.B = B
        self.C = C
        self.J = J

    def _j_bigger_than_i_by_2(self, i: int) -> float:
        """Calculate H_i,i+2 matrix element.

        Args:
            i (int): element position in matrix

        Returns:
            float: value of matrix element on given position
        """
        return (
            0.25
            * (self.A - self.B)
            * sqrt(
                (self.J - i)
                * (self.J - i - 1)
                * (self.J + i + 1)
                * (self.J + i + 2)
            )
        )

    def get_e_plus_submatrix(self, arr: np.array) -> np.array:
        """Get E+ submatrix from deleting specific rows and columns from H0 matrix.

        Args:
            arr (np.array): H0 matrix

        Returns:
            np.array: E+ submatrix
        """
        for x in range(1, arr.shape[0]):
            if x < arr.shape[0]:
                arr = np.delete(np.delete(arr, x, axis=0), x, axis=1)

        return arr

    def get_e_minus_submatrix(self, arr: np.array) -> np.array:
        """Get E- submatrix from deleting first row and first column from E+ submatrix.

        Args:
            arr (np.array): E+ submatrix

        Returns:
            np.array: E- submatrix
        """
        arr = np.delete(np.delete(arr, 0, axis=0), 0, axis=1)

        return arr

    def get_o_plus_submatrix(self, arr: np.array) -> np.array:
        """Get O+ submatrix from deleting specific rows and columns from H1 matrix.

        Args:
            arr (np.array): H1 matrix

        Returns:
            np.array: O+ submatrix
        """
        print(arr)
        for x in range(1, arr.shape[0]):
            if x < arr.shape[0]:
                arr = np.delete(np.delete(arr, x, axis=0), x, axis=1)
        print(f"ARRAY from O+ {arr}")
        if len(arr) > 0 and len(arr[0]) > 0:
            arr[0][0] += self._j_bigger_than_i_by_2(-1)

        return arr

    def get_o_minus_submatrix(self, arr: np.array) -> np.array:
        """Get O- submatrix from deleting specific rows and columns from H1 matrix.

        Args:
            arr (np.array): H1 matrix

        Returns:
            np.array: O- submatrix
        """
        print(arr)
        for x in range(1, arr.shape[0]):
            if x < arr.shape[0]:
                arr = np.delete(np.delete(arr, x, axis=0), x, axis=1)
        print(f"ARRAY from O- {arr}")
        if len(arr) > 0 and len(arr[0]) > 0:
            arr[0][0] -= self._j_bigger_than_i_by_2(-1)

        return arr
