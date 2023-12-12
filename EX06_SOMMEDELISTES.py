# ex06_sommeDeListes.py

liste1 = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
liste2 = [-1, 12, 17, 14, 5, -9, 0, 18, -6, 0, 4, -13, 5, 7, -2, 8, -1]

# Création de la liste résultat
resultat = [a + b for a, b in zip(liste1, liste2)]

# Affichage des valeurs de la liste résultat avec une boucle
for element in resultat:
    print(element)
