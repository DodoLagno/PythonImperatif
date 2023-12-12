# ex08_fonctionRecursive.py

def compte_entiers_recursive(liste):
    count = 0
    for element in liste:
        if isinstance(element, int):
            count += 1
        elif isinstance(element, list):
            count += compte_entiers_recursive(element)
    return count

# Exemple d'utilisation
exemple_liste = [28, [12, [13, 1], -2, [[4, 5], -5]]]
resultat = compte_entiers_recursive(exemple_liste)
print("Le nombre d'entiers dans la liste est :", resultat)
