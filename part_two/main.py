# --- PARTIE 2 ---
# Créer un script python qui va contenir un dictionnaire (par exemple une personne, avec des attributs comme l'âge, le prénom, le genre...)
# Retourner ce dictionnaire sous forme d'objet JSON dans le terminal (voir le package 'json' pour plus d'info)
# /!\ En POO également, vous devez initialiser le dictionnaire soit dans le constructeur soit avec un setter après instanciation de la classe /!\
import json

class PartTwo:

    def __init__(self): 
        self.person = { 
            "name": "John",
            "age": 36,
            "country": "Norway"
        }

    def get_person_json(self):
        """
            Return json formated dump of person dict
            This will be used for scanning other computers on LAN.

            Returns:
                json: json formated dump of person dict
        """
        return json.dumps(self.person, indent=4, sort_keys=True)
