"""tuples"""
#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
       passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici
    a = 1
    l = []
    ld = []

    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            print(i)
            a += 1
        else:
            l.append(a) # nombre de lettre en commun
            ld.append(s[i-1]) # carractère
            a = 1

    # Ajouter le dernier groupe
    l.append(a)
    ld.append(s[-1])

    return list(zip(ld, l))

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
       passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici
    # cas de base
    if s == "":
        return []
    # recherche nombre de caractères identiques au premier
    a = 1
    while a < len(s) and s[a] == s[0]:
        a += 1

    # appel récursif
    return [(s[0], a)] + artcode_r(s[a:])

#### Fonction principale

def main():
    """main"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
