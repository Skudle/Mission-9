"""
Tests fournis pour la mission 9; à compléter par les étudiants.
@author Kim Mens
@version 4 novembre 2021
"""

from mission9 import Article, Facture, ArticleReparation, ArticlePiece, Piece

"""
Test initial pour la classe Article.
@author Kim Mens
@version 4 novembre 2021
"""
articles = [ Article("laptop 15\" 8GB RAM", 743.79),
             Article("installation windows", 66.11),
             Article("installation wifi", 45.22),
             Article("carte graphique", 119.49),
             ArticleReparation("Réparation", 35, 0.75),
             ArticlePiece("souris bluetooth", 15.99, 3, Piece("souris bluettoth", 15.99, 0.5, True, False)),
             ArticlePiece("Java in a Nutshell", 24, 2, Piece("Java in a Nutshell", 24, 0.1, False, True))
             ]
carte_graphique_piece = Piece("Carte Graphique RTX 3090", 1599.99, 2, True, False)
disque_dur_piece = Piece("disque dur 350 GB", 5,  0.355, True, True)
adaptateur_DVI_VGA = Piece("adaptateur DVI - VGA ", 12.0, 0)
adaptateur_DVI_VGA_article = ArticlePiece("adaptateur DVI - VGA ", 12.0, 5, adaptateur_DVI_VGA)
Java_in_a_Nutshell = Piece("Java in a Nutshell", 24.00, 0.321)
Java_in_a_Nutshell_article = ArticlePiece("Java in a Nutshell", 24.0, 2, Java_in_a_Nutshell)
disque_dur_article_piece = ArticlePiece("disque dur 350 GB", 5, 1, disque_dur_piece)
souris_bluetooth = Piece("souris bluetooth", 15.99, 0.176, False, False)
souris_bluetooth_article_piece = ArticlePiece("souris bluetooth", 15.99, 3, souris_bluetooth)
souris_bluetooth_article_piece2 = ArticlePiece("souris bluetooth", 15.99, 5, souris_bluetooth)
pc_store = Facture("PC store 22 octobre", [disque_dur_article_piece, souris_bluetooth_article_piece, adaptateur_DVI_VGA_article, Java_in_a_Nutshell_article, souris_bluetooth_article_piece2], 1)

def test_articles(a_list) :
    for art in a_list :
        print(art)

"""
Test initial pour la classe Facture.
@author Kim Mens
@version 4 novembre 2020
"""
facture = Facture("PC Store - 22 novembre", articles, 1)

def test_facture(f) :
    print(f)
def test_facture_pp(f):
    print(f.print_livraison_avec_prix())


"""
Faire exécuter les différents tests.
"""
a = ArticleReparation("Acer Nitro 5", 1099, 2)
a2 = ArticleReparation("Acer Nitro 5", 1099, 0)


def test_article_reparation():
    assert a.description() == "Réparation (2 heures)"
    assert a.prix() == 90
    assert a2.prix() == 20
    assert a.prix() == 90
    try:
        a3 = ArticleReparation("Acer Nitro 5", 1099, -1)
    except ValueError:
        print("Test passed") #La durée de répération ne peut etre inferieur à 0
    assert a2.prix() == 20


b = Piece("RPI 4", 65.99, 0.120, True, True)
b2 = Piece("RPI 4", 65.99, 0.120, False, False)

def test_piece():
    assert b.__str__() == "RPI 4(!) - 65.99 - 0.12 - True - True"
    assert b2.__str__() == "RPI 4 - 65.99 - 0.12 - False - False"

c = ArticlePiece("RPI 4", 65.99, 2, b2)
c2 = ArticlePiece("RPI 4", 65.99, 0, b)


def test_article_piece():
    assert c.__str__() == "RPI 4 - 65.99 - RPI 4"
    assert c.tva_ou_pas() == False
    assert c.taux_tva() == 0.21
    assert c2.taux_tva() == 0.06
    assert c.poids_total() == 0.240
    assert c2.poids_total() == 0

z = Facture("Test", [c, c, c, c], 3)

def test_facture_nombre():
    assert z.nombre(c) == 4

if __name__ == "__main__":

    print("\n*** TEST DE LA CLASSE Article ***\n")
    test_articles(articles)

    print("\n*** TEST DE LA CLASSE Facture ***\n")
    test_facture(facture)
    test_facture_pp(pc_store)

test_article_reparation()
test_piece()
test_article_piece()
test_facture_nombre()