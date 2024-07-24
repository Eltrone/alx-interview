#!/usr/bin/python3
"""
Module to validate UTF-8 encoding.
"""

def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    """
    # Nombre d'octets de continuation attendus.
    continuation_bytes = 0

    for byte in data:
        # Masque pour identifier les bits les plus significatifs de l'octet.
        mask = 0b10000000
        
        if continuation_bytes == 0:
            # Compter le nombre de bits à 1 au début de l'octet.
            while byte & mask:
                continuation_bytes += 1
                mask >>= 1

            # S'il n'y a pas de bits à 1, il s'agit d'un caractère ASCII sur un seul octet.
            if continuation_bytes == 0:
                continue

            # Si le nombre de bits à 1 est 1 ou plus de 4, ce n'est pas valide.
            if continuation_bytes == 1 or continuation_bytes > 4:
                return False

            # Réduire de 1 pour exclure l'octet de démarrage.
            continuation_bytes -= 1
        
        else:
            # Vérifier si l'octet est un octet de continuation.
            if not (byte & 0b10000000 and not (byte & 0b01000000)):
                return False
            
            continuation_bytes -= 1

    # S'il reste des octets de continuation attendus, la chaîne est tronquée.
    return continuation_bytes == 0

# Tests unitaires ou exemples d'usage ici...
