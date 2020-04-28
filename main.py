from Classes.Personne import Person
from Classes.Dettes import Dette
from function.users_func import usersManagement
from function.transctions_func import transactions
from function.general import save
import pickle

users_list = []
with open("data/person.dat", "rb") as f:
    for _ in range(pickle.load(f)):
        users_list.append(pickle.load(f))

dette_list = []
with open("data/dette.dat", "rb") as f:
    for _ in range(pickle.load(f)):
        dette_list.append(pickle.load(f))


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
        usersManagement(users_list, dette_list)
    elif choice == 2:
        transactions(users_list, dette_list)
    elif choice == 3:
        current_user = 0
        users_list[current_user].currentDettes(dette_list, users_list)
    elif choice == 4:
        current_user = 0
        users_list[current_user].currentCredit(dette_list, users_list)
    elif choice == 5:
        run = False