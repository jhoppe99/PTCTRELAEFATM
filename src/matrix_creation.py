from math import sqrt
import numpy as np


class BasicMatrixes:
    """Class for building H_0 and H_1 matrixes, which are base for further factorized submatrices."""
    def __init__(self, A: float, B: float, C: float, K: int) -> None:
        """Class constructor."""
        self.A = A
        self.B = B
        self.C = C
        self.K = K

    def _i_and_j_equal(self, i: int) -> float:
        """Calculate H_ii matrix element.
        
        Args:
            i: element position in matrix.

        Returns:
            Value of matrix element on given position.       
        """
        return 0.5 * (self.A + self.B) * (self.K * (self.K + 1) - (i * i)) + self.C * (i * i)

    def _j_bigger_than_i_by_2(self, i: int) -> float:
        """Calculate H_i,i+2 matrix element.
        
        Args:
            i: element position in matrix.

        Returns:
            Value of matrix element on given position.
        """       
        return 0.25 * (self.B - self.A) * (self.K - i) * (self.K - i - 1) * (self.K + i + 1) * (self.K + i + 2)

    def _j_smaller_than_i_by_2(self, i: int) -> float:
        """Calculate H_i,i-2 matrix element.
        
        Args:
            i: element position in matrix.

        Returns:
            Value of matrix element on given position.
        """
        return 0.25 * (self.B - self.A) * (self.K + i) * (self.K + i - 1) * (self.K - i + 1) * (self.K - i + 2)

    def _create_matrix_base(self) -> None:
        """Create matrix base, with calculated all elements.

        This base will be further use to build H_0 and H_1 matrixes.

        Returns:
            Matrix which will be used to create H_0 and H_1 matrixes.
        """
        arr = np.zeros((abs(self.K), abs(self.K)), np.float64)
        for i in range(0, arr.shape[0]):
            for j in range(0, arr.shape[1]):
                if i == j:
                    arr[i][j] = self._i_and_j_equal(i=i)
                elif j == i+2:
                    arr[i][j] = self._j_bigger_than_i_by_2(i=i)
                elif j == i-2:
                    arr[i][j] = self._j_smaller_than_i_by_2(i=i)
        
        return arr

    def create_H0_matrix(self) -> np.array:
        """Create H_0 matrix.

        Returns:
            H_0 matrix.
        """
        arr = self._create_matrix_base()
        if arr.shape[0] > 1 and arr.shape[1] > 1:
            arr[1][1] += self._j_smaller_than_i_by_2(1)
        if arr.shape[0] > 2 and arr.shape[1] > 2:
            arr[0][2] = arr[0][2] * sqrt(2)
            arr[2][0] = arr[2][0] * sqrt(2) 

        return arr

    def create_H1_matrix(self) -> np.array:
        arr = self._create_matrix_base()
        arr = np.delete(np.delete(arr, 0, axis=0), 0, axis=1)
        arr[0][0] -= self._j_bigger_than_i_by_2(-1)
        
        return arr
        
        
class FactorizedSubmatrices():
        """Class containing mathods creating submatices."""

        def create_e_plus_matrix(arr: np.array) -> np.array:
            """Create E^+ matrix.

            The H_0 matrix is required in order to delete every 2 axises.

            Returns:
                E^+ matrix.
            """
            for x in range(1, arr.shape[0]):
                if x < arr.shape[0]:
                    arr = np.delete(np.delete(arr, x, axis=0), x, axis=1)

            return arr
        
        def create_e_minus_matrix(arr: np.array) -> np.array:
            """
            """
            for x in range(0, arr.shape[0]):
                if x < arr.shape[0]:
                    arr = np.delete(np.delete(arr, x, axis=0), x, axis=1)
            
            return arr
        
        def create_o_plus_matrix(arr: np.array) -> np.array:
            """
            """
            for x in range(1, arr.shape[0]):
                if x < arr.shape[0]:
                    arr = np.delete(np.delete(arr, x, axis=0), x, axis=1)

            return arr
        
        def create_o_minus_matrix(arr: np.array) -> np.array:
            pass
        # def
        # e_plus = np.delete(np.delete(self.arr, 1, axis=0), 1, axis=1)
        # for x in range(2, 5):
        #     e_plus = np.delete(np.delete(e_plus, x, axis=0), 2, axis=1)
        # print(f"E+ arr: \n{e_plus}")        

        # return e_plus

    # def _get_E_minus_matrix(self) -> np.array:
    #     e_plus = self._get_E_plus_matrix()
    #     e_minus = np.delete(np.delete(e_plus, 0, axis=0), 0, axis=1)
    #     print(f"E- arr: \n{e_minus}")

    #     return e_minus
