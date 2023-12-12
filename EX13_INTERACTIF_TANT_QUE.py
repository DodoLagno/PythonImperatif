nombre_utilisateur = int(input("Entrez un nombre entre 1 et 10 : "))

# Tant que le nombre n'est pas compris entre 1 et 10, redemander
while not (1 <= nombre_utilisateur <= 10):
    print("Nombre non valide, veuillez saisir un nombre entre 1 et 10.")
    nombre_utilisateur = int(input("Entrez un nombre entre 1 et 10 : "))

# Si le nombre est compris entre 1 et 10, loguer le nombre
print("Le nombre saisi est :", nombre_utilisateur)
