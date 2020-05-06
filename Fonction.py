#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import time
from pygame.locals import*
from Constante import*

#from fonction_test import*


from k1 import*


#lancer le Main.py

############################################################################################################################
                                                    #information
############################################################################################################################

#projet: Kakuro (en cours de dev) 24/04/2017
#groupe: L2C1 PARIS DESCARTES

#fait par: david dilay
#          li laurent
#          saverinadin jeanne
#          chansuk chatri

#mail: ih05933@etu.parisdescartes.fr

#fait pour (encadrant): severine affeldt

#remerciement: a notre encadrente qui nous a encadré pendant tout le long du projet

#nous avons l'autorisation d'utiliser les logos de descartes

#toutes les autres images ont ete faits pas nous


#la musique utilisé est libre de droit:
# http://www.musicscreen.be/musique-libre-de-droit/Catalogue/Tigra.html
# ------> pour activer la musique retirer les commentaires '#' devant chaque 'musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)' du fichier Main.py (le son grisaille legerement)


#la police a caractere special 'PWPerspective.ttf' utilisé est libre de droit:
# http://www.dafont.com/fr/pwperspective.font
#-->remerciment www.peax-webdesign.com pour la police


#la police a caractere special 'Black Carrot.ttf' utilisé est libre de droit:
# http://www.dafont.com/fr/black-carrot.font


#la police a caractere special MEEGOREN.ttf utilisé est libre de droit:
# http://www.dafont.com/fr/meegoreng.font


#source du fichier k1.py qui nous a aidé:
# http://pydoc.net/Python/kakuro/1.0.0/kakuro/



#fait sous WINDOWS avec
#python 2.7.13 windows 32bits  : https://www.python.org/downloads/release/python-2713/ 
#pygame 1.9.1 windows 32bits   : http://www.pygame.org/download.shtml
# /!\ ne pas prendre de version 64bits /!\



#compatible avec linux et mac OS, suffit d'installer python 2.7 et pygame 1.9
# /!\ ne pas prendre de version 64bits /!\


#/!\mettre a jour la grille du niveau dans le code/!\





############################################################################################################################
                                                    #fonction
############################################################################################################################


def saisir_nombre(x,y,tempp):   
        """Permet d'afficher le nombre saisie par le joueur dans une grille en partie classique
        le programme accepte toutes les saisies, mais ne complete la grille que si c'est un chiffre de type caractere entre 1 et9
        ---------------------------------------------------------------------------------------------------------------
        ENTRE:
                x:(int) position en abscisse en px du chiffre a affiché
                y:(int) position en ordonne en px du chiffre a affiché
                tempp:(int) est le temps de jeu totale depuis le debut de la partie en seconde*60
        ---------------------------------------------------------------------------------------------------------------
        SORTIE:
        de type: "chiffre", "tempaddi"

                "chiffre":(int) correspond au chiffre que le joueur a entrée, au meme chiffre qui a etait affiché, pour que le prgrm prenne en compte l'avancé de la grille (graphiquement et internement)
                "tempaddi":(int) (temps additionnel)est le temps de jeu totale depuis le debut de la partie en seconde*60 AVEC le temps que le joueurs a utilisé
                          pour faire la saisie au clavier (que la saisie soit erronée ou bonne)
        ---------------------------------------------------------------------------------------------------------------
        REMARQUE:
        la demande d'entrée se fait dans la fonction "ask", mais c'est bien la fonction saisir_nombre qui traite la donnée

        la demande d'entrée est une chaine de caractere (limité a 1 caractere, d'ou le 2eme argument dans "ask"), si l'unique caractere n'est pas un chiffre compris entre le caractere 1 et 9
        alors le prgrm ne plante pas et retourne 0,tempaddi
        """
       
        n,tempaddi=ask("ton chiffre",1,tempp)
        #n=asktst("ton chiffre",tempp)
        #n=raw_input("mets ton chiffre: ")                    #le joueur entre des valeurs qui sont convertis en chaine
        if (n>='1') and (n<='9') and len(n)==1:              #compare caractere par caractere selon ordre ascii, et verifie si la longeur de l entre est 1
                if n=='1':  
                        fenetre.blit(nbr_1,(x,y))
                        return 1,tempaddi
                elif n=='2':
                        fenetre.blit(nbr_2,(x,y))
                        return 2,tempaddi
                elif n=='3':
                        fenetre.blit(nbr_3,(x,y))
                        return 3,tempaddi
                elif n=='4':
                        fenetre.blit(nbr_4,(x,y))
                        return 4,tempaddi
                elif n=='5':
                        fenetre.blit(nbr_5,(x,y))
                        return 5,tempaddi
                elif n=='6':
                        fenetre.blit(nbr_6,(x,y))
                        return 6,tempaddi
                elif n=='7':
                        fenetre.blit(nbr_7,(x,y))
                        return 7,tempaddi
                elif n=='8':
                        fenetre.blit(nbr_8,(x,y))
                        return 8,tempaddi
                elif n=='9':
                        fenetre.blit(nbr_9,(x,y))
                        return 9,tempaddi
                else:
                        return 0,tempaddi #entrée incorrecte, on renvoit 0 par defaut
               
                       
        else:                           #le else n'arrive jamais

                return 0,tempaddi   
                                 
def effacealrt():
    """
    creer un rectangle de couleur fond d'ecran pour effacer le texte
    qui informe au joueur qu'il n'a aucune grille dans creation
    """
    rect = pygame.Rect([250, 440, 200, 30]) #x y longueur largeur
    pygame.draw.rect(fenetre,(185,122,87),rect,0)
    
               


def efface_save():
        """
        creer un rectangle de couleur fond d'ecran et de meme dimension que le bouton sauvegarde
        pour pouvoir effacer la zone de texte dynamique (du bouton sauvegarde)
        permet de refaire un collage de texte par dessus(autre fonction)
        et ainsi ne pas avoir d effet de superposition(gras) qui rend moche
        """
        rect = pygame.Rect([35, 357, 225, 30]) #x y longueur largeur
        pygame.draw.rect(fenetre,(185,122,87),rect,0)
        #pygame.draw.rect(fenetre,(255,255,255),rect,0)

def efface_verif():
        """
        creer un rectangle de couleur fond d'ecran et de meme dimension que le bouton verification
        pour pouvoir effacer la zone de texte dynamique(du bouton verification)
        permet de refaire un collage de texte par dessus(autre fonction)
        et ainsi ne pas avoir d effet de superposition(gras) qui rend moche
        """
        rect = pygame.Rect([35, 407, 215, 30]) #x y longueur largeur
        pygame.draw.rect(fenetre,(185,122,87),rect,0)
        

def efface_stats():
        """
        creer un rectangle de couleur fond d'ecran et de meme dimension que la zone de stats en jeu (nombre aide utilise, coups utilisé)
        pour pouvoir effacer la zone de texte dynamique(de la zone de stats)
        permet de refaire un collage de texte par dessus(autre fonction)
        et ainsi ne pas avoir d effet de superposition(gras) qui rend moche
        """
        
        rect = pygame.Rect([76, 240, 200, 90])
        pygame.draw.rect(fenetre,(185,122,87),rect,0)



def efface():
        """
        creer un rectangle de couleur fond d'ecran et de meme dimension que le rectangle utilisé permettant
        de faire les saisie en partie classque, partie edité, et le choix du niveau(edité) a lancé
        la fonction est appelé a chaque fois que le joueur valide la saisie clavier
        """
        rect = pygame.Rect([0, 0, 358, 30])
        rect.top=grilley+50*7+7+taille_sprite/2
        rect.left=grillex
        pygame.draw.rect(fenetre,(185,122,87),rect,0)
        pygame.display.flip()


def efface_temps():
        """
        creer un rectangle de couleur fond d'ecran et de meme dimension que la zone du texte permettant d'ecrire le chronometre
        pour pouvoir effacer la zone de texte dynamique(affichage du chronometre)
        permet de refaire un collage de texte par dessus(autre fonction)
        et ainsi ne pas avoir d effet de superposition(gras) qui rend moche
        """
        
        rect = pygame.Rect([76, 300, 200, 15])
        pygame.draw.rect(fenetre,(185,122,87),rect,0)
        
                
                
                
def display_box(message):
    """cree un rectangle qui mis a jour a chaque caractere nouveau dans la saisie
    permet aussi de ne pas avoir de surperposition de texte
    ce rectangle est utilisé pour le choix du niveau a jouer en edition, en partie classique, en partie edité
    """
    rect = pygame.Rect([0, 0, 358, 30])#rect = pygame.Rect([0, 0, 358, 22])
    rect.top=grilley+50*7+7+taille_sprite/2
    rect.left=grillex
    pygame.draw.rect(fenetre,(226, 226, 226), rect, 0) #fond
    pygame.draw.rect(fenetre, (0,0,0), rect, 1) #contour car largeur +grand
    fenetre.blit(fontedite.render(message, 1, (0,0,0)), (rect.left+8,rect.top+10))    
    pygame.display.flip()


def display_box_log(message):
    """cree un rectangle qui mis a jour a chaque caractere nouveau dans la saisie
    permet aussi de ne pas avoir de surperposition de texte
    ce rectangle est situté au milieu de l'ecran, au 1er menu, lorsque le joueur doit entrer son compte
    """
    rect = pygame.Rect([0, 0, 358, 30])#rect = pygame.Rect([0, 0, 358, 22])
    rect.centerx=ecran.get_rect().centerx
    rect.centery=ecran.get_rect().centery
    txt_posx=rect.centerx-170
    txt_posy=rect.centery-5
    pygame.draw.rect(fenetre,(226, 226, 226), rect, 0) #fond
    pygame.draw.rect(fenetre, (0,0,0), rect, 1) #contour car largeur +grand
    fenetre.blit(fontedite.render(message, 1, (0,0,0)), (txt_posx,txt_posy)) #color text         
    pygame.display.flip()







