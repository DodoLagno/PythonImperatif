# Déclaration de la liste
liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]

# Affichage de tous les éléments de la liste avec une boucle
print("Tous les éléments de la liste :")
for element in liste:
    print(element)

# Affichage des éléments positifs de la liste avec une boucle et un if
print("\nÉléments positifs de la liste :")
for element in liste:
    if element > 0:
        print(element)

# Calcul du nombre d'éléments positifs et affichage
nombre_elements_positifs = sum(1 for element in liste if element > 0)
print("\nNombre d'éléments positifs :", nombre_elements_positifs)
