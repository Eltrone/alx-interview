#!/usr/bin/python3
"""
Détermine le nombre minimal de pièces pour un montant total.
"""


def makeChange(coins, total):
    """
    Utilise une approche gloutonne pour calculer le nombre minimal de pièces.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)  # Trie les pièces en décroissant
    sum_current = 0  # Somme actuelle
    num_coins = 0  # Compteur de pièces

    for coin in coins:
        while sum_current + coin <= total:
            sum_current += coin
            num_coins += 1
            if sum_current == total:
                return num_coins

    return -1  # Retourne -1 si le total ne peut être atteint


# Exemple d'utilisation
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Devrait retourner 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Devrait retourner -1
