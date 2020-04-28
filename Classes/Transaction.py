from Classes.Dettes import Dette
from function.general import save

class Transaction:
    def __init__(self, montant, debiteur, crediteur):
        self. montant = montant
        self.debiteur = debiteur
        self.crediteur = crediteur

    def applyDette(self, dette_list):
        dette_exist = False
        for i in range(0, len(dette_list)):
            if self.debiteur == dette_list[i].payeur:
                if self.crediteur == dette_list[i].beneficiaire:
                    dette_list[i].changeMontant(self.montant)
                    dette_exist = True
                    print("1")
            if self.debiteur == dette_list[i].beneficiaire:
                if self.crediteur == dette_list[i].payeur:
                    dette_list[i].changeMontant((self.montant*(-1)))
                    dette_exist = True
                    print("2")

        if dette_exist == False:
            print('Create new dette')
            new_dette = Dette(self.montant, self.debiteur, self.crediteur)
            dette_list.append(new_dette)

        save("dette", dette_list)
        print(dette_list)
        return dette_list
