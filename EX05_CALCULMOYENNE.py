# ex05_calculMoyenne.py

liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]

# Calcul et affichage de la moyenne des valeurs de la liste
moyenne_totale = sum(liste) / len(liste)
print("La moyenne des valeurs de la liste est :", moyenne_totale)

# Calcul et affichage de la moyenne des valeurs positives de la liste uniquement
valeurs_positives = [valeur for valeur in liste if valeur > 0]
moyenne_positives = sum(valeurs_positives) / len(valeurs_positives)
print("La moyenne des valeurs positives de la liste est :", moyenne_positives)
