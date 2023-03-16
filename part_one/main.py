# --- PARTIE 1 ---
# Créer un script python qui va afficher dans le terminal une phrase aléatoire,
# venant d'un tableau que vous aurez préalablement rempli de quelques citations par exemple
# /!\ En POO même s'il y a peu d'attributs/getters/setters à faire /!\

import random

class PartOne :

    quotes = [
        "Al diel shala = Bon voyage.",
        "Anar'alah = 'Par la lumière.'",
        "Anaria shola = Que puis-je pour vous ?",
        "Anar'endal dracon = Par le souffle du dragon.",
        "Anu belore dela'na = Que le soleil nous guide.",
        "Bal'a dash, malanore = Bienvenue, voyageur.",
        "Ban'dinoriel = 'Gardien de la porte'.",
        "Felo'melorn = 'Choc de flammes'",
        "Medivh = 'Gardien des secrets'",
        "Quel'Zaram = Haute lame.",
    ]

    def get_random_sentence(self):
        return(random.choice(self.quotes))