def ask(question,maxi,tempp):#on limite a maxi le nbr de caractere dans ask, s'il n'y pas de limite l'ecriture peut depasser le rectangle ou meme de l'ecran
    """
    permer au joueur de saisie une chaine de caractere qui serra traité par d'autre fonction
    ----------------------------------------------------------------------------------------------------------------
    ENTRE:
        question:(string) ce qui serra afficher a l'ecran dans la fonction secondaire(display_box(_log))
        maxi:(int) nombre de caractere maximum pris en compte (le surplus ne serra pas afficher pas la fonction secondaire)
        tempp:(int)le temp ecoulé en jeu classique depuis le debut d'une partie en seconde*60
    ----------------------------------------------------------------------------------------------------------------
    SORTIE:
        text:(string) qui est ce qu'a entrée le joueur
        tempp:(int) le nouveau temps qui est ecoulé depuis le debut de partie avec la durée de cette saisie en seconde*60
    ----------------------------------------------------------------------------------------------------------------
    REMARQUE:
    la fonction est utilisé dans bcq de cas differents, la variable maxi et tempp permet de differencier ces cas
    en effet si le temps est -1 on ne cree pas de chronometre interne
             si maxi est 10 alors on fait l'affichage pour la gestion des log (1r menu)
             sinon c'est un affichage classique en jeu (l'affichage du choix niveau edition est le meme avec une limitation de 3caracters soit 999niveau maximum)

    quand le tempp n'est pas -1 alors on creer un deuxieme chronometre pendant la saisie, qui commence a la valeur de tempp,
    ce qui permet de faire tourner le chronometre meme pendant la saisie. On fait sortir la nouvelle valeur de tempp qui serra appelé tempaddi (temp additionnel)
    dans la suite du prgrm
    """

    pygame.font.init()  
    text = ""


    if tempp==-1:
        chrono=False
    else:
        chrono=True
                    

    if maxi==10: #si le msg est limite a 10caractere, c'est forcement celui du log, car tout les autres entrees sont limite a 2
            display_box_log(question + ": " + text)
    else:
            display_box(question + ": " + text)

    while True:
           
        event = pygame.event.poll()
        if chrono==True:
                        
                        tempp+=1
                        total_seconds = tempp // 60
                        minutes = total_seconds // 60
                        seconds = total_seconds % 60
                        afficher = "temps: {0:02}:{1:02}".format(minutes, seconds)
                        text2 = font.render(afficher, True, (0,0,0))
                        efface_temps()
                        fenetre.blit(text2,(76,300))
                        clock.tick(60)  #limitation de vitesse a 60t/s
                        pygame.display.flip()
        
        if event.type == QUIT:  
            pygame.quit()

        if event.type==KEYDOWN:#sinon quand ont appuye sur echap sur zone saisie ça met des carres 
            if event.key == K_ESCAPE:
                    continue
        
            
        if event.type != KEYDOWN:
          continue

          
          
        if event.key == K_BACKSPACE:
            text = text[0:-1]
            
        elif event.key == K_RETURN:#enter
                if maxi==30:
                        display_box_log(question + ": " + "")#pour effacer sur le rectangle ce qui a etait saisie apres validation
                        
                else:
                        display_box(question + ": " + "")#pour effacer sur le rectangle ce qui a etait saisie apres validation
                        
                
                break
        
        elif len(text)<maxi:
                text += event.unicode.encode("UTF-8")#ascii
            
        
        
        if maxi==10:
                display_box_log(question + ": " + text)
                
        else:
                
                display_box(question + ": " + text)
                
                

    if chrono==True:
        return text,tempp
    return text




def saisir_nombredite(intro):
                """Permet d'afficher le nombre saisie par le joueur dans une grille en partie partie edité
                le programme accepte toutes les saisies, mais ne complete la grille que si c'est un chiffre de type caractere entre 1 et39
                ---------------------------------------------------------------------------------------------------------------
                ENTRE:
                        intro:(string) la phrase d'introduction qui serra affiché juste avant la zone de saisie par une autre fonction
                ---------------------------------------------------------------------------------------------------------------
                SORTIE:
                si la saisie est incorrecte alors elle s'appelle elle meme tant que l'entrée du joueur n'est pas correcte (recurcive)
                si la saisie est correcte alors elle renvoit deux cas (en fonction de la longueur de la chaine entrée limité a 2)
                    "z"+chif:(string) avec chif un caractere rangé dans le tableau de caractere "chiffre" defini dans Constante.py
                    dizaine+unite:(string) avec dizaine un caractere rangé dans le tableau "chiffred" defini dans Constante.py
                                           avec unite un caractere rangé dans le tableau de caractere "chiffre" defini dans Constante.py      
                ---------------------------------------------------------------------------------------------------------------
                REMARQUE:

                on ne force pas le joueur a ecrire un chiffre en 2caractere, le joueur ne veut pas ecrire "08" pour mettre "8"
                alors le programme regarde la longueur de la chaine et ajoute le carac "z", qui signifie un zero qu'on n'affiche pas, en effet en jeu on n'affiche pas 08 mais 8
                
                le caractere "z" est necessaire pour les sauvegardes aussi, pour que le programme qu'il y a un caractere qui ne doit pas etre lu a cet emplacement,
                (et qui prend le decalage quand meme lors de la lecture)
                il faut que lorsque le joueur edite une grille, le programme ecrit les informations dans un fichier txt de la meme facon que nous(developpeur) ayant ecrit les grilles a la main (dans un fichier txt)
                ainsi les fonctions d'affichage et de sauvegarde serront compatible, car nous utilisons la meme methode pour "coder" et "decoder" nos information sur fichier txt
                """

                                        
                #n=raw_input("mets ton nbr a 2 chiffre du bas: ")
                n=ask(intro,2,-1)
                
                if len(n)==1: #si le joueur mets qu'un chiffre alors c est forcement celui des unite
                        for chif in chiffre:
                                if n==chif and n!='0': #pour pas ecrire 0...
                                        return ("z"+chif)

                                      
                elif len(n)==2:
                        for chif in chiffred:
                                if n[0]==chif:
                                        dizaine=n[0]
                                        for chif in chiffre:
                                                if n[1]==chif:
                                                        unite=n[1]
                                                        return (dizaine+unite)
                                        
                
                if intro[0]=='r': #si la 1er lettre est un 'r' alors le 1er mot est forcement "remets", donc pas besoin d'afficher "remets ton remets ton remets ton... intro"
                        return saisir_nombredite(intro)
                return (saisir_nombredite("remets ton "+intro)) #si l'entre du joueur remplis pas condition alors on lui redemande
                                                                                                

                     
def char_nbr(listechar): #transforme 2 caractere en 1 nombre
        """
        transforme 2 caractere (chiffre) en 1 nombre
        ---------------------------------------------------------------------------------------------------------------
        ENTRE:
            listechar:(tableau caractere) de taille 2
        ---------------------------------------------------------------------------------------------------------------
        SORTIE:
            entier:(int) le nombre entier
        ---------------------------------------------------------------------------------------------------------------
        REMARQUE:

        tout les nombres sommes sont "codé" avec 2caractere meme si le nombre en lui meme est un chiffre (presence du caractere "z")
        """
        listeint=[]
        k=0
        while k<2:
                if listechar[k]=='z':
                        listeint.append(0)
                else:
                        listeint.append(int(listechar[k]))
                k+=1
    
        entier=listeint[0]*10+listeint[1]
        return entier



def sommehori(modifiable,debut):
        """
        faits la somme d'une rangée horizontale
        ---------------------------------------------------------------------------------------------------------------
        ENTREE:
            modifiable:(tableau de int et char) contient la ligne dont on va calculer la rangée horizontale
            debut:(int) nous donne l'information du debut où l'on va commencer a additionner les nombres pour avoir les sommes
        ---------------------------------------------------------------------------------------------------------------
        SORTIE:
            k:(int) le compteur qui accumule les sommes des rangée horizontale, initialisé a 0
            -1: le parametre debut est la position du nombre somme, or on commence a sommé juste apres le nombre somme, il faut verifier qu'on
                ne sorte pas de la grille. (si une grille possede case somme a la derniere ligne/colonne, la grille devient impossible)
                on renvoit un nombre negatif, car il n'y a pas de case somme negatif (comparaison du compteur obtenu avec la case somme)
        ---------------------------------------------------------------------------------------------------------------
        REMARQUE:

        modifiable est de taille 7 (0a6), les elements contenus sont soit des chiffres int(0a9) soit le caractere "x" signifiant non-modifiable (case somme, obstacle)
        ex: sommehori(['x', 'x', 4, 2, 'x', 8, 'x'],1)
        va retourner k=6
        le prgrm commence a sommer a l'indice 1, et s'arrete a la premiere case qui n'est pas modifiable

        ex: sommehori(['x', 4, 0, 'x', 0, 3, 8],3)
        va retourner k=11
        le prgrm commence a sommer a l'indice 3, et s'arrete a la derniere colonne (la 7eme)

        il peut y avoir plusieurs rangé dans une meme ligne
        """

     
        
        debut+=1
        if debut==7: #permet de ne pas faire planter le prgm si il y a niv impossible (si on mets case somme a extremiter grille et qu il possede aucune place pour 'saisir' un nombre (car hors grille)
                return -1
        k=0

        while debut!=7  and modifiable[debut]!='x':#BUG(corrige) il faut forcer l arret du comptage meme si il n' a pas de 'x', le prgm ne peut pas regarder si le terme d'apres est un 'x' lorsqu'il est a la derniere COLONNE de la grille
                if modifiable[debut]==0:           #ordre condition(while) important car dans l'autre sens SI debut==7 alors le prgram va chercher modifiable[7] qui n'existe pas et va BUG // python lis donc la 1er instruction et si elle est fausse il ne lis pas le reste
                        return -1 #on ne retourne surtout pas de 0 ou de k, cette condition prouve qu'il manque un nbr dans un ligne
                k=modifiable[debut]+k
                debut+=1
               
        #if debut==6:
                #return k+ modifiable[debut] #on doit ajouter manuellement la derniere valeur si elle se situe a la derniere colonne
        
        return k



