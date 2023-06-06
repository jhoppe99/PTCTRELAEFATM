# main python file, for now running script
# just check if proper version of all dependencies
# are installed properly
import numpy as np

from version_checker import VersionCheck
from computations import DetOfMatrixCalculation

arr = np.array([
    [2, 2, 12, 102, 0, 8],
    [7, 2, 6, 76, 0, 16],
    [1, 12, 4, 89, 76, 5],
    [5, 96, 12, 43, 21, 2],
    [4, 64, 32, 64, 98, 0],
    [56, 921, 86, 1, 93, 7]
])

vc = VersionCheck(are_versions_ok=False)
det = DetOfMatrixCalculation(arr=arr)


def graetings_ver_check():
    print("\n\n*--------------------------------------------------*")
    print("|            Welcome! This is program              |")
    print("|    to calculate the rotational energy levels     |")
    print("|   and eigenvectors for asymmetric top molecules  |")
    print("*--------------------------------------------------*")
    print(f"\nYour dependencies status: \n{vc.print_version_checker_output()}")


def matrix_determinant():
    print('\n\n*---------------------------------------------*')
    print('| Numerical calcualtion of matrix determinant |')
    print('*---------------------------------------------*\n')
    print(f'The determinant of the matrix:\n\n {arr}\n\nis: {det.calculate_determinant()}\n')
    print(f'Rounded determinant is: {det.round_determinant()}\n')


def main():
    graetings_ver_check()
    matrix_determinant()


if __name__ == "__main__":

    main()
