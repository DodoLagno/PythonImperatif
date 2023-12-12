nombre_utilisateur = int(input("Entrez un nombre entre 1 et 10 : "))

# Tant que le nombre n'est pas compris entre 1 et 10, redemander
while not (1 <= nombre_utilisateur <= 10):
    print("Nombre non valide, veuillez saisir un nombre entre 1 et 10.")
    nombre_utilisateur = int(input("Entrez un nombre entre 1 et 10 : "))

# Loguer la table de multiplication de ce nombre
for i in range(1, 11):
    resultat = nombre_utilisateur * i
    print(f"{nombre_utilisateur} * {i} = {resultat}")