def sommeverti(modifiable,debut,col):   
        """
        faits la somme d'une rangée verticale
        ---------------------------------------------------------------------------------------------------------------
        ENTREE:
            modifiable:(tableau de int et char) qui est self.grillemodifiable, qui contient 7 sous tableau de taille 7
            debut:(int) nous donne l'information du debut où l'on va commencer a additionner les nombres pour avoir les sommes
            col:(int) position de la colonne que le prgrm va sommer
        ---------------------------------------------------------------------------------------------------------------
        SORTIE:
            k:(int) le compteur qui accumule les sommes des rangées verticale, initialisé a 0
            -1: le parametre debut est la position du nombre somme, or on commence a sommé juste apres le nombre somme, il faut verifier qu'on
                ne sorte pas de la grille. (si une grille possede case somme a la derniere ligne/colonne, la grille devient impossible)
                on renvoit un nombre negatif, car il n'y a pas de case somme negatif (comparaison du compteur obtenu avec la case somme)
        ---------------------------------------------------------------------------------------------------------------
        REMARQUE:

        modifiable est de taille 7 (0a6), les elements contenus sont soit des chiffres int(0a9) soit le caractere "x" signifiant non-modifiable (case somme, obstacle)
        ex: sommehori(['x', 'x', 4, 2, 'x', 8, 'x'],1)
        va retourner k=6
        le prgrm commence a sommer a l'indice 1, et s'arrete a la premiere case qui n'est pas modifiable

        grilleexemple=['x', 'x', 'x', 'x',  'x', 'x', 'x'], 
                      ['x', 'x',  0,  'x',  'x', 'x', 'x'],
                      ['x',  0,   1,   2,    0,   0,  'x'], 
                      ['x',  0,   4,   0,    0,   0,  'x'],
                      ['x',  0,   1,   6,    0,   0,  'x'], 
                      ['x', 'x', 'x', 'x',   0, 'x', 'x'],
                      ['x', 'x', 'x',  9, 'x', 'x', 'x']]
                      
        ex: sommeverti(grillexemple,1,3)
        va retourner k=2+0+6=8
        le programme commence a compter a la 1er ligne et 3eme colonne, il s'arrete de compter a la sortie de la gille (7) ou lorsque le prochain caractere (du bas, donc il faut donc changer de sous tableau) est "x" 

        il peut y avoir plusieurs rangé dans une meme ligne
        """
              

        debut+=1
        if debut==7: #permet de ne pas faire planter le prgm si il y a niv impossible (si on mets case somme a extremiter grille et qu il possede aucune place pour 'saisir' un nombre (car hors grille)
                return -1
        k=0
        while debut!=7 and modifiable[debut][col]!='x':#BUG(corrige) il faut forcer l arret du comptage meme si il n' a pas de 'x', le prgm ne peut pas regarder si le terme d'apres est un 'x' lorsqu'il est a la derniere LIGNE de la grille
                if modifiable[debut][col]==0:          #ordre condition(while) important car dans l'autre sens SI debut==7 alors le prgram va chercher modifiable[7][col] qui n'existe pas et va BUG // python lis donc la 1er instruction et si elle est fausse il ne lis pas le reste
                        return -1 #on ne retourne surtout pas de 0 ou de k, cette condition prouve qu'il manque un nbr dans un ligne
                k=modifiable[debut][col]+k
                debut+=1

        #if debut==6:
              #  return k+modifiable[debut] #on doit ajouter manuellement la derniere valeur si elle se situe a la derniere ligne
        
        return k


def anti_doublon_horizontale(n,liste,y):
        """
        si au moment de la saisie, l ancien nombre (qui est ecrasé par la nouvelle saisie) etait present exactement 2 fois dans la meme rangé horizontale,
        (nombre barré en rouge), il n'y est donc qu'une plus seule fois
        alors on affiche  par dessus la valeur de ce meme nombre sur toute la ligne(sur les nombres de la meme valeur) si elle n'est plus presente qu'une seule fois
        
        cela aura pour effet d'effacer le rouge qui ne doit etre present qu'en cas d'erreur (le joueur sort de l'erreur)
        ---------------------------------------------------------------------------------------------------------------
        ENTRE:
            n:(int) est le chiffre qui c'est fait ecrasé par la nouvelle saisi du joueur en partie classique
            liste: (int et char) est un tableau (celui de self.grillemodifiable, a une ligne precise) qui correspond a la ligne où il y a eu la nouvelle saisie
            y:(int) l'ordonne en pixel ou doit se faire l'affichage
        ---------------------------------------------------------------------------------------------------------------     
        """
        k=0 #occ du nbr, reset entre 2 case non modifiable 'x'
        i=-1#rang liste
        pn=-1 #position du nombre dans la ligne, elle serra range dans un tableau SEULEMENT SI elle est repete qu'une fois entre 2 'x'(ou debut fin de grille)
        tabln=[]
      
        while i<6:
                i+=1
                
                if liste[i]==n:
                        k+=1
                        pn=i#on la save au cas ou
                        
                if liste[i]=='x' or i==6:
                        if k==1:
                                tabln.append(pn)
                        k=0
                
                
        if n==1:
                for i in range(0,len(tabln)): #parmis les positions(x) save dans ce tableau, il y a forcement celui du nbr qui est barre en rouge s il ne doit plus l'etre, alors on repose par dessus les images de tout ces nbr de la ligne.
                        fenetre.blit(nbr_1,(tabln[i]*(taille_sprite)+grillex+tabln[i]+1 , y+1))
        elif n==2:
                for i in range(0,len(tabln)):
                        fenetre.blit(nbr_2,(tabln[i]*(taille_sprite)+grillex+tabln[i]+1 , y+1))
        elif n==3:
                for i in range(0,len(tabln)):
                        fenetre.blit(nbr_3,(tabln[i]*(taille_sprite)+grillex+tabln[i]+1 , y+1))
        elif n==4:
                for i in range(0,len(tabln)):
                        fenetre.blit(nbr_4,(tabln[i]*(taille_sprite)+grillex+tabln[i]+1 , y+1))
        elif n==5:
                for i in range(0,len(tabln)):
                        fenetre.blit(nbr_5,(tabln[i]*(taille_sprite)+grillex+tabln[i]+1 , y+1))
        elif n==6:
                for i in range(0,len(tabln)):
                        fenetre.blit(nbr_6,(tabln[i]*(taille_sprite)+grillex+tabln[i]+1 , y+1))
        elif n==7:
                for i in range(0,len(tabln)):
                        fenetre.blit(nbr_7,(tabln[i]*(taille_sprite)+grillex+tabln[i]+1 , y+1))
        elif n==8:
                for i in range(0,len(tabln)):
                        fenetre.blit(nbr_8,(tabln[i]*(taille_sprite)+grillex+tabln[i]+1 , y+1))
        elif n==9:
                for i in range(0,len(tabln)):
                        fenetre.blit(nbr_9,(tabln[i]*(taille_sprite)+grillex+tabln[i]+1 , y+1))



def anti_doublon_verticale(n,liste,rangx,x):
        """
        si au moment de la saisie, l ancien nombre (qui est ecrasé par la nouvelle saisie) etait present exactement 2 fois dans la meme rangé verticale,
        (nombre barré en rouge), il n'y est donc qu'une plus seule fois
        alors on affiche  par dessus la valeur de ce meme nombre sur toute la colonne(sur les nombres de la meme valeur) si elle n'est plus presente qu'une seule fois
        
        cela aura pour effet d'effacer le rouge qui ne doit etre present qu'en cas d'erreur (le joueur sort de l'erreur)
        ---------------------------------------------------------------------------------------------------------------
        ENTRE:
            n:(int) est le chiffre qui c'est fait ecrasé par la nouvelle saisi du joueur en partie classique
            liste: (int et char) est un tableau (celui de self.grillemodifiable) a deux dimensions qui represente la grille kakuro
            rangx:(int) la position de la ligne, pour pouvoir parcourir le tableau de ligne en ligne (et non pas de colonne en colonne comme "d'habitude")
            x:(int) l'abscisse en pixel ou doit se faire l'affichage
        ---------------------------------------------------------------------------------------------------------------     
        """
        k=0
        i=-1
        pn=-1
        tabln=[]

        while i<6:
                i+=1

                if liste[i][rangx]==n:
                        k+=1
                        pn=i

                if liste[i][rangx]=='x' or i==6:
                         if k==1:
                                 tabln.append(pn)
                         k=0
       

        if n==1:
                for i in range(0,len(tabln)):
                        fenetre.blit(nbr_1,(x+1 , tabln[i]*(taille_sprite)+grilley+tabln[i]+1))
        elif n==2:
                for i in range(0,len(tabln)):
                        fenetre.blit(nbr_2,(x+1 , tabln[i]*(taille_sprite)+grilley+tabln[i]+1))
        elif n==3:
                for i in range(0,len(tabln)):
                        fenetre.blit(nbr_3,(x+1 , tabln[i]*(taille_sprite)+grilley+tabln[i]+1))
        elif n==4:
                for i in range(0,len(tabln)):
                        fenetre.blit(nbr_4,(x+1 , tabln[i]*(taille_sprite)+grilley+tabln[i]+1))
        elif n==5:
                for i in range(0,len(tabln)):
                        fenetre.blit(nbr_5,(x+1 , tabln[i]*(taille_sprite)+grilley+tabln[i]+1))
        elif n==6:
                for i in range(0,len(tabln)):
                        fenetre.blit(nbr_6,(x+1 , tabln[i]*(taille_sprite)+grilley+tabln[i]+1))
        elif n==7:
                for i in range(0,len(tabln)):
                        fenetre.blit(nbr_7,(x+1 , tabln[i]*(taille_sprite)+grilley+tabln[i]+1))
        elif n==8:
                for i in range(0,len(tabln)):
                        fenetre.blit(nbr_8,(x+1 , tabln[i]*(taille_sprite)+grilley+tabln[i]+1))
        elif n==9:
                for i in range(0,len(tabln)):
                        fenetre.blit(nbr_9,(x+1 , tabln[i]*(taille_sprite)+grilley+tabln[i]+1))



