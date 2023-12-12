# ex03_rechercheMax.py

liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]

# Recherche du plus grand élément sans utiliser la fonction max
max_element = liste[0]
for element in liste:
    if element > max_element:
        max_element = element

# Affichage du plus grand élément
print("Le plus grand élément de la liste est :", max_element)
