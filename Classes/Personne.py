#Classe définissant une partie
import pickle

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

    def modifyPrenom(self, value):
        self.prenom = value

    def modifyNom(self, value):
        self.nom = value

    def modifyRib(self, value):
        self.rib = value

    def modifyMail(self, value):
        self.mail = value

    def modifyTel(self, value):
        self.tel = value

    def suppr(self, users_list):
        print('yo')

#