#ancienement utilisé
                        
def fsimple(joueur):
    """
    permet au joueur de soit quitter le jeu, soit revenir au menu precedent
    ---------------------------------------------------------------------------------------------------------------
    ENTREE:
        joueur:(string) le nom de compte du joueur (ou son nom), utilisé dans la fonction logout
                        et dans les chemin d'acces de fichier
    ---------------------------------------------------------------------------------------------------------------
    SORTIE:
        boolean de type int
        si 1 alors retour au menu precedent
        sinon quitter le jeu
    ---------------------------------------------------------------------------------------------------------------
    REMARQUE:

    la touche echap permet toujours de revenir au menu precredent
    """
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key == K_ESCAPE:
                return 1
        
        elif event.type==QUIT:
            logout(joueur)  
            jeu=False
            pygame.quit()
            return 0
        





def effaceb(pos):
    """
    pose un carre couleur fond d'ecran sur un texte
    ---------------------------------------------------------------------------------------------------------------
    ENTREE:
        pos:(int) la position en ordonnee de la pose du rectangle que l'on va poser        
    ---------------------------------------------------------------------------------------------------------------
    """
    rect = pygame.Rect([190, -27+pos, 338, 50]) #x y longueur largeur
    #pygame.draw.rect(fenetre,(0,0,0),rect,0)
    pygame.draw.rect(fenetre,(185,122,87),rect,0)
 
        
def colorb(pos,nom,color):
    """
    permet d'ecrire un texte
    ---------------------------------------------------------------------------------------------------------------
    ENTREE:
        pos:(int) la position en ordonnee de la pose du bouton/texte
        nom:(string) le nom du bouton/texte a afficher
        color: (int,int,int) triplet de trois nombre entre 0 et 255 qui forme une couleur
    ---------------------------------------------------------------------------------------------------------------
    """
   # txt=fontregle2.render(nom,1,color)
    txt=fontmenu.render(nom,1,color)
    txt_pos=txt.get_rect()
    txt_pos.centerx = ecran.get_rect().centerx 
    txt_pos.centery = pos
    fenetre.blit(txt,txt_pos)
    
def effaceb2(pos):
    """
    pose un carre couleur fond d'ecran sur un texte
    ---------------------------------------------------------------------------------------------------------------
    ENTREE:
        pos:(int) la position en ordonnee de la pose du rectangle que l'on va poser        
    ---------------------------------------------------------------------------------------------------------------
    """
    rect = pygame.Rect([190, pos-20, 338, 50]) #x y longueur largeur
    pygame.draw.rect(fenetre,(185,122,87),rect,0)

def colorb2(pos,nom,color):
    """
    permet d'ecrire un texte
    ---------------------------------------------------------------------------------------------------------------
    ENTREE:
        pos:(int) la position en ordonnee de la pose du bouton/texte
        nom:(string) le nom du bouton/texte a afficher
        color: (int,int,int) triplet de trois nombre entre 0 et 255 qui forme une couleur
    ---------------------------------------------------------------------------------------------------------------
    REMARQUE:

    on separe colorb2 a colorb et effaceb2 a effaceb pour un menu particulier, car il possede 4 zones clicable alors
    que les autres seulements 3.
    cela permet de mieux gerer l'espace restant (visuelement)
    """
    txt=fontregle2.render(nom,1,color)
    txt_pos=txt.get_rect()
    txt_pos.centerx = ecran.get_rect().centerx 
    txt_pos.centery = pos
    fenetre.blit(txt,txt_pos)
    
def fchoix2(joueur):
    """
    le choix que le joueur fait lorsqu'il est dans le 2eme menu
    ---------------------------------------------------------------------------------------------------------------
    ENTREE:
        joueur:(string) le nom de compte du joueur (ou son nom), utilisé dans la fonction logout
    ---------------------------------------------------------------------------------------------------------------
    SORTIE:
        le type de sortie est different (avantage du haut niveau python)
        la sortie est soit vide, soit int soit string
    ---------------------------------------------------------------------------------------------------------------
    REMARQUE:

    la sortie serra interpretré dans le main, qui permetra au joueur d'interagir au clavier/souris avec
    les parcours de menu

    la touche echap permet toujours de revenir au menu precredent
    """
    (sx,sy)=pygame.mouse.get_pos()
    for event in pygame.event.get():

        
        if event.type==KEYDOWN:
            if event.key == K_ESCAPE:
                return 1
        
        elif event.type==QUIT:
            logout(joueur)
            jeu=False
            pygame.quit()
            return 0              
        
        
        if (sx>240 and sx<468) and (sy>100 and sy<150):
            effaceb(127)
            colorb(127,"nouveau",(0,0,255))
        
        else:
            effaceb(127)
            colorb(127,"nouveau",(255,255,255))
       
        if(sx>240 and sx<468) and (sy>227 and sy<277):
            effaceb(254)
            colorb(254,"editer",(0,0,255))
      
        else:
            effaceb(254)
            colorb(254,"editer",(255,255,255))

        if (sx>240 and sx<468) and (sy>354 and sy<404):
            effaceb(380)
            colorb(380,"parametre",(0,0,255))
       
        else:
            effaceb(380)
            colorb(380,"parametre",(255,255,255))

             
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            
                    
            if (sx>240 and sx<468) and (sy>100 and sy<150):
                print("clic nouveau")
                return "nouveau"
                    
            if(sx>240 and sx<468) and (sy>227 and sy<277):
                print("clic editer")
                return "editer"

            if (sx>240 and sx<468) and (sy>354 and sy<404):
                print("clic parametre")
                return "parametre"
                
                

        
   # else:
     #   return 0
        
                

def fchoix3(joueur):
    """
    le choix que le joueur fait lorsqu'il est dans le 3eme menu
    ---------------------------------------------------------------------------------------------------------------
    ENTREE:
        joueur:(string) le nom de compte du joueur (ou son nom), utilisé dans la fonction logout
                        et dans les chemin d'acces de fichier
    ---------------------------------------------------------------------------------------------------------------
    SORTIE:
        le type de sortie est different (avantage du haut niveau python)
        la sortie soit int soit string

        le 1er argument de sortie correspond souvent au niveau de difficulté que le joueur choisie
        le 2eme argument correspont au numeros de la grille qu'il veut jouer si il a choisi de jouer a un niveau qu'il a lui meme deja cree
    ---------------------------------------------------------------------------------------------------------------
    REMARQUE:

    la sortie serra interpretré dans le main, qui permetra au joueur d'interagir au clavier/souris avec
    les parcours de menu

    la touche echap permet toujours de revenir au menu precredent
    """
    (sx,sy)=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if (sx>240 and sx<468) and (sy>80 and sy<130):
            effaceb2(100)
            colorb2(100,"facile",(0,0,255))
        
        else:
            effaceb2(100)
            colorb2(100,"facile",(255,255,255))
       
        if(sx>240 and sx<468) and (sy>180 and sy<230):
            effaceb2(200)
            colorb2(200,"moyen",(0,0,255))
      
        else:
            effaceb2(200)
            colorb2(200,"moyen",(255,255,255))

        if (sx>240 and sx<468) and (sy>280 and sy<330):
            effaceb2(300)
            colorb2(300,"difficile",(0,0,255))
       
        else:
            effaceb2(300)
            colorb2(300,"difficile",(255,255,255))


        if (sx>240 and sx<468) and (sy>380 and sy<430):
            effaceb2(400)
            colorb2(400,"mes creations",(0,0,255))
        
        else:
            effaceb2(400)
            colorb2(400,"mes creations",(255,255,255))
        
        if event.type==KEYDOWN:
            if event.key == K_ESCAPE:
                return (1,0)
        
        elif event.type==QUIT:
                logout(joueur)
                jeu=False
                pygame.quit()
                return (0,0)             
        
        elif event.type==MOUSEBUTTONDOWN and event.button==1:
                if (sx>240 and sx<468) and (sy>80 and sy<130):
                       print("clic facile")
                       return ("facile",0)
                if(sx>240 and sx<468) and (sy>180 and sy<230):                  
                    print("clic editer")
                    return ("moyen",0)

                if (sx>240 and sx<468) and (sy>280 and sy<330):
                        print("clic difficile, abandonne")
                        return ("difficile",0)

                if (sx>240 and sx<468) and (sy>380 and sy<430):
                    fmaxi=open("joueurs"+"//"+joueur+"//"+'num.txt','r')
                    maxi=0
                    for element in fmaxi:
                            maxi=maxi=+int(element)
                    if maxi==0:
                            effacealrt()
                            txt=font.render("tu n as pas cree de partie",1,(255,0,0))
                            txt_pos=txt.get_rect()
                            txt_pos.centerx = ecran.get_rect().centerx 
                            txt_pos.centery = 460
                            fenetre.blit(txt,txt_pos)
                            return (0,0)

                    repete=1
                    while repete==1:
                         #passage par chaine pour accepter toute les entree du joueur puis ensuite les selectionner
                             numniv=ask("ton niveau entre 1 et "+str(maxi),3,-1)
                             for caract in numniv:
                                     if ord(caract)<48 or ord(caract)>57: 
                                             numniv=-1
                                     
                             if int(numniv)>=1 and int(numniv)<=maxi: #numniv est forcement un int, car tout ces caracteres sont compris en ASCII entre 0 et 9, si ce n'est pas le cas il est devenu -1
                                     print ("perso",numniv)
                                     return ("perso",numniv)
                                     repete=0 
                    return (0,0) #arrive jamais normalement
                    



                
    else:
        return -1,-1 #necessaire de le mettre pour equilibre tout les sorties, qui seront utilisé dans le Main.py


