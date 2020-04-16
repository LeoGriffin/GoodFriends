from Classes.Personne import Person
from Classes.Transaction import Transaction
from Classes.Dettes import Dette
import os
import pickle
import json

def save(users_list):
    with open("data/person.dat", "wb") as f:
        pickle.dump(len(users_list), f)
        for value in users_list:
            pickle.dump(value, f)

#leo = Person(0, 'Griffin', 'Léo', 'FR76', 'leogriffin@hotmail.fr', '0769196079')
#users_list = [leo]
#save(users_list)

users_list = []
with open("data/person.dat", "rb") as f:
    for _ in range(pickle.load(f)):
        users_list.append(pickle.load(f))

run = True
while run:
    print("Good Friends")
    print("==============================================")

    print("\n")
    print("1 - Gerer les utilisateurs")
    print("2 - Ajouter une transaction")
    print("3 - Afficher mes dettes")
    print("4 - Afficher ce qu'on me doit")
    print("5 - Quitter")
    choice = int(input("Choisit une action : "))

    if choice == 1:
        print("--------------------------------------")
        print("Gestion des utilisateurs")
        print("\n0 - Ajouter un utilisateur")
        i = 1
        for user in users_list:
            print(str(i) + " - " + user.nom + " " + user.prenom)
            i += 1

        choice_users = int(input("Choisit un utilisateur ou une action : ")) - 1
        if choice_users == (-1):
            nom = input('Nom : ')
            prenom = input('Prénom : ')
            rib = input('RIB : ')
            mail = input('Mail : ')
            tel = input('Tel : ')
            newPerson = Person((users_list[len(users_list)-1].id +1), nom, prenom, rib, mail, tel)
            users_list.append(newPerson)
            save(users_list)

        else:

            mod_menu = True
            while mod_menu:
                print("\n" + users_list[choice_users].prenom + " " + users_list[choice_users].nom + " " +
                      users_list[choice_users].rib + " " + users_list[choice_users].mail + " " + users_list[choice_users].tel)
                print("\n1 - Modifier l'utilisateur")
                print("2 - Supprimer l'utilisateur l'utilisateur")
                print("3 - Voir les dettes liées à cette utilisateur")
                print("4 - Retour")
                print("5 - Menu principal")
                choice_user = int(input("Choisit une action : "))

                if choice_user == 1:
                    print("Modification de l'utilisateur")
                    print("1 - Prénom")
                    print("2 - Nom")
                    print("3 - RIB")
                    print("4 - Mail")
                    print("5 - Tel")
                    print("6 - Retour")
                    choice_user_mod = int(input("Choix: "))

                    if choice_user_mod == 1:
                        print("Prénom actuel : " + users_list[choice_users].prenom)
                        value = input("Nouveau prénom : ")
                        users_list[choice_users].modifyPrenom(value)
                        print("Le prénom a bien été remplacé par " + users_list[choice_users].prenom)
                        save(users_list)

                    elif choice_user_mod == 2:
                        print("Nom actuel : " + users_list[choice_users].nom)
                        value = input("Nouveau nom : ")
                        users_list[choice_users].modifyNom(value)
                        print("Le nom a bien été remplacé par " + users_list[choice_users].nom)
                        save(users_list)

                    elif choice_user_mod == 3:
                        print("RIB actuel : " + users_list[choice_users].rib)
                        value = input("Nouveau RIB : ")
                        users_list[choice_users].modifyRib(value)
                        print("Le RIB a bien été remplacé par " + users_list[choice_users].rib)
                        save(users_list)

                    elif choice_user_mod == 4:
                        print("Mail actuel : " + users_list[choice_users].mail)
                        value = input("Nouveau mail : ")
                        users_list[choice_users].modifyMail(value)
                        print("Le mail a bien été remplacé par " + users_list[choice_users].mail)
                        save(users_list)

                    elif choice_user_mod == 5:
                        print("Numéro de téléphone actuel : " + users_list[choice_users].tel)
                        value = input("Nouveau tel : ")
                        users_list[choice_users].modifyTel(value)
                        print("Le numéro de téléphone a bien été remplacé par " + users_list[choice_users].tel)
                        save(users_list)

                    elif choice_user_mod == 6:
                        mod_menu = False

                elif choice_user == 2:
                    double_touch = input("Voulez-vous vraiment supprimer " + users_list[choice_users].prenom + " " +
                                         users_list[choice_users].nom + " ? (y/N)   ")
                    if double_touch.lower() == "y":
                        del users_list[choice_users]
                        save(users_list)
                        mod_menu = False

    elif choice == 5:
        run = False