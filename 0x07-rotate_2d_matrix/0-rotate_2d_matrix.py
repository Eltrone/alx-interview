#!/usr/bin/python3
"""
Implémentation de la fonction rotate_2d_matrix pour pivoter une matrice de 90 degrés dans le sens horaire.
"""

def rotate_2d_matrix(matrix):
    n = len(matrix)
    
    # Transposer la matrice
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Inverser chaque colonne
    for i in range(n):
        for j in range(n // 2):
            matrix[j][i], matrix[n - j - 1][i] = matrix[n - j - 1][i], matrix[j][i]

# Test de la fonction
if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    rotate_2d_matrix(matrix)
    print(matrix)  # Devrait afficher [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