def fchoixparam(joueur):
    """
    le choix que le joueur fait lorsqu'il est dans le menu parametre
    ---------------------------------------------------------------------------------------------------------------
    ENTREE:
        joueur:(string) le nom de compte du joueur (ou son nom), utilisé dans la fonction logout
                        et dans les chemin d'acces de fichier
    ---------------------------------------------------------------------------------------------------------------
    SORTIE:
        le type de sortie est different (avantage du haut niveau python)
        la sortie soit int soit string

        le 1er argument de sortie correspond souvent au niveau de difficulté que le joueur choisie
        le 2eme argument correspont au numeros de la grille qu'il veut jouer si il a choisi de jouer a un niveau qu'il a lui meme deja cree
    ---------------------------------------------------------------------------------------------------------------
    REMARQUE:

    la sortie serra interpretré dans le main, qui permetra au joueur d'interagir au clavier/souris avec
    les parcours de menu

    la touche echap permet toujours de revenir au menu precredent
    """
    (sx,sy)=pygame.mouse.get_pos()
    for event in pygame.event.get():
        
        if event.type==KEYDOWN:
            if event.key == K_ESCAPE:
                return (1)


        if (sx>190 and sx<528) and (sy>100 and sy<150):#rect = pygame.Rect([240, 100, 228, 50])
            effaceb(127)
            colorb(127,"meilleurs scores",(0,0,255))
        
        else:
            effaceb(127)
            colorb(127,"meilleurs scores",(255,255,255))
       
        if(sx>190 and sx<528) and (sy>227 and sy<277):#rect = pygame.Rect([240, 227, 228, 50])
            effaceb(254)
            colorb(254,"regles du jeu",(0,0,255))
      
        else:
            effaceb(254)
            colorb(254,"regles du jeu",(255,255,255))

        if (sx>190 and sx<528) and (sy>354 and sy<405):
            effaceb(380)
            colorb(380,"credits",(0,0,255))
       
        else:
            effaceb(380)
            colorb(380,"credits",(255,255,255)) 

        
        if event.type==QUIT:
                logout(joueur)
                jeu=False
                pygame.quit()
                return (0)             
 
        if event.type==MOUSEBUTTONDOWN and event.button==1:
                if (sx>190 and sx<528) and (sy>100 and sy<150):
                    print("clic meilleurs scores")
                    return ("score")
                if(sx>190 and sx<528) and (sy>227 and sy<277):                   
                    print("clic regle du jeu")
                    return ("regle")

                if (sx>190 and sx<528) and (sy>354 and sy<405):
                    print("clic credit")
                    return ("credit")
    

def fchoixscore(joueur):
    """
    le choix que le joueur fait lorsqu'il est dans le parametre/score
    ---------------------------------------------------------------------------------------------------------------
    ENTREE:
        joueur:(string) le nom de compte du joueur (ou son nom), utilisé dans la fonction logout
                        et dans les chemin d'acces de fichier
    ---------------------------------------------------------------------------------------------------------------
    SORTIE:
        le type de sortie est different (avantage du haut niveau python)
        la sortie soit int soit string

        le 1er argument de sortie correspond souvent au niveau de difficulté que le joueur choisie
        le 2eme argument correspont au numeros de la grille qu'il veut jouer si il a choisi de jouer a un niveau qu'il a lui meme deja cree
    ---------------------------------------------------------------------------------------------------------------
    REMARQUE:

    la sortie serra interpretré dans le main, qui permetra au joueur d'interagir au clavier/souris avec
    les parcours de menu

    la touche echap permet toujours de revenir au menu precredent
    """
    (sx,sy)=pygame.mouse.get_pos()
    for event in pygame.event.get():
        
        if event.type==KEYDOWN:
            if event.key == K_ESCAPE:
                return (1)

        if (sx>240 and sx<468) and (sy>100 and sy<150):#rect = pygame.Rect([240, 100, 228, 50])
            effaceb(127)
            colorb(127,"facile",(0,0,255))
        
        else:
            effaceb(127)
            colorb(127,"facile",(255,255,255))
       
        if(sx>240 and sx<468) and (sy>227 and sy<277):#rect = pygame.Rect([240, 227, 228, 50])
            effaceb(254)
            colorb(254,"moyen",(0,0,255))
      
        else:
            effaceb(254)
            colorb(254,"moyen",(255,255,255))

        if (sx>240 and sx<468) and (sy>354 and sy<404):
            effaceb(380)
            colorb(380,"difficile",(0,0,255))
       
        else:
            effaceb(380)
            colorb(380,"difficile",(255,255,255))
            
        if event.type==QUIT:
                logout(joueur)
                jeu=False
                pygame.quit()
                return (0)             
        
        elif event.type==MOUSEBUTTONDOWN and event.button==1:
                if (sx>240 and sx<468) and (sy>100 and sy<150):
                    print("clic facile")
                    return ("sc_facile")
                if(sx>240 and sx<468) and (sy>227 and sy<277):                  
                    print("clic moyen")
                    return ("sc_moyen")

                if (sx>240 and sx<468) and (sy>354 and sy<404):
                    print("clic difficile")
                    return ("sc_difficile")










def choixgrille(joueur):
    """
    le choix que le joueur fait lorsqu'il est dans le menu selection de niveau,
    il peut choisir une grille parmis les 6 proposé pour chaque niveau de difficulté
    ---------------------------------------------------------------------------------------------------------------
    ENTREE:
        joueur:(string) le nom de compte du joueur (ou son nom), utilisé dans la fonction logout
    ---------------------------------------------------------------------------------------------------------------
    SORTIE:
        le type de sortie est different (avantage du haut niveau python)
        la sortie soit int soit string

        Si l'argument de sortie est positif alors c'est le choix de grille du joueur
        Si l'argument de sortie est negatif c'est simplement de la gestion de menu
    ---------------------------------------------------------------------------------------------------------------
    REMARQUE:

    la sortie serra interpretré dans le main, qui permetra au joueur d'interagir au clavier/souris avec
    les parcours de menu

    la touche echap permet toujours de revenir au menu precredent
    """
    (sx,sy)=pygame.mouse.get_pos()
    for event in pygame.event.get():
        
        if event.type==KEYDOWN:
            if event.key == K_ESCAPE:           
                return -2
        
        elif event.type==QUIT:
            logout(joueur)                                                  
            jeu=False
            pygame.quit()
            return -1

        elif event.type==MOUSEBUTTONDOWN:
            if event.button==1:
                (sx,sy)=pygame.mouse.get_pos()

                k=6
                h=pgrilley
                decale=0
                ligne=1
                while 0<k:
                    if ligne==1:
                        num=(7-k)
                    if ligne==2:
                        num=(4-k)

                    if(sx>pgrillex+taille_pgrille*(num-1)+ decale)and(sx<pgrillex+taille_pgrille*(num)+ decale )and(sy>h)and(sy<h+taille_pgrille):
                        if ligne==1:
                            print num
                            return num
                        else:
                            print num+3
                            return num+3

                    decale=decale+63
                    if num==3:
                        decale=0
                        h=pgrilleyy
                        ligne=2
                    k-=1
        
    else:
             return 0



def logout(joueur):
    """
    fait apparaitre en haut du fichier log et la deconnexion avec
    le nom du compte et la date
    ---------------------------------------------------------------------------------------------------------------
    ENTREE:
        joueur:(string) qui contient le nom du compte (nom du joueur)
    ---------------------------------------------------------------------------------------------------------------
    """
    date=time.strftime('%d/%m/%y %H:%M:%S',time.localtime())
    
    fichier_log=open("joueurs"+"//"+'log.txt','r')  #on ne peut seulement ajouter du contenu dans un fichier a la fin,
    totale=date+' deconnexion de '+joueur+'\n'+ fichier_log.read() #donc pour ajouter du contenu au debut, on copie tout le fichier txt, ecrase ce qui est deja la, ecrit nos information, et colle ce qu'on a copier avant(totale)
    fichier_log.close()

    fichier_log=open("joueurs"+"//"+'log.txt','w')
    fichier_log.write(totale)
    fichier_log.close()
    


def login(joueur,nv):
    """
    fait apparaitre en haut du fichier log et la connexion ou la creation
    le nom du compte et la date
    si le joueur n'as pas de compte, la fonction ecrit creation
    si le joueur a deja un compte, et le recupere, alors la fonction ecrit connexion
    ---------------------------------------------------------------------------------------------------------------
    ENTREE:
        joueur:(string) qui contient le nom du compte (nom du joueur)
    ---------------------------------------------------------------------------------------------------------------
    """
    date=time.strftime('%d/%m/%y %H:%M:%S',time.localtime())
    if nv==1:
            action=' creation de '
    else:
            action=' connexion de '

    fichier_log=open("joueurs"+"//"+'log.txt','r')  
    totale=date+action+joueur+'\n'+ fichier_log.read() 
    fichier_log.close()

    fichier_log=open("joueurs"+"//"+'log.txt','w')
    fichier_log.write(totale)
    fichier_log.close()

        

clock = pygame.time.Clock() 
def stats_gochrono(temps):
        """
        on affiche le chronometre a l'ecran lors d'une partie classique
        qui est associé au joueur et a la grille en cour
        ---------------------------------------------------------------------------------------------------------------
        ENTREE:
            temps:(int)contient le temps en seconde*60 
        ---------------------------------------------------------------------------------------------------------------
        REMARQUE:

        le prgrm converti "temps" en seconde, et en minutes pour faire l'affichage

        Le temps n'est qu'un compteur couplé a une limitation de tour de boucle, en effet on LIMITE le tour de boucle a 60tours/secondes
        et increment(+1) la variable temps(Main.py) a chaque tours de boucle.
        donc touts les 60tours (soit a chaque fois que temps est un multiple de 60), le temps reel passé est de 1secondes
        on peut ainsi donc obtenir incrementer mes minutes quand la variable temps est multiple de 60*60
        """
        total_seconds = temps // 60
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        afficher = "temps: {0:02}:{1:02}".format(minutes, seconds)
        text = font.render(afficher, True, (0,0,0))
        ##efface_temp() #nettoie la zone pour un prochain collage
        #fenetre.blit(text, [70, 430])
        #fenetre.blit(text,(76,240))
        fenetre.blit(text,(76,300))
        clock.tick(60)  #limitation de vitesse a 60t/s 


def stats_aide(kaide):
        """
        on affiche les aides restantes a l'ecran lors d'une partie classique
        qui est associé au joueur et a la grille en cour
        ENTREE:
            kaide:(int)contient le nombre d'aide restante 
        ---------------------------------------------------------------------------------------------------------------
        """
        mot="aide restante(h): "+str(kaide)
        txt=font.render(mot,1,(0,0,0))
        fenetre.blit(txt,(76,240))



def stats_saisi(ksaisi):
        """
        on affiche le nombres totales de saisie lors d'une partie classique
        qui est associé au joueur et a la grille en cour
        ENTREE:
            ksaisi:(int)contient le nombre totale de saisi
        ---------------------------------------------------------------------------------------------------------------
        """
        mot="coup: "+str(ksaisi)
        txt=font.render(mot,1,(0,0,0))
        fenetre.blit(txt,(76,270))


def bsave():
        """
        bouton "sauvegarder", lorsque le curseur de la souris est a l'exterieur du bouton (couleur blanc)
        le bouton est visible en partie classique et édité
        """
        txt=titrespe.render("sauvegarder",1,(255,255,255))#226
        fenetre.blit(txt,(40,360))

def bverif():
        """
        bouton "verification", lorsque le curseur de la souris est a l'exterieur du bouton (couleur blanc)
        le bouton est visible en partie classique et édité
        """
        txt=titrespe.render("verification",1,(255,255,255))
        fenetre.blit(txt,(40,410))

def bsolu():
        """
        bouton "solution", lorsque le curseur de la souris est a l'exterieur du bouton (couleur blanc)
        le bouton est visible en partie classique
        """
        txt=titrespe.render("solution",1,(255,255,255))
        fenetre.blit(txt,(40,410))
        
        
def bsavecolor():
        """
        bouton "sauvegarder", lorsque le curseur de la souris est a l'interieur du bouton (couleur bleu)
        le bouton est visible en partie classique et édité
        """
        txt=titrespe.render("sauvegarder",1,(0,0,255))
        fenetre.blit(txt,(40,360))

def bverifcolor():
        """
        bouton "verification", lorsque le curseur de la souris est a l'interieur du bouton(couleur bleu)
        le bouton est visible en partie classique et édité
        """
        txt=titrespe.render("verification",1,(0,0,255))
        fenetre.blit(txt,(40,410))

def bsolucolor():
        """
        bouton "solution", lorsque le curseur de la souris est a l'interieur du bouton(couleur bleu)
        le bouton est visible en partie classique 
        """
        txt=titrespe.render("solution",1,(0,0,255))
        fenetre.blit(txt,(40,410))
        
        
def conv_coupleV(x):
    """
    fonction intermediaire de convertion
    ---------------------------------------------------------------------------------------------------------------
    ENTREE:
        x:(string) (contenu dans la copie) de self.structure
        la variable x est de taille 7, et est toujours sous cette forme "(xx,yy)"
    ---------------------------------------------------------------------------------------------------------------
    SORTIE:
        le sortie est un int 
    ex: conv_coupleV("(12,z8)")->12
    ex: conv_coupleV("(z2,17)")->2
        la sorite peut etre aussi un string
    ex: conv_coupleV("(zz,10)")-> "passe"
    on "passe" car le nombre somme verticale est null
    """

    if x[1]!='z' and x[2]!='z':
        return int(x[1]+x[2])

    elif x[1]=='z' and x[2]!='z':
        return int(x[2])

    else:
        return "passe"

        
    
def conv_coupleH(x):
    """
    fonction intermediaire de convertion
    ---------------------------------------------------------------------------------------------------------------
    ENTREE:
        x:(string) (contenu dans la copie) de self.structure
        la variable x est de taille 7, et est toujours sous cette forme "(xx,yy)"
    ---------------------------------------------------------------------------------------------------------------
    SORTIE:
        le sortie est un int 
    ex: conv_coupleH("(z8,12)")->12
    ex: conv_coupleH("(17,z2)")->2
        la sorite peut etre aussi un string
    ex: conv_coupleH("(10,zz)")-> "passe"
    on "passe" car le nombre somme verticale est null
    """
    if x[4]!='z' and x[5]!='z':
        return int(x[4]+x[5])

    elif x[4]=='z' and x[5]!='z':
        return int(x[5])

    else:
        return "passe"


def conv(tabl):
    """
    utilise pour convertir notre structure de tableau,
    cela permetra d'utiliser la fonction qui permet de calculer la solution de la grille (que le joueur creer)
    ---------------------------------------------------------------------------------------------------------------
    ENTREE:
        tabl:(string)tableau de sous tableau qui contient la structure de la grille
    ---------------------------------------------------------------------------------------------------------------
    SORITE:
        tabl:(type instance d'adresse?) contient des adresse necessaire pour la resolution de la grille
    ---------------------------------------------------------------------------------------------------------------
    REMARQUE:
        la fonction qui permet de calculer la solution d'une grille a etait trouvé sur internet (voir reference sur k1.py)
        nous nous somme debrouiller pour faire les convertions necessaire pour pouvoir rendre la fonction de resolution
        compatible a notre jeu. (dans le cadre du projet il est demandé d'afficher une solution de grille chose que nous avons
        fait, pas necessairement de faire un algorythme qui trouve la solutiond'une grille de kakuro)
    """
    type((tabl))
    print tabl
    for ligne in range(0,7):
        for col in range(0,7):
            if len(tabl[ligne][col])>1:
                vv=conv_coupleV(tabl[ligne][col])
                hh=conv_coupleH(tabl[ligne][col])
                print vv
                if vv=="passe":
                   tabl[ligne][col]=Brick(h=hh)
                elif hh=="passe":
                    tabl[ligne][col]=Brick(v=vv)
                else:
                    tabl[ligne][col]=Brick(v=vv,h=hh)

            if tabl[ligne][col]=='x':
                tabl[ligne][col]=Brick()
            if tabl[ligne][col]=='_':
                tabl[ligne][col]=Blank()
                
    return tabl



def solution(board):#ne marche qu'une fois
    """
    permet de calculer la solution de toute grille possible,
    pour plus d'explication voir k1.py
    ---------------------------------------------------------------------------------------------------------------
    ENTREE:
        board:(tableau adresse) est le tableau de stucture apres la convertion
    ---------------------------------------------------------------------------------------------------------------
    SORTIE:
        solution:(tableau int) contient la ou toutes les solutions de de la grille, (toutes les combinaisons)
        si l'algo ne trouve pas de solution, la fonction retourne un tableau vide
    """
    solution=[]
    tmp=[]
    #if nsolution==1:
            #ki = KakuroBoard(board)
    ki = KakuroBoard(board)
    for entries in ki.solve():
        for entry in entries:
                tmp.append(entry.possibleValues)
       
    for element in tmp:
        for sselement in element:
            solution.append(sselement)
    print solution
    return solution



def nbtrait(grandtab):
        """
        permet de compter le nombre de case modifiable vide que possede une grille
        ---------------------------------------------------------------------------------------------------------------
        ENTREE:
            grandtab:(string) contient le texte brute du niveau (encore plus brute que le tableau brute)
                    c'est exactement ce qui est mis dans un fichier texte
        ---------------------------------------------------------------------------------------------------------------
        SORTIE:
            k: (int) le compteur de trait dans la chaine
        """
        k=0
        for petittab in grandtab:
                for element in petittab:
                        if element=='_':
                                k+=1
        return k


def save_solution(joueur,solution):
        """
        lorsque le prgrm trouve une solution unique a une grille edite,
        le prgrm va ecrire la solution unique dans son repertoire
        ---------------------------------------------------------------------------------------------------------------
        ENTREE:
            joueur:(string) le nom du joueur, qui est aussi le nom du compte et du repertoire créer pour ranger les données de ce meme joueur
            solution:(tableau int) contient la solution unique
        """
        fnum=open("joueurs"+"//"+joueur+"//"+'num.txt','r')#on lis a quel save on est
        num=0
        for element in fnum:
                num=num+int(element)
        fnum.close()
        nom="savesolution"+str(num)+".txt"#+1 a la save

        chaine=""
        print solution
        for chiffre in solution:
                chaine=chaine+str(chiffre)
        fichier=open("joueurs"+"//"+joueur+"//"+nom,'w')
        fichier.write(chaine)
        fichier.close()
        

