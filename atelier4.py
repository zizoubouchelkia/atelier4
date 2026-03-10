class Employe:
    def __init__(self, numero_permis, nom, prenom):
        self.numero_permis = numero_permis
        self.nom = nom
        self.prenom = prenom
        self.voiture_service = None

    def afficher_informations(self):
        print("Employe :")
        print("Numero de permis :", self.numero_permis)
        print("Nom :", self.nom)
        print("Prenom :", self.prenom)

        if self.voiture_service is not None:
            print("Voiture de service attribuee :")
            print("  Matricule :", self.voiture_service.matricule)
            print("  Annee :", self.voiture_service.annee)
            print("  Marque :", self.voiture_service.marque)
            print("  Kilometrage :", self.voiture_service.kilometrage)
        else:
            print("Aucune voiture de service attribuee.")
        print("-" * 40)

    def affecter_voiture(self, voiture):
        if self.voiture_service is not None:
            print(self.prenom, self.nom, "a deja une voiture.")
        elif voiture.chauffeur is not None:
            print("Cette voiture est deja attribuee a un autre employe.")
        else:
            self.voiture_service = voiture
            voiture.chauffeur = self
            print("Voiture attribuee a", self.prenom, self.nom)

    def retirer_voiture(self):
        if self.voiture_service is None:
            print(self.prenom, self.nom, "n'a aucune voiture a retirer.")
        else:
            self.voiture_service.chauffeur = None
            self.voiture_service = None
            print("Voiture retiree de", self.prenom, self.nom)

class Voiture:
    def __init__(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None

    def afficher_informations(self):
        print("Voiture :")
        print("Matricule :", self.matricule)
        print("Annee :", self.annee)
        print("Marque :", self.marque)
        print("Kilometrage :", self.kilometrage)

        if self.chauffeur is not None:
            print("Employe associe :")
            print("  Numero de permis :", self.chauffeur.numero_permis)
            print("  Nom :", self.chauffeur.nom)
            print("  Prenom :", self.chauffeur.prenom)
        else:
            print("Aucun employe associe.")
        print("-" * 40)