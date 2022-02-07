######################################################################################
#fonction principale
#nom du fichier à lire

def question1(nom):
    print(f"je vais ouvrir le fichier {nom}")

    fichier =open(nom,'r',encoding="utf-8") #fais que les caractère spéciaux soit lu

    cpt=1 #compteur

    for ligne in fichier: #pour toute les lignes du fichiers

        ligne=ligne.rstrip("\n\r") #supprime les espace entre les lignes et supprime les caractères spéciaux

        print(f"ligne{cpt}:{ligne}")

        cpt=cpt+1


    fichier.close() #pas oublier de fermer le fichier quand on l'ouvre

    #####################################################################################
    # fonction principale
    # nom du fichier à lire
    #pour trouver les doublons
def question2(nom):
    print(f"je vais ouvrir le fichier {nom}")

    fichier = open(nom, 'r', encoding="utf-8")  # fais que les caractère spéciaux soit lu

    #j'enlève la première ligne
    fichier.readline()

    etudiants = {}  # crée une nouveau dico pour regrouper les valeurs
    for ligne in fichier:  # pour toute les lignes du fichiers


        ligne = ligne.rstrip("\n\r")  # supprime les espace entre les lignes et supprime les caractères spéciaux
        liste =ligne.split(";")

        for elt in liste: #affiche tous les éléments de la liste
           print(elt)



    fichier.close()  # pas oublier de fermer le fichier quand on l'ouvre


#####################################################################################
def question3(nom):
    print(f"je vais ouvrir le fichier {nom}")

    fichier = open(nom, 'r', encoding="utf-8")  # fais que les caractère spéciaux soit lu

    #j'enlève la première ligne
    fichier.readline()

    etudiants = {}  # crée une nouveau dico pour regrouper les valeurs
    for ligne in fichier:  # pour toute les lignes du fichiers


        ligne = ligne.rstrip("\n\r")  # supprime les espace entre les lignes et supprime les caractères spéciaux
        liste =ligne.split(";")

        dictco={}# crée un dictionnaire pour chaque ligne du fichier

        dictco["num etudiant"] = liste[1],
        dictco["nom"] = liste[2],
        dictco["prenom"] = liste[3],
        dictco["classe"] = liste[4],
        dictco["note"] = liste[5],

        if liste [1] not in etudiant: #
            etudiants[liste[1]] = dictco

        #print(dictco["num étudiant"],dictco["nom"],dictco["prenom"],dictco["classe"],dictco["note"])#affiche les lignes du dictco


    fichier.close()  # pas oublier de fermer le fichier quand on l'ouvre


#####################################################################################
if __name__ =='__main__':
    #question1("C:\\Temp\\un fichier de notes.txt") chemin absolu du fichier note
    #question2("C:\\Temp\\un fichier de notes.txt")  # chemin absolu du fichier note
    question3("C:\\Temp\\un fichier de notes.txt")  # chemin absolu du fichier note
    etudiant=question3("C:\\Temp\\un fichier de notes.txt")
    print(etudiant)