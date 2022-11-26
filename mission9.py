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

    def super_edit_description(self, txt):
        self.__description += txt

###############
### FACTURE ###
###############

"""
Cette classe représente une Facture, sous forme d'une liste d'articles.
   
@author Kim Mens
@version 4 novembre 2021
"""

class Facture:

    def __init__(self, d, a_list, facture_num):
        """
        @pre  d est un string court décrivant la facture;
              a_list est une liste d'objets de type Article.
        @post Une facture avec une description d et un liste d'articles a_list été crée.
        Exemple: Facture("PC Store - 22 novembre", [ Article("carte graphique", 119.49) ])
        """
        self.__description = d
        self.__articles = a_list
        self.facture_num = facture_num

    def description(self):
        """
        @post: retourne la description de cette facture.
        """
        return self.__description

    def articles(self):
        """
        :return: retourne la liste d'objets de type Article
        """
        return self.__articles

    def __str__(self):
        """
        @post: retourne la représentation string d'une facture, à imprimer avec la méthode print().
        (Consultez l'énoncé pour un exemple de la représentation string attendue.)
        """
        s = self.entete_str()
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.articles():
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA)

        return s

    def entete_str(self):
        """
        @post: retourne une représentation string de l'entête de la facture, comprenant le descriptif
               et les entêtes des colonnes.
        """
        return "Facture No " + str(self.facture_num) + " : " + self.__description + "\n" \
               + self.barre_str() \
               + "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description", "prix HTVA", "TVA", "prix TVAC") \
               + self.barre_str()

    def barre_str(self):
        """
        @post: retourne un string représentant une barre horizontale sur la largeur de la facture
        """
        barre_longeur = 83
        return "=" * barre_longeur + "\n"


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

    def totaux_str_pkpp(self, nombre, poids):
        """
        @pre:  nombre est le nombre total de tout les articles combiné
               poids est l'addition des poids de tout les articles
        @post: retourne un string représentant une ligne de facture avec les nombre totaux et poids,
               à imprimer en bas de la facture
        """
        return self.barre_str() \
               + "| {0:1} articles                               |              |{2:11.0f} |{3:8.3f}kg|\n".format((len(self.articles())), nombre, nombre, poids) \
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
        return "Livraison - Facture No " + str(self.facture_num) + " : " + self.__description + "\n" \
                + self.barre_str() \
                + "| {0:<40} | {1:>10}   | {2:>10} | {3:>9}|\n".format("Description", " poids/pce", "nombre",
                                                                          "poids") \
                + self.barre_str()

    def article_str(self, art):
        """
        @pre:  art une instance de la classe Article
        @post: retourne un string correspondant à une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.prix(), art.tva(),
                                                                         art.prix_tvac())

    def article_str_pkpp(self, art):
        """
        @pre:  art une instance de la classe Article
        @post: retourne un string correspondant à une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.3f}kg | {2:10.0f} |{3:8.3f}kg|\n".format(art.piece_obj.description(), art.piece_obj.poids(), art.nombre(),
                                                                         art.poids_total())
    def article_str_pkpp_test(self, art):
        """
        @pre:  art une instance de la classe Article
        @post: retourne un string correspondant à une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.3f}kg | {2:10.0f} |{3:8.3f}kg|\n".format(art.description_sans_nombre(), art.piece_obj.poids(), art.nombre(),
                                                                         art.poids_total())

    def print_livraison(self):
        """
        args: un objet de class facture
        creé une facture avec les données de l'objet
        retourne une facture à imprimer avec tous les articles, poids, prix, livraison fragile, ...
        """
        s = self.livraison_str()
        poids = 0
        total_nombre = 0
        article_fragile = 0
        for art in self.articles():
            if art.piece_obj.fragile() == True:
                article_fragile += 1
            s += self.article_str_pkpp(art)
            poids += art.poids_total()
            total_nombre += art.nombre()

        total_nombre = int(total_nombre)
        if article_fragile >= 1:
            s += self.totaux_str_pkpp(total_nombre, poids)
            s += " (!) *** livraison fragile ***"
            return s
        s += self.totaux_str_pkpp(total_nombre, poids)
        return s

    def print_livraison_avec_prix(self):
        """
        args: un objet de class facture
        creé une facture avec les données de l'objet
        retourne une facture à imprimer avec tous les articles, poids, prix, livraison fragile, ... mais cette fois avec les prix à coté
        des articles dans la facture

        """
        s = self.livraison_str()
        poids = 0
        total_nombre = 0
        article_fragile = 0
        for art in self.articles():
            if art.piece_obj.fragile() == True:
                article_fragile += 1
            s += self.article_str_pkpp_test(art)
            poids += art.poids_total()
            total_nombre += art.nombre()

        total_nombre = int(total_nombre)
        if article_fragile >= 1:
            s += self.totaux_str_pkpp(total_nombre, poids)
            s += " (!) *** livraison fragile ***"
            return s
        s += self.totaux_str_pkpp(total_nombre, poids)
        return s
#########################
### ARTICLEREPARATION ###
#########################
class ArticleReparation(Article):

    def __init__(self, d, p, duration: float):
        super().__init__(d, p)
        self.duration = duration
        if self.duration < 0:
            raise ValueError
        else:
            pass

    def description(self):
        """
        retourne la description de la reparation

        """
        return f"Réparation ({self.duration} heures)"

    def prix(self):
        """
        retourne le prix total de la reparation
        """
        return 20 + (35*self.duration)

#############
### PIECE ###
#############

class Piece:
    def __init__(self, string: str, montant: float, kg: float, fragilité=False, taux_tva_reduite=False):
        self.__string = string
        self.__montant = montant
        self.__kg = kg
        self.__fragilité = fragilité
        self.__taux_tva_reduite = taux_tva_reduite

        if self.__fragilité == True:
            self.__string += "(!)"

    def __str__(self):
        """
        retourne un string avec tous les attributs de la classe piece
        """
        return f"{self.description()} - {str(self.prix())} - {str(self.poids())} - {str(self.fragile())} - {str(self.tva_reduit())}"

    def description(self):
        """
        retourne la description textuelle de l'article piece
        """
        return self.__string

    def prix(self):
        return self.__montant

    def poids(self):
        return self.__kg

    def fragile(self):
        return self.__fragilité

    def tva_reduit(self):
        return self.__taux_tva_reduite

    def __eq__(self, other):
        return self.description() == other.description() and self.prix() == other.prix():


####################
### ARTICLEPIECE ###
####################

class ArticlePiece(Article):
    def __init__(self, d: str, p: float, piece_number: int, piece_obj):
        super().__init__(d, p)
        self.__number = piece_number
        self.piece_obj = piece_obj


    def super_description(self):
        """
        apelle la methode description de la class parent (article)
        """
        return super().description()

    def tva_ou_pas(self):
        """
        retourne vrai si l'objet piece beneficie d'une reduction de tva sinon false

        """
        return self.piece_obj.tva_reduit()

    def nombre(self):
        return self.__number

    def prix_piece(self):
        '''
        retourne le prix de l'article
        '''
        return super().prix()

    def description(self):
        """
        retourne la description de l'article
        """
        return f"{self.nombre()} * {super().description()} @ {float(super().prix())}"

    def description_sans_nombre(self):
        """
        retourne la description de l'article sans les nombre à cote de l'article
        """
        return f"{self.piece_obj.description()} @ {format(float(super().prix()), '.2f')}"

    def prix(self):
        """
        retourne le prix total de l'article HTVA

        """
        return self.nombre() * super().prix()

    def taux_tva(self):
        '''
        :return: 0.06 si l'article beneficie d'une reduc tva sinon 0.21
        '''
        if self.piece_obj.tva_reduit() == True:
            return 0.06
        else:
            return 0.21

    def poids_total(self):
        """
        retourne le poids total de l'article

        """
        return self.nombre() * self.piece_obj.poids()

    def __str__(self):
        return f"{self.super_description()} - {self.prix_piece()} - {self.piece_obj.description()}"


########################
### RUNNING THE CODE ###
########################

# Ajouter votre code ici pour imprimer une facture et un borderaux
# de livraison.
if __name__ == '__main__':
    carte_graphique_piece2 = Piece("Cparte Graphique RTX 3090", 1599.99, 2, True, False)
    carte_graphique_piece = Piece("Carte Graphique RTX 3090", 1599.99, 2, True, False)
    disque_dur_piece = Piece("disque dur 350 GB", 5, 0.355, True, True)
    adaptateur_DVI_VGA = Piece("adaptateur DVI - VGA ", 12.0, 0)
    adaptateur_DVI_VGA_article = ArticlePiece("adaptateur DVI - VGA ", 12.0, 5, adaptateur_DVI_VGA)
    Java_in_a_Nutshell = Piece("Java in a Nutshell", 24.00, 0.321)
    Java_in_a_Nutshell_article = ArticlePiece("Java in a Nutshell", 24.0, 2, Java_in_a_Nutshell)
    disque_dur_article_piece = ArticlePiece("disque dur 350 GB", 5, 1, disque_dur_piece)
    souris_bluetooth = Piece("souris bluetooth", 15.99, 0.176, False, False)
    souris_bluetooth_article_piece = ArticlePiece("souris bluetooth", 15.99, 3, souris_bluetooth)
    souris_bluetooth_article_piece2 = ArticlePiece("souris bluetooth", 15.99, 5, souris_bluetooth)
    pc_store = Facture("PC store 22 octobre",[disque_dur_article_piece, souris_bluetooth_article_piece, adaptateur_DVI_VGA_article, Java_in_a_Nutshell_article, souris_bluetooth_article_piece2], 1)
    print(pc_store.print_livraison())

