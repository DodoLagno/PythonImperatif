# ex04_rechercheMin.py

liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]

# Recherche du plus petit élément sans utiliser la fonction min
min_element = liste[0]
for element in liste:
    if element < min_element:
        min_element = element

# Affichage du plus petit élément
print("Le plus petit élément de la liste est :", min_element)
