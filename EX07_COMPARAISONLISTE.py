# ex07_comparaisonListe.py

liste1 = [1, 15, -3, 8, 7, 4, -2, 28, -1, 17, 2, 3, 0, 14, -4]
liste2 = [3, -8, 17, 5, -1, 4, 0, 6, 2, 11, -5, -4, 8]

# Nombre de valeurs communes aux deux listes
valeurs_communes = set(liste1) & set(liste2)
nombre_valeurs_communes = len(valeurs_communes)

print("Le nombre de valeurs communes aux deux listes est :", nombre_valeurs_communes)

# Afficher les valeurs communes
print("Les valeurs communes aux deux listes sont :", valeurs_communes)

