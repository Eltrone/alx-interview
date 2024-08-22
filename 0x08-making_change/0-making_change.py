#!/usr/bin/python3
"""
Définit fonction makeChange pour déterminer nombre minimal de pièces
nécessaires pour obtenir montant donné avec liste de dénominations de pièces.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    # Initialisation d'un tableau pour le stockage des résultats intermédiaires
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Calcul pour chaque sous-total de 1 à 'total'
    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Retourne -1 si aucune combinaison de pièces ne peut former le total
    return dp[total] if dp[total] != float('inf') else -1


# Exemple d'utilisation de la fonction dans un script principal
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Doit retourner 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Doit retourner -1
