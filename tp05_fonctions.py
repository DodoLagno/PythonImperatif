# EXERCICE EX01_SOMME_NB_PAIRS
def somme_nombres_pairs(liste):
    return sum(nombre for nombre in liste if nombre % 2 == 0)

# Exemple d'utilisation EX01
liste_test_ex01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultat_somme_pairs = somme_nombres_pairs(liste_test_ex01)
print("EX01 - Somme des nombres pairs :", resultat_somme_pairs)

# EXERCICE EX02_PALINDROME
def est_palindrome(chaine):
    chaine = chaine.lower()  # Ignorer la casse
    return chaine == chaine[::-1]

# Exemple d'utilisation EX02
chaine_test_ex02 = "bob"
resultat_palindrome = est_palindrome(chaine_test_ex02)
print(f"EX02 - '{chaine_test_ex02}' est un palindrome : {resultat_palindrome}")

# EXERCICE EX03_RECHERCHEMINMAX
def recherche_min_max(minimum, maximum, liste):
    return [nombre for nombre in liste if minimum <= nombre <= maximum]

# Exemple d'utilisation EX03
liste_test_ex03 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min_value_ex03 = 3
max_value_ex03 = 8
resultat_recherche_min_max = recherche_min_max(min_value_ex03, max_value_ex03, liste_test_ex03)
print(f"EX03 - Éléments entre {min_value_ex03} et {max_value_ex03} inclus :", resultat_recherche_min_max)

# EXERCICE EX04_CALCULMOYENNE
def calcul_moyenne(liste):
    if not liste:
        return None  # Retourner None si la liste est vide pour éviter une division par zéro
    return sum(liste) / len(liste)

# Exemple d'utilisation EX04
liste_test_ex04 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultat_moyenne = calcul_moyenne(liste_test_ex04)
print("EX04 - Moyenne de la liste :", resultat_moyenne)