def lire_solution(nom,joueur):
        """
        lorsque le joueur decide de jouer a une grille qui a lui meme creer,
        le prgrm doit etre chargé les reponses qui ont était ecrite lorsque le joueur avait VERIFIER
        sa grille en mode edité
        ---------------------------------------------------------------------------------------------------------------
        ENTREE:
            joueur:(string) le nom du joueur, qui est aussi le nom du compte et du repertoire créer pour ranger les données de ce meme joueur
        ---------------------------------------------------------------------------------------------------------------
        REMARQUE:
            quand le joueur veut jouer a sa Xeme partie creer, le prgrm charge la Xeme solution
            de ce fait meme quand le joueur joue a des grilles qu'il a lui meme edité, il aura exacement les meme fonctionnalitée
            que les grilles qui sont deja intégré, (afficher une aide, afficher la solution...)
        """
        fichier=open("joueurs"+"//"+joueur+"//"+nom,'r')
        txt=fichier.read()
        fichier.close()
        print "txt"
        print txt
        print "txt"
        solu=[]
        for caractere in txt:
                solu.append(int(caractere))
        print "solu"
        print solu
        print "solu"
        return solu
        

def txtedite(pnum):
    """
    afficher un masg alerte pour avertir que la grille cree a
    bien etati cree
    ---------------------------------------------------------------------------------------------------------------
    ENTRE:
        pnum:(int) correspond au nombre grilles sauvegardé par le joueur
    """
    fenetre.blit(font.render("ta grille "+str(pnum)+" est sauvegarde", 1, (255,0,0)), (288,456))
    
def erreurchiffre():
        """
        afficher un msg alerte lors d'une mauvaise saisi
        dans une case modifiable en partie classique
        """
        txt="erreur saisie: mets un chiffre entre 1 et 9"
        fenetre.blit(font.render(txt, 1, (255,0,0)), (288,456)) #coordonné du txt dans ask a ce moment
        

def erreuraide():
        """
        afficher un msg alerte lorsque le joueurs veut utiliser une aide 
        alors qu'il n'y en a plus de disponible
        """
        efface()
        txt="tu as utilise toutes tes aides"
        fenetre.blit(font.render(txt, 1, (255,0,0)), (288,456)) #coordonné du txt dans ask a ce moment
        
#tableau utilisé dans recherche        
tabmodif=[1,2,3,4,5,6,7,8,9]
tabnlettre=['a','b','c','d','e','f','g','h','i']
#tableau utilisé dans recherche
def recherche(dbtligne,dbtcol,grillemodifiable):
    """
    parcour grillemodifiable a partir de la ligne dbtligne et de la colonne dbtcol
    ---------------------------------------------------------------------------------------------------------------
    ENTREE:
        grillemodifaible:(tableau int et char) qui a pour valeur self.grillemodifiable, il contient 7 sous-tableau de 7colonnes
        dbtligne:(int) correspond au rang de la ligne
        dbtcol:(int) correspond au rand du de la colonne
    ---------------------------------------------------------------------------------------------------------------
    REMARQUE:
        le prgrm parcour grillemodifiable a partir de la ligne dbtligne et de la colonne dbtcol et s'arrete lorsque
        qu'un element vaut un chiffre (int) entre 1 et 9,
        il va renvoyer la position de ligne, de la colonne+1 ou la fonction c'est arreté, et la valeur convertit: (a l'aide des tableaux definis 10lignes plus haut)
                                                                                                            1->'a'
                                                                                                            2->'b'
                                                                                                            3->'c'
                                                                                                              ...
                                                                                                            9->'i'
        ->s'il est deja a la derniere colonne on increment la ligne et initialise la colonne a 0

        ->il n'arrivera jamais APRES la 7eme ligne et la 7eme colonne, pas besoin de gerer le cas où la ligne depasse donc 6
    

    """
    conv='_'
    for ligne2 in range(dbtligne,7): 
        for col2 in range(dbtcol,7):
            if grillemodifiable[ligne2][col2]!='x':
                for i in range(0,9):
                        if tabmodif[i]==grillemodifiable[ligne2][col2]:
                            conv=tabnlettre[i]
                if col2==6:
                    return ligne2+1,0,conv #ligne ne depassera jamais 6
                
                return ligne2,col2+1,conv
            if col2==6:
                dbtcol=0
            
    
    return (0,0,0)







def reprendre_stats(chemin):
    """
    permet de lire dans le fichier txt pour reprendre les stats(aide restante, nombre de saisi/coups, et le temps en seconde*60)
    de la grille que l'on va charger
    ---------------------------------------------------------------------------------------------------------------
    ENTREE:
        chemin:(string) le chemin d'acces a la sauvegarde
     ---------------------------------------------------------------------------------------------------------------   
    SORTIE:
    de type: kaide,ksaisi,temps
        
         kaide:(int) aides restantes associé a la partie du jouer
         ksaisi:(int) nombre de coup restant associé a la partie du joueur
         temps:(int) le temps en seconde*60 associé a la partie du joueur
    
    """
    kaide=""
    ksaisi=""
    temps=""
    stats=[kaide,ksaisi,temps]
    i=0
    with open(chemin,'r') as fichier:
        for ligne in fichier:
            ligne_stats=""
            for carac in ligne:
                if carac!='\n':
                   stats[i]=stats[i]+carac
            i+=1
    kaide=int(stats[0])
    ksaisi=int(stats[1])
    temps=int(stats[2])
    return kaide,ksaisi,temps
    
        
def reset_grille(tabl):
        """
        permet de faire un reset de la grille
        ---------------------------------------------------------------------------------------------------------------
        ENTREE
            tabl:(tableau de int et char) contient uniquement des chiffre (int) entre 0 et 9 et le caracetere "x"
                    il est composé de sous tableau de taille 7 possedent tous 7 colonnes
                    tabl est le self.grillemodifiable
        ---------------------------------------------------------------------------------------------------------------
        REMARQUE:
            le prgrm parour tabl, et a chaque fois qu'il croise un chiffre il va le remplacer par 0
            il gere aussi l'affichage de la case modifiable vierge
        """
        for ligne in range(0,7):
                for col in range(0,7):
                    if tabl[ligne][col]!='x':
                        tabl[ligne][col]=0
                        fenetre.blit(case_blanc,(grillex+col*taille_sprite+col+1 , grilley+ligne*taille_sprite+ligne+1))
         
        return tabl
        






def meilleurstats(niv,aide,saisi,temps,joueur):
    """
    permet d'enregistrer les stats du joueur associée niveau s'ils sont les meilleurs parmis touts les joueurs
    ---------------------------------------------------------------------------------------------------------------
    ENTREE
        niv:(string) le prenom du fichier .txt, qui est celui du niveau qui viens d'etre termine
        aide:(int) nombre d'aide restant du niveau termine
        saisi:(int) nombre totale de saisie du niveau termine
        temps:(int) nombre totale de seconde du niveau termine, en seconde*60
        joueur:(string) le nom du joueur (qui est aussi son nom de compte)
    ---------------------------------------------------------------------------------------------------------------
    REMARQUE:

    lis un fichier qui contient les meilleurs scores, si un score est plus eleve (ou egale) alors il est remplace par le nouveau,
    on ajoute aussi le nom du joueur qui a fait le meilleur score
    """
    fichier=open("img//meilleur_score//meilleur"+niv,"r")
    txt=fichier.read()
    fichier.close()
 
    s=""
    p=""
    stats=[]
    i=-2
    score=1
    ligne=-1
    while ligne<2:
        ligne+=1
        s=""
        p=""
        score=1
        i+=1
        while txt[i+1]!='\n':
            i+=1
            if score==1 and txt[i]!=' ':
                s=s+txt[i]
            if score==0:
                p=p+txt[i]
            if txt[i]==' ':
                score=0

        stats.append(s)
        stats.append(p)
        
    if stats[0]>=aide:
        stats[0]=str(aide)
        stats[1]=joueur

    if stats[2]>=saisi:
        stats[2]=str(saisi)
        stats[3]=joueur


    if stats[4]>=temps:
        stats[4]=str(temps)
        stats[5]=joueur

    print stats

    fichier=open("img//meilleur_score//meilleur"+niv,"w")
    for i in range(0,6):
        if i%2==0:
            fichier.write(stats[i]+' ')
        else:
            fichier.write(stats[i]+'\n')
    fichier.close()
    

    
                        
            
#tableau chiffre defini dans Constante.py
    
def affichescoref(choix):
    """
    permet d'afficher les meilleurs scores de toutes les grilles en fonction de 'choix'
    ---------------------------------------------------------------------------------------------------------------
    ENTREE
        choix:(string) la fin du nom du ficher qui va contenir le niveau des parties des sauvegardes,
             pour differencier 'facile','moyen' et 'difficile'
    ---------------------------------------------------------------------------------------------------------------
    """
    decalx=0
    decaly=0
    for i in range (1,7):
        fichier=open("img//meilleur_score//meilleurniv"+choix+chiffre[i]+".txt","r")#chiffre[i] definis dans Constante.py
        txt=fichier.read()
        fichier.close()
        aide,saisi,temps=score(txt)
        txtaide=font.render(aide,1,(255,255,255))
        txtsaisi=font.render(saisi,1,(255,255,255))
        txttemps=font.render(temps,1,(255,255,255))
        txt=font1.render("grille "+chiffre[i],1,(0,0,0))
        fenetre.blit(txt,(64+decalx+15, 170+decaly-40) )
        fenetre.blit(txtaide, (64+decalx, 170+decaly) )
        fenetre.blit(txtsaisi,(64+decalx, 195+decaly ) )
        fenetre.blit(txttemps,(64+decalx, 220+decaly) )
        decalx+=230
        if i==3:
            decalx=0
            decaly=230
        
        


