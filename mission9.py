"""
Classes fournies pour la mission 9; à compléter par les étudiants.
@author Kim Mens
@version 4 novembre 2021
"""

###############
### ARTICLE ###
###############

"""
Cette classe représente un Article de facture simple,
comprenant un descriptif et un prix.
   
@author Kim Mens
@version 4 novembre 2021
"""

counter = 0

class Article:

    def __init__(self, d, p):
        """
        @pre:  d un string décrivant l'article
               p un float représentant le prix HTVA en EURO d'un exemplaire de cet article 
        @post: Un article avec description d et prix p a été créé.
        Exemple: Article("carte graphique", 119.49)
        """
        self.__description = d
        self.__prix = p

    def description(self):
        """
        @post: retourne la description textuelle décrivant l'article.
        """
        return self.__description

    def prix(self):
        """
        @post: retourne le prix d'un exemplaire de cet article, hors TVA.
        """
        return self.__prix

    def taux_tva(self):
        """
        @post: retourne le taux de TVA (même valeur pour chaque article)
        """
        return 0.21  # TVA a 21%

    def tva(self):
        """
        @post: retourne la TVA sur cet article
        """
        return self.prix() * self.taux_tva()

    def prix_tvac(self):
        """
        @post: retourne le prix d'un exemplaire de cet article, TVA compris.
        """
        return self.prix() + self.tva()

    def __str__(self):
        """
        @post: retourne un string decrivant cet article, au format: "{description}: {prix}"
        """
        return "{0}: {1:.2f} EUR".format(self.description(), self.prix())


###############
### FACTURE ###
###############

"""
Cette classe représente une Facture, sous forme d'une liste d'articles.
   
@author Kim Mens
@version 4 novembre 2021
"""

class Facture:

    def __init__(self, d, a_list):
        """
        @pre  d est un string court décrivant la facture;
              a_list est une liste d'objets de type Article.
        @post Une facture avec une description d et un liste d'articles a_list été crée.
        Exemple: Facture("PC Store - 22 novembre", [ Article("carte graphique", 119.49) ])
        """
        self.__description = d
        self.__articles = a_list

    def description(self):
        """
        @post: retourne la description de cette facture.
        """
        return self.__description

    def articles(self):
        return self.__articles

    def __str__(self):
        """
        @post: retourne la représentation string d'une facture, à imprimer avec la méthode print().
        (Consultez l'énoncé pour un exemple de la représentation string attendue.)
        """
        s = self.entete_str()
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.__articles:
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA)

        return s

    def entete_str(self):
        global counter
        """
        @post: retourne une représentation string de l'entête de la facture, comprenant le descriptif
               et les entêtes des colonnes.
        """
        counter += 1
        return "Facture No " + str(counter) + " : " + self.__description + "\n" \
               + self.barre_str() \
               + "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description", "prix HTVA", "TVA", "prix TVAC") \
               + self.barre_str()

    def barre_str(self):
        """
        @post: retourne un string représentant une barre horizontale sur la largeur de la facture
        """
        barre_longeur = 83
        return "=" * barre_longeur + "\n"

    def article_str(self, art):
        """
        @pre:  art une instance de la classe Article
        @post: retourne un string correspondant à une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.prix(), art.tva(),
                                                                         art.prix_tvac())

    def totaux_str(self, prix, tva):
        """
        @pre:  prix un float représentant le prix total de la facture en EURO
               tva un float représentant le TVA total de la facture en EURO
        @post: retourne un string représentant une ligne de facture avec les totaux prix et tva,
               à imprimer en bas de la facture
        """
        return self.barre_str() \
               + "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format("T O T A L", prix, tva, prix + tva) \
               + self.barre_str()

    # Cette méthode doit être ajouté lors de l'étape 2.5 de la mission    
    def nombre(self, pce):
        """
        @pre:  pce une instance de la classe Piece
        @post: retourne le nombre d'articles de type ArticlePiece dans la facture,
               faisant référence à une pièce qui est égale à pce,
               en totalisant sur tous les articles qui contiennent une telle pièce.
        """
        same_piece = 0
        for word in self.articles():
            if pce == word:
                same_piece += 1
            else:
                continue
        return same_piece



    # Cette méthode doit être ajouté lors de l'étape 2.6 de la mission    
    def livraison_str(self):
        """
        Cette méthode est une méthode auxiliaire pour la méthode printLivraison
        """
        pass


#########################
### ARTICLEREPARATION ###
#########################
class ArticleReparation(Article):

    def __init__(self, d, p, duration: float):
        super().__init__(d, p)
        self.duration = duration

    def description(self):
        return f"Réparation ({self.duration} heures)"

    def prix(self):
        return 20 + (35*self.duration)


class Piece:
    def __init__(self, string: str, montant: float, kg: float, fragilité=False, taux_tva_reduite=False):
        self.__string = string
        self.__montant = montant
        self.__kg = kg
        self.__fragilité = fragilité
        self.__taux_tva_reduite = taux_tva_reduite

    def description(self):
        return self.__string

    def prix(self):
        return self.__montant

    def poids(self):
        return self.__kg

    def fragile(self):
        return self.__fragilité

    def tva_reduite(self):
        return self.__taux_tva_reduite

    def __eq__(self, other):
        return self.description() == other.description() and self.prix() == other.prix()


class ArticlePiece(Article):
    def __init__(self, d, p, piece_number, piece_obj):
        super().__init__(d, p)
        self.__number = piece_number
        self.piece_obj = piece_obj

    def tva_ou_pas(self):
        return self.piece_obj.tva_reduite()

    def nombre(self):
        return self.__number

    def prix_piece(self):
        return super().prix()

    def description(self):
        return f"{self.nombre()} * {super().description()} @ {float(super().prix())}"

    def prix(self):
        return self.nombre() * super().prix()

    def taux_tva(self):
        if self.piece_obj.tva_reduite() == True:
            return 0.06
        else:
            return 0.21


a = Facture("Gaming", [Article("Carte Graphique RTX 3090", 1099.99)])
b = Facture("Gaming", [Article("Carte Graphique RTX 3090", 1099.99), Article("Carte Graphique RTX 3090", 1099.99)])
g = Piece("Carte Graphique RTX 3090", 1099.99, 3, True, False)
g2 = ArticlePiece("souris bluetooth", 15.99, 3, g)
print(a)
print(b)



#############
### PIECE ###
#############

# Cette classe doit être ajouté lors de l'étape 2.3 de la mission    

####################
### ARTICLEPIECE ###
####################




########################
### RUNNING THE CODE ###
########################

# Ajouter votre code ici pour imprimer une facture et un borderaux
# de livraison.
