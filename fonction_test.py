#! /usr/bin/env python
# -*- coding: utf-8 -*-


#############################################################################################################################
                                                    #fonction teste ##plan teste ##teste unitaire
#############################################################################################################################



#quelques fonctions unitaires qui vienne completer notre documentation


def teste_saisir_nombre(x,y,tempp):
        if saisir_nombre(x,y)==-1:
                print("erreur sur la saisie") #arrive lorsque le joueur entre un caractere compris entre 1et9...
                pygame.quit()
        if saisir_nombre(x,y)==0,0:
                print ("le joueur n a pas entrer un nombre entier compose d un caractere en 1et9")
                        
        else:
            print"saisir_nombre: OK"




                
def teste_sommehori(modifiable,debut):
        if sommehore(modifiable,debut)<0:
                print("erreur de comptage")#arrive lorsque on incremente k mais qu il se fait decrementer..
                pygame.quit()





def teste_doublon_verticale(self,fenetre):
        if doublon_verticale(fenetre)!=0 and doublon_verticale(fenetre)!=1:
                print("erreur") #le bool est initialisé a 1 et ne change que pour avoir la valeur 0..
                pygame.quit()



def teste_doublon_horizontale(self,fenetre):
        if doublon_horizontale(fenetre)!=0 and doublon_horizontale(fenetre)!=1:
                print("erreur") #le bool est initialisé a 1 et ne change que pour avoir la valeur 0..
                pygame.quit()



def teste_solution_utile(self):
        if solution_utile==[]:
                print("tu n'a pas besoin d'aide tu as deja finis le jeu")# n'arrivera pas car quand le joueurs entre un nbr le prgm faire direct le verification pour savoir si le niveau est termine,
                pygame.quit()                                            #si c est le cas, le prgm quitte le jeu et ne proposera pas l evenement pour afficher une reponse
                                                                         #(car l evenement pour afficher pour executer la solution est executer apres la fonction qui verifie si la grille est finis)



def teste_saisir(self,fenetre): 
        (a,b,c)=saisir(fenetre)
        if a!=1 or a!=0:
                print("erreur dans gestion de fenetre")
                pygame.quit()
        if len(b)!=7: #b doit toujours faire 7*7 et contient uniquements les elements 'x' et les chiffres en int
                print("erreur sur la grille")
                pygame.quit()
        if c!=1 or c!=0:
                print("erreur sur l evenement")
                pygame.quit()




def teste_char_nbr(listechar):  #listchar est un tableau contenant 2caractere parmis 'z','0','1','2'...'9' la sortie est le nombre (int) en concatenant les caracteres, ['1','8']-> 18 // ['7','z']->7
        res=char_nbr(listechar)
        if res<0 or res>99:
                print("erreur dans la passage char->int")
                pygame.quit()





def teste_afficher(self,fenetre):
        res=afficher(fenetre)
        if len(res)!=7:         #res doit toujours faire 7*7 et contient uniquements les elements 'x' et les chiffres en int
                print("erreur sur la grille")
                pygame.quit()



def teste_reset_grille(tabl):
        res=reset_grille
        if len(res)!=7:         #res doit toujours faire 7*7 et contient uniquements les elements 'x' et les chiffres en int
                print("erreur sur la grille") 
                pygame.quit()
