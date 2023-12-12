import random

def charger_mots():
    mots = []
    with open("mots.txt", "r") as fichier:
        for ligne in fichier:
            mots.append(ligne.strip())
    return mots

def choisir_mot():
    liste_mots = charger_mots()
    return random.choice(liste_mots)

def afficher_mot_cache(mot, lettres_trouvees):
    mot_cache = ""
    for lettre in mot:
        if lettre.isalpha() and lettre.lower() in lettres_trouvees:
            mot_cache += lettre + " "
        elif lettre.isspace():
            mot_cache += " "
        else:
            mot_cache += "_ "
    return mot_cache.strip()

def jouer_pendu():
    mot_a_deviner = choisir_mot()
    max_erreurs = random.randint(5, 10)
    lettres_trouvees = []
    erreurs = 0

    print("Bienvenue dans le jeu du pendu !")
    mot_cache = afficher_mot_cache(mot_a_deviner, lettres_trouvees)
    print(mot_cache)

    while True:
        proposition = input("Proposez une lettre : ").lower()

        if proposition in lettres_trouvees:
            print("Vous avez déjà proposé cette lettre. Essayez à nouveau.")
            continue

        if proposition.lower() in mot_a_deviner.lower():
            lettres_trouvees.append(proposition.lower())
        else:
            erreurs += 1
            print(f"La lettre {proposition} n'est pas dans le mot. Erreurs : {erreurs}/{max_erreurs}")

        mot_cache = afficher_mot_cache(mot_a_deviner, lettres_trouvees)
        print(mot_cache)

        if mot_cache == mot_a_deviner:
            print("Félicitations ! Vous avez trouvé le mot.")
            break

        if erreurs == max_erreurs:
            print(f"Désolé, vous avez dépassé le nombre maximal d'erreurs. Le mot était : {mot_a_deviner}")
            break

    print(f"La réponse était : {mot_a_deviner}")

if __name__ == "__main__":
    jouer_pendu()
