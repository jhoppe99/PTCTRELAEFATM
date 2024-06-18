# import numpy as np
# import numpy.linalg as la
# from typing import Any

# K = 5
# J = 1


# class DiagonalsPreparation:

#     def __init__(self, K, A, B, C, J) -> None:
#         self.K = K
#         self.A = A
#         self.B = B
#         self.C = C
#         self.J = J

#     def looping_over_k1(self):
#         big_diagonal = []
#         for k1 in range(0, self.K):
#             big_diagonal.append(self.looping_over_k2(k1=k1))
#         return big_diagonal

#     def looping_over_k2(self, k1: int) -> list:
#         small_diagonal = []
#         for k2 in range(0, self.K):
#             if k1 == k2:
#                 small_diagonal.append(self.equal_ks_equation(k1, k2))
#             else:
#                 small_diagonal.append(self.not_equal_ks_equation(k1, k2))
#         return small_diagonal

#     def equal_ks_equation(self, k1: int, k2: int) -> float:
#         eq = 0.5 * (self.A + self.B) * (self.J * (self.J + 1) - (k1 * k1)) + (self.C * (k1 * k1))
#         return eq

#     def not_equal_ks_equation(self, k1: int, k2: int) -> int:
#         eq = 0.25 * (self.B - self.A) * (self.J - k1) * (self.J - k1 - 1) * (self.J + k1 + 1) * (self.J + k1 + 2)
#         return eq


# class MatrixesCreation:
#     def __init__(self, diagonals: list) -> None:
#         self.diagonals = diagonals

#     def access_all_diagonals(self) -> list:
#         print(self.diagonals)

#     def access_particual_list(self, j):
#         return self.diagonals[j]

#     def create_matrix(self) -> np.array:
#         for j in range(0, len(self.diagonals)):
#             diagonal = self.access_particual_list(j=j)
#             self.calcualte_eigenvalues(np.diag(diagonal))
#             print(np.diag(diagonal))
#             print("--------------------------")

#     def calcualte_eigenvalues(self, arr) -> tuple:
#         print(la.eigh(arr))


# tryout = DiagonalsPreparation(K=5, A=0.25, B=0.3, C=0.4, J=0.5)
# separate = MatrixesCreation(diagonals=tryout.looping_over_k1())
# separate.create_matrix()

A = 2
B = 3
C = 1
J = 5

arr = [[0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0]]

# E_plus = [[0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0]]

for x in arr:
    print(x)


def i_and_j_equal(i: int, j: int):
    eq = 0.5 * (A + B) * (J * (J + 1) - (i * i)) + C * (i * i)
    arr[i][j] = eq
    return eq


def j_bigger_than_i_by_2(i: int, j: int):
    eq = 0.25 * (B - A) * (J - i) * (J - i - 1) * (J + i + 1) * (J + i + 2)
    arr[i][j] = eq
    return eq


def j_smaller_than_i_by_2(i: int, j: int):
    eq = 0.25 * (B - A) * (J + i) * (J + i - 1) * (J - i + 1) * (J - i + 2)
    arr[i][j] = eq
    return eq


for i in range(0, 7):
    for j in range(0, 7):
        if i == j:
            print(f"FOR i={i} and j={j}")
            print(i_and_j_equal(i=i, j=j))
        elif j == i+2:
            print(f"FOR i={i} and j={j}")
            print(j_bigger_than_i_by_2(i=i, j=j))
        elif j == i-2:
            print(f"FOR i={i} and j={j}")
            print(j_smaller_than_i_by_2(i=i, j=j))

for x in arr:
    print(x)

E_plus = arr
print("-----------------")
for y in E_plus:
    print(y)
for k in range(0, 4):
    for n in range(0, 4):
        print(k)
        print(n)
        if k % 2 != 0 and n % 2 != 0 or E_plus[k][n] == 0:
            del E_plus[k][n]

print(E_plus)