def score(txt):
    """
    fonction annexe de affichescoref qui permet d'extraire toutes les stats d'un fichier
    ainsi que le nom du joueur les ayants faits
    ---------------------------------------------------------------------------------------------------------------
    ENTREE
        txt:(string) la chaine de caractere recupere dans le fichier precedement
    ---------------------------------------------------------------------------------------------------------------
    """
    aide=-1
    saisi=-1
    temps=-1
    ligne=""
    tabl=[aide,saisi,temps]
    i=0
    for caractere in txt:
        if caractere!='\n':
            ligne=ligne+caractere
        else:
            tabl[i]=ligne
            i+=1
            ligne=""

    if tabl[0]=="-1 ": #on ecrit "-1" dans un fichier pour afficher un espace " " ce qui permet d'initialiser les affichages a vide des meilleurs score quand il n y en a pas
        tabl[0]=" "
    if tabl[1]=="-1 ":
        tabl[1]=" "
    if tabl[2]=="-1 ":
        tabl[2]=" "
    else:
        tabl[2]=convtemp(tabl[2])
    
    tabl[0]="aide: "+tabl[0]
    tabl[1]="coup: "+tabl[1]
    
    tabl[2]="temps: "+tabl[2]
    
    return tabl[0],tabl[1],tabl[2]


            
def convtemp(lignetemp):
    """
    permet de convertir le temps en seconde*60 contenu dans le 1er nombre de la 3eme ligne
    d'un fichier txt
    ENTREE
        lignetemp:(string) est la ligne en chaine de caractere ecrit dans le fichier txt
                qui contient un temps (ou -1 s'il n'y en a pas, or la fonction n'est appele uniquement quand le temps est different de -1
                donc ce cas n'arrive jamais) en seconde*60
    ---------------------------------------------------------------------------------------------------------------
    SORTIE
        txtemp+nom:(string) qui contient le temps convertit (toujours en string) avec le meme nom (le meme mot contenu apres le temps dans le fichier txt)
    """

    i=-1
    temp=""
    while lignetemp[i+1]!=" ":
        i+=1
        temp=temp+lignetemp[i]

        
  
    nom=""
    i+=1
    while i<len(lignetemp):
        nom=nom+lignetemp[i]
        i+=1
   
    temp=int(temp)
    total_seconds = temp // 60
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    txttemp = "{0:02}:{1:02}".format(minutes, seconds)
    return txttemp+nom




    
def enteteselec(choix):
        """
        fait de simple affichage de texte pendant la selection de grille en fonction du niveau de difficulte choisit par le joueur
        ---------------------------------------------------------------------------------------------------------------
        ENTREE
            choix:(string) est le niveau de difficulte choisit par le joueur
        ---------------------------------------------------------------------------------------------------------------
        """
        if choix=="facile":
            fenetre.blit(facile,(0,0))
        elif choix=="moyen":
            fenetre.blit(moyen,(0,0))
        elif choix=="difficile":
            fenetre.blit(difficile,(0,0))
        txt=titre.render(choix,1,(0,0,255))
        txt_pos=txt.get_rect()
        txt_pos.centerx = ecran.get_rect().centerx 
        txt_pos.centery = 20 
        fenetre.blit(txt,txt_pos)
        numgrille()
        pygame.display.flip()
        

def entetesc(choix):
    """
     fait de simple affichage de texte pendant l'affichage des scores en fonction du niveau de difficulte choisit par le joueur
    ---------------------------------------------------------------------------------------------------------------
    ENTREE
        choix:(string) est le niveau de difficulte choisit par le joueur
    ---------------------------------------------------------------------------------------------------------------
    """
    fenetre.fill((185,122,87))
    if choix=="sc_facile":
        affichescoref("a")
        #txt=titre.render("score facile",1,(0,0,255))
        txt=fontregle2.render("score facile",1,(0,0,255))
    elif choix=="sc_moyen":
        affichescoref("b")
        #txt=titre.render("score moyen",1,(0,0,255))
        txt=fontregle2.render("score moyen",1,(0,0,255))
    elif choix=="sc_difficile":
        affichescoref("c")
        #txt=titre.render("score difficile",1,(0,0,255))
        txt=fontregle2.render("score difficile",1,(0,0,255))
    
    txt_pos=txt.get_rect()
    txt_pos.centerx = ecran.get_rect().centerx 
    txt_pos.centery = 20 
    fenetre.blit(txt,txt_pos)
    pygame.display.flip()



def affregle():
    """
    fait l'affichage des regles et des raccourcis du jeu, dans parametre>regles_de_jeu
    """
    fenetre.fill((185,122,87))
    txt=fontregle2.render("regle",1,(0,0,255))
    txt_pos=txt.get_rect()
    txt_pos.centerx = ecran.get_rect().centerx 
    txt_pos.centery = 70
    fenetre.blit(txt,txt_pos)

    txt=fontregle.render("remplir toutes les cases vides avec des chiffres",1,(255,255,255)) #(226,266,266)
    fenetre.blit(txt,(50,110))

    txt=fontregle.render("de sorte que la somme de ses chiffres",1,(255,255,255))
    fenetre.blit(txt,(50,130))
    txt=fontregle.render("soit egale a la rangee correspondante.",1,(255,255,255))
    fenetre.blit(txt,(50,150)) 
    txt=fontregle2.render("raccourcis",1,(0,0,255))
    txt_pos=txt.get_rect()
    txt_pos.centerx = ecran.get_rect().centerx 
    txt_pos.centery = 270 
    fenetre.blit(txt,txt_pos)

    txt=fontregle.render("h",1,(0,0,0))
    fenetre.blit(txt,(50,320))
    txt=fontregle.render(": permet d'afficher une aide",1,(255,255,255))
    fenetre.blit(txt,(70,320))
    
    txt=fontregle.render("r",1,(0,0,0))
    fenetre.blit(txt,(50,340))
    txt=fontregle.render(": permet de retourner a la derniere sauvegarde",1,(255,255,255))
    fenetre.blit(txt,(70,340))
    
    txt=fontregle.render("ctrl+r",1,(0,0,0))
    fenetre.blit(txt,(50,360))
    txt=fontregle.render(": permet de reinitialiser la grille",1,(255,255,255))
    fenetre.blit(txt,(130,360))
    
    txt=fontregle.render("clic gauche",1,(0,0,0))
    fenetre.blit(txt,(50,380))
    txt=fontregle.render(": ajoute un element a la grille",1,(255,255,255))
    fenetre.blit(txt,(195,380))

    txt=fontregle.render("clic droit",1,(0,0,0))
    fenetre.blit(txt,(50,400))
    txt=fontregle.render(": supprime un element a la grille",1,(255,255,255))
    fenetre.blit(txt,(180,400))

    txt=fontregle.render("ECHAP",1,(0,0,0))
    fenetre.blit(txt,(50,420))
    txt=fontregle.render(": permet toujours de revenir au menu precedent",1,(255,255,255))
    fenetre.blit(txt,(120,420))
    pygame.display.flip()




def affcredit():
    """
    fait l'affichage des credtis, dans parametre>credtis
    """
    fenetre.fill((185,122,87))
    txt=fontregle2.render("developpeurs",1,(0,0,255))
    txt_pos=txt.get_rect()
    txt_pos.centerx = ecran.get_rect().centerx 
    txt_pos.centery = 70
    fenetre.blit(txt,txt_pos)

    txt=fontregle.render("dilay david",1,(255,255,255))
    txt_pos=txt.get_rect()
    txt_pos.centerx = ecran.get_rect().centerx 
    txt_pos.centery = 110
    fenetre.blit(txt,txt_pos)

    txt=fontregle.render("li laurent",1,(255,255,255))
    txt_pos=txt.get_rect()
    txt_pos.centerx = ecran.get_rect().centerx 
    txt_pos.centery = 130
    fenetre.blit(txt,txt_pos)

    txt=fontregle.render("saverinadin jeanne",1,(255,255,255))
    txt_pos=txt.get_rect()
    txt_pos.centerx = ecran.get_rect().centerx 
    txt_pos.centery = 150
    fenetre.blit(txt,txt_pos)

    txt=fontregle.render("chansuk chatri",1,(255,255,255))
    txt_pos=txt.get_rect()
    txt_pos.centerx = ecran.get_rect().centerx 
    txt_pos.centery = 170
    fenetre.blit(txt,txt_pos)

    txt=fontregle2.render("remerciement",1,(0,0,255))
    txt_pos=txt.get_rect()
    txt_pos.centerx = ecran.get_rect().centerx 
    txt_pos.centery = 260
    fenetre.blit(txt,txt_pos)

    txt=fontregle.render("a notre encadrante severine affeldt",1,(255,255,255))
    txt_pos=txt.get_rect()
    txt_pos.centerx = ecran.get_rect().centerx 
    txt_pos.centery = 300
    fenetre.blit(txt,txt_pos)

    txt=fontregle.render("qui nous a soutenu tout au long du projet",1,(255,255,255))
    txt_pos=txt.get_rect()
    txt_pos.centerx = ecran.get_rect().centerx 
    txt_pos.centery = 320
    fenetre.blit(txt,txt_pos)

    fenetre.blit(descartes,(0,352))
    pygame.display.flip()
    
        

def numgrille():
    """
    permet de faire l'affichage des numeros de grille dans
    la selection de grille
    """
    decalx=0
    decaly=0
    for i in range (1,7):
        txt=font1.render("grille "+chiffre[i],1,(0,0,0))
        fenetre.blit(txt,(64+decalx+45, 170+decaly-105) )
        decalx+=220
        if i==3:
            decalx=0
            decaly=215
        

