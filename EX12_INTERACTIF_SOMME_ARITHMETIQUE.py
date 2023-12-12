nombre_utilisateur = int(input("Entrez un nombre : "))

# Affichage du nombre
print("Le nombre saisi est :", nombre_utilisateur)

# Calcul de la somme de 1 à ce nombre inclus
somme = sum(range(1, nombre_utilisateur + 1))
print("La somme de 1 à", nombre_utilisateur, "est :", somme)
