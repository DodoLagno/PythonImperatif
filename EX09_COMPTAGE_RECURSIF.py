# ex09_comptageRecursif.py

def compte_elements_dans_plage_recursive(liste, min_val, max_val):
    count = 0
    for element in liste:
        if isinstance(element, int) and min_val <= element <= max_val:
            count += 1
        elif isinstance(element, list):
            count += compte_elements_dans_plage_recursive(element, min_val, max_val)
    return count

# Exemple d'utilisation
exemple_liste = [28, [12, [13, 1], -2, [[4, 5], -5]]]
min_val = 10
max_val = 15
resultat = compte_elements_dans_plage_recursive(exemple_liste, min_val, max_val)
print(f"Le nombre d'éléments entre {min_val} et {max_val} est :", resultat)
