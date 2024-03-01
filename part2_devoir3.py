# Comments: Ce programme permet de jouer au pouilleux
# Jeu de cartes appelé "Pouilleux" 
# L'ordinateur est le donneur des cartes.
# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random
import re

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass

def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
    '''(list of str)-> tuple of (list of str,list of str)

    Retournes deux listes qui représentent les deux mains des cartes.  
    Le donneur donne une carte à l'autre joueur, une à lui-même,
    et ça continue jusqu'à la fin du paquet p.
    '''
    
    donneur=[]
    autre=[]


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    for i in p:
        if p.index(i) % 2 == 0 :
            autre.append(i)
        else:
            donneur.append(i)
    return (donneur, autre)

def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    resultat=[]


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    #sort les paire
    resultat = sorted(l)
    index_remove=[]
   #finding paire to remove by number  
    for i in range (len(resultat)-1):
        temp = re.split('([♠♣♢♡])', resultat[i])
        temp2 = re.split('([♠♣♢♡])', resultat[i+1])
        if temp[0] == temp2[0] and resultat.index(resultat[i]) not in index_remove:
                index_remove.extend((resultat.index(str(resultat[i])),resultat.index(resultat[i+1])))
      
    nbrListe = list(set(index_remove))   
    index=0
    while index < len(nbrListe):
        #retirer les element dans la liste en ordre croissant des index
         del resultat[nbrListe[index]-index]
         index+=1 
    random.shuffle(resultat)
    return resultat

def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''
    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    for i in p:
        print(i, end=' ')
    print("")

def entrez_position_valide(n):
    '''
    (int)->int
    Retourne un entier du clavier, de 1 à n (1 et n inclus).
    Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
    
    Précondition: n>=1
    '''

    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    card=0
    while n>=1 :
        card=int(input("SVP entrez un entier de 1 à {} : ".format(n)))
        if 1<=card<=n:
            return card

def joue():
    '''()->None
    Cette fonction joue le jeu'''

    p=prepare_paquet()
    melange_paquet(p)
    tmp=donne_cartes(p)
    donneur=tmp[0]
    humain=tmp[1]
    print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
    print("Votre main est:")
    affiche_cartes(humain)
    print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
    print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
    attend_le_joueur()
    donneur=elimine_paires(donneur)
    humain=elimine_paires(humain)

    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    #turn0 = joueur turn 1 = donneur
    turn=0
    #Determine who should start the game first
    #The one who has the fewest cards is the one who will have to start the game as indicated in the rules on wikipedia
    if len(donneur)<len(humain):
        turn=1

    #Loop while both of the player have card
    while len(donneur) !=0 or len(humain) !=0 :
        if turn==0:
            print("votre tour")
            print("Votre main est:")
            affiche_cartes(humain)
            print("J'ai {nb_carte} cartes. Si 1 est la position de ma première carte et {nb_carte} la position de ma dernière carte, laquelle de mes cartes voulez-vous?".format(nb_carte=len(donneur)))
            carte_prise=entrez_position_valide(len(donneur))
            carte=donneur[carte_prise-1]
            donneur.pop(carte_prise-1)
            if carte_prise==1:
                print("Vous avez demandé ma "+str(carte_prise)+"ère carte")
            else:
                print("Vous avez demandé ma "+str(carte_prise)+"ème carte")
           
            print("La voilà. C'est un "+str(carte))
            humain.append(carte)
            print("Avec "+str(carte)+" votre main est")
            affiche_cartes(humain)
            print("Après avoir défaussé toutes les paires et mélangé les cartes, votre main est:")
            humain=elimine_paires(humain)
            #check if someone win the game
            if len(donneur) ==0:
                print("J'ai terminé toutes les cartes.\nVous avez perdu! Moi, Robot, j'ai gagné.")
                break
            elif len(humain) ==0:
                print("Vous avez terminé toutes les cartes.\nFélicitations! Vous, Humain, vous avez gagné.")
                break
            affiche_cartes(humain)
            attend_le_joueur()
            #assign turn for robot
            turn=1
        else:
            '''
            Mon tour.
            J'ai pris votre 6ème carte.
            Appuyez Enter pour continuer. 
            '''
            carte_prise= random.randint(1,len(humain))
            print("***********************************************************")
            print("Mon tour")
            if carte_prise==1:
                print("J'ai pris votre {c}ère carte.".format(c=carte_prise))
            else:
                print("J'ai pris votre {c}ème carte.".format(c=carte_prise))
           
            carte=humain[carte_prise-1]
            humain.pop(carte_prise-1)
            donneur.append(carte)
            donneur=elimine_paires(donneur)
            attend_le_joueur()
            #check if someone win the game
            if len(humain) ==0:
                print("Vous avez terminé toutes les cartes.\nFélicitations! Vous, Humain, vous avez gagné.")
                break
            elif len(donneur) ==0:
                print("J'ai terminé toutes les cartes.\nVous avez perdu! Moi, Robot, j'ai gagné.")
                break
            #assign turn off player
            turn=0
            print("***********************************************************")
        
	 
# programme principale
joue()

