class Dette:
    def __init__(self, montant, payeur, beneficiaire):
        self.montant = montant
        self.payeur = payeur
        self.beneficiaire = beneficiaire

    def diminuer(self, valeur):
        self.montant -= valeur