import pickle
from Classes.Personne import Person
from function.general import save


def LogIn(users_list):
    print("Connexion")
    print("-------------")
    while True == True:
        cred_mail = input("Adresse mail : ")
        for i in range (0, len(users_list)):
            if cred_mail == users_list[i].mail:
                print("Bonjour " + users_list[i].prenom + " " + users_list[i].nom + ".\n")
                return users_list[i].id
        print("Aucun correspondance trouvée. Veuillez réessayer.\n")

def add(users_list):
    nom = input('Nom : ')
    prenom = input('Prénom : ')
    rib = input('RIB : ')
    mail = input('Mail : ')
    tel = input('Tel : ')
    return Person((users_list[len(users_list) - 1].id + 1), nom, prenom, rib, mail, tel)


def modif(users_list, choice_users):
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
        return False


def suppr(users_list, choice_users):
    double_touch = input("Voulez-vous vraiment supprimer " + users_list[choice_users].prenom + " " +
                         users_list[choice_users].nom + " ? (y/N)   ")
    if double_touch.lower() == "y":
        del users_list[choice_users]
        save(users_list)


def dette_user(users_list, choice_users, dette_list):
    user_id = users_list[choice_users].id
    result = False
    for i in range(0, len(dette_list)):
        if user_id == dette_list[i].payeur:
            dette_list[i].display(users_list)
            result = True
    if result == False:
        print("Aucune dette trouvée.")


def usersManagement(users_list, dette_list):
    users_menu = True
    while users_menu:
        print("--------------------------------------")
        print("Gestion des utilisateurs")
        print("\n0 - Ajouter un utilisateur")
        i = 1
        for user in users_list:
            print(str(i) + " - " + user.nom + " " + user.prenom)
            i += 1

        choice_users = int(input("Choisit un utilisateur ou une action : ")) - 1
        if choice_users == (-1):
            newPerson = add(users_list)
            users_list.append(newPerson)
            save(users_list)

        else:

            user_menu = True
            while user_menu:
                print("\n" + users_list[choice_users].prenom + " " + users_list[choice_users].nom + " " +
                      users_list[choice_users].rib + " " + users_list[choice_users].mail + " " + users_list[
                          choice_users].tel + "id: " + str(users_list[choice_users].id))
                print("\n1 - Modifier l'utilisateur")
                print("2 - Supprimer l'utilisateur l'utilisateur")
                print("3 - Voir les dettes liées à cette utilisateur")
                print("4 - Retour")
                print("5 - Menu principal")
                choice_user = int(input("Choisit une action : "))

                if choice_user == 1:
                    mod_menu = True
                    while mod_menu:
                        mod_menu = modif(users_list, choice_users)

                elif choice_user == 2:
                    suppr(users_list, choice_users)
                    user_menu = False

                elif choice_user == 3:
                    dette_user(users_list, choice_users, dette_list)

                elif choice_user == 4:
                    user_menu = False

                elif choice_user == 5:
                    user_menu = False
                    users_menu = False
