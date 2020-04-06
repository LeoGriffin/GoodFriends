#Classe définissant une partie
import os
import simplejson as json

class Person:
#Props : nom, prénom, RIB, mail, num
#Fonctions : infos
    def __init__(self, id, nom, prenom, rib, mail, tel):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.rib = rib
        self.mail = mail
        self.tel = tel

    def save(self):
        data = {"id": self.id, "data": {"nom": self.nom, "prenom": self.prenom, "rib": self.rib, "mail": self.mail, "tel": self.tel}}
        #data = {"id": self.id, "data": {data}}
        person_file = open("data/person.json", "+a")
        person_file.write(json.dumps(data) + "\n")
        person_file.close()

    def modify(self):
        old_file = open("data/person.json", "+w")
        print(json.dumps(old_file))
