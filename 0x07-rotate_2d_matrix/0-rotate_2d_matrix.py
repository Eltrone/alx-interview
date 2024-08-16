#!/usr/bin/python3
"""
Fonction pour pivoter une matrice 2D de 90 degrés dans le sens horaire.
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Transposition de la matrice
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Inversion des rangées pour la rotation horaire
    for i in range(n):
        matrix[i].reverse()


# Test de la fonction avec une matrice 3x3
if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    rotate_2d_matrix(matrix)
    print(matrix)  # Attendu: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
