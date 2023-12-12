nombres_utilisateur = [float(input(f"Entrez le nombre {i + 1} : ")) for i in range(10)]

# Trouver et afficher le plus grand nombre
plus_grand = max(nombres_utilisateur)
print("Le plus grand nombre saisi est :", plus_grand)
