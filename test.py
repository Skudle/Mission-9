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

def test_articles(a_list) :
    for art in a_list :
        print(art)

"""
Test initial pour la classe Facture.
@author Kim Mens
@version 4 novembre 2020
"""
facture = Facture("PC Store - 22 novembre", articles)

def test_facture(f) :
    print(f)

"""
Faire exécuter les différents tests.
"""
a = ArticleReparation("Acer Nitro 5", 1099, 2)
a2 = ArticleReparation("Acer Nitro 5", 1099, 0)

def test_article_reparation():
    assert a.description() == "Réparation (2 heures)"
    assert a.prix() == 90
    assert a2.prix() == 20

'''def test_article_piece():
    assert'''

if __name__ == "__main__":

    print("\n*** TEST DE LA CLASSE Article ***\n")
    test_articles(articles)

    print("\n*** TEST DE LA CLASSE Facture ***\n")
    test_facture(facture)

test_article_reparation()