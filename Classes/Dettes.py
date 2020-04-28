class Dette:

    def __init__(self, montant, payeur, beneficiaire):
        self.montant = montant
        self.payeur = payeur
        self.beneficiaire = beneficiaire

    def diminuer(self, valeur):
        self.montant -= valeur

    def display(self, users_list):
        payeur = "Utilisateur non trouvé"
        beneficiaire = "Utilisateur non trouvé"
        for i in range (0, len(users_list)):
            if users_list[i].id == self.payeur:
                payeur = users_list[i].prenom + " " + users_list[i].nom
            if users_list[i].id == self.beneficiaire:
                beneficiaire = users_list[i].prenom + " " + users_list[i].nom
        print("Montant : " + str(self.montant) + "   Payeur : " + payeur + "   Bénéficiaire : " + beneficiaire)

    def changeMontant(self, montant):
        self.montant += montant