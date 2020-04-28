from Classes.Transaction import Transaction



def transactions(users_list, dette_list):
    i = 1
    for user in users_list:
        print(str(i) + " - " + user.nom + " " + user.prenom)
        i += 1

    crediteur = int(input("Qui a payé ? ")) - 1
    debiteur = int(input("Pour qui ? ")) - 1
    montant = int(input("Combien ? "))

    print(users_list[crediteur].prenom + " " + users_list[crediteur].nom + " a payé " + str(montant) + "€ pour " +
          users_list[debiteur].prenom + " " + users_list[debiteur].nom + ".")
    goodcheck = False
    while goodcheck == False:
        check = input("Valide-tu ? [y/n] ")
        if check.lower() == "y":
            goodcheck = True
            newTransaction = Transaction(montant, debiteur, crediteur)
            dette_list = newTransaction.applyDette(dette_list)
        elif check.lower() == "n":
            goodcheck = True
