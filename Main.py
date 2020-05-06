#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import pygame.mixer
import os.path
import shutil

from pygame.locals import*
from Class import*
from Fonction import*
from Constante import*


import operator

#lancer le Main.py

############################################################################################################################
                                                    #information
############################################################################################################################

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




#fait sous windows et ubuntu avec
#python 2.7.13 windows 32bits  : https://www.python.org/downloads/release/python-2713/ 
#pygame 1.9.1 windows 32bits   : http://www.pygame.org/download.shtml
# /!\ ne pas prendre de version 64bits /!\


        
#############################################################################################################################
                                                    #main
#############################################################################################################################
        




#choix1=0 #pas utile
choix2=0
choix3=0
choix4=0
choixpartie=0
kedit=0
#choixparam=0

#solution grille installé facile
sa1=[1,2,5,3]
sa2=[9,7,4,1]
sa3=[6,8,7,9,2,1,1,8,9,3,9]
sa4=[9,8,7,3,7,5,1,2]
sa5=[3,9,1,4,2,3,1,8,9]
sa6=[4,9,9,3,1,4,8,1,2,6,9,8,4,3,1,2,1,2]

#solution grille installé moyen
sb1=[2,6,4,1,1,9,8,6,2,1,5,7,2,3,9,8,1,6,8,9,7]
sb2=[5,1,2,9,8,9,1,7,8,6,9,3,9,8,7,2,1,6,2,1,9,8]
sb3=[8,9,1,2,3,4,5,9,3,7,9,3,1,2,9,8,1,8]
sb4=[1,6,8,4,8,9,5,7,3,2,5,1]
sb5=[2,1,9,7,1,3,8,9,4,2,6,3,2,1,8,1]
sb6=[1,8,2,2,9,5,3,8,3,5,1,9,9,3,1,8,8,1,7,3,9,9,1,8]

#solution grille installé difficile
sc1=[6,2,7,2,7,8,1,9,1,4,8,9,3,2,1,9]
sc2=[3,9,6,9,1,8,4,9,8,3,7,8,7,1,8,5,8,1,2,9,9,3]
sc3=[1,7,2,8,4,9,1,9,2,4,3,3,9,2,7,7,3,1,9,8,1,5]
sc4=[6,2,9,6,2,8,4,6,5,1,4,9,7,4,3,6,3,7,3,1,7,5,8,9,9,7,1,2]
sc5=[3,5,2,7,5,2,1,7,9,6,8,6,2,4,5,1,7,8,5,9,7,1,8,6,9,4,5,6]
sc6=[2,4,1,8,1,2,4,7,6,3,5,6,9,2,4,3,9,8,3,1,1,2]

choixniv=0
joueur=""
jeu= True

fond=0
fond2=0
while jeu:
    if fond==0:
        fond=1                                        
        fenetre.fill((185,122,87))                #pour chaque menu, echap permet de retourner au menu d'avant
    fond1=0
    pygame.display.flip()
    tout=os.listdir("joueurs") #all in dossier
    #print tout
    dossier=[]
    for element in tout:
        if os.path.isdir("joueurs"+"//"+element)==True:
            dossier.append(element)

    print(dossier)

    
    if dossier==[]:
        #print "il n y a aucune partie"
        text=font2.render("aucune partie existante",1,(0,0,255))
        fenetre.blit(text,(20,10))
        #fenetre.blit(text,(grillex,grilley+7*taille_sprite+8+taille_sprite/2-25))
        
    else:
        #print "les partie de:",dossier
        longu=len(dossier)
        txt=font2.render("partie existante ("+str(longu)+") :",1,(0,0,255))
        fenetre.blit(txt,(20,10))
        
        colonne=1
        if longu>32:
            colonne=2
        if colonne==1:
            for i in range(0,longu):
                text=font.render(dossier[i],1,(255,255,255))
                fenetre.blit(text,(20,45+i*15))
        else:
            for i in range(0,longu):
                if i<30:
                    text=font.render(dossier[i],1,(255,255,255))
                    fenetre.blit(text,(20,45+i*15))
                else:
                    text=font.render(dossier[i],1,(255,255,255))
                    fenetre.blit(text,(410,0+(i-30)*15))
                    

    
   
    ecrire=1
    while ecrire==1:
        joueur=ask("ton prenom ",10,-1) #limitation a 30caracatere, car sinon ça risque de depasser le rectangle (pour les caracteres large comme 'M')
        if joueur!="niv" and joueur!="img": #on interdit ces prenoms meme si ca gene en rien le prgrm
             for caract in joueur: #faut qu'il y a au moin un caractere != espace pour la suite du prgm sinon pas possible de creer dossier
                 if caract!=" ":
                     ecrire=0
        
    print "bonjour",joueur
    
    print "je tourne"
    if os.path.isdir("joueurs"+"//"+joueur)==False: #si le joueur n est pas on le fait
        shutil.copytree("niv","joueurs"+"//"+joueur) #copie les niv original dans le dossier cree joueur, permet init a 0 toutes les saves
        #os.mkdir("joueurs"+"//"+joueur,0777)
        fichier_num=open("joueurs"+"//"+joueur+"//"+"num.txt",'w')
        fichier_num.write("0")
        fichier_num.close()
        
        login(joueur,1)
        #choix1=fchoix1() #le choix1 du menu1 ##pas utile
    else:
        login(joueur,0)
        
    

    
    while joueur!="":
        if fond1==0:
            fenetre.fill((185,122,87))
            text=font2.render("bonjour "+joueur,1,(0,0,0))
            fenetre.blit(text,(20,10))
            #bfond1()
            fond1=1
          

##        txt_joueur=titre.render("bonjour "+joueur,1,(255,255,255))
##        txt_joueur_pos=txt_joueur.get_rect()
##        txt_joueur_pos.centerx = ecran.get_rect().centerx #ecran defini dans constante
##        txt_joueur_pos.centery = ecran.get_rect().centery
##        txt_joueur_pos.centery = 20
##        fenetre.blit(txt_joueur,txt_joueur_pos)
       
      
        choix2=fchoix2(joueur) #le choix2 du menu2

        creation=0
        pygame.display.flip()
        if choix2==1:
            logout(joueur)
            joueur="" #retour dans menu precedent
            fond=0
        fond4=0 #bool du param
        while choix2=="nouveau":
            if fond2==0:
                print "maj"
                #fenetre.blit(menu2,(0,0))
                fenetre.fill((185,122,87))
                temps = 0
                fond2=1
                creation=0
                
            
            #grille_modifiable=[]
            musiquejeu.stop()
            fond3=0 #bool selec niv
            fond1=0
            pygame.display.flip()
            choix3,numniv=fchoix3(joueur)
            creation=0
            if choix3==1:
                choix2=0
                fond2=0
  



################################################################################### FACILE ###################################################################################
##########################################################################......... FACILE .........##########################################################################
#########################################################.......................... FACILE .........................##########################################################
##########################################......................................... FACILE .........................................##########################################
###########################........................................................ FACILE ........................................................###########################  
                
            while choix3=="facile":
                if fond3==0:
##                    fenetre.blit(facile,(0,0))
##                    txt_joueur=titre.render(choix3,1,(0,0,255))
##                    txt_joueur_pos=txt_joueur.get_rect()
##                    txt_joueur_pos.centerx = ecran.get_rect().centerx #ecran defini dans constante
##                    txt_joueur_pos.centery = ecran.get_rect().centery
##                    txt_joueur_pos.centery = 20
##                    fenetre.blit(txt_joueur,txt_joueur_pos)
##                    pygame.display.flip()
                    enteteselec(choix3)
                    musiquejeu.stop()
                    #pygame.display.flip()
                    fond3=1
                    #temps = 0 #==>le mettre dans chaque init pour la reset
                choixniv=choixgrille(joueur)
                creation=0 #oui et en haut
                if choixniv==-2:
                    print "bye"
                    choix3=""
                    fond2=0
                

                while choixniv==1:
                    if creation==0:  #instruction faite qu une fois par partie
                        
                        if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsniva1.txt"):
                            kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsniva1.txt") #on verifie s'il existe une sauvegarde de la grille du joueur, si c'est le cas on lui charges les stats
                            print "tu continues ton ancienne partie"
                        else:
                            temps=0             #sinon on lui mets les stats par defaut
                            kaide=1
                            ksaisi=0
                       
                        fenetre.blit(partie,(0,0))
                        niveau=Niveau()
                        niveau.initcharge("niva1.txt",joueur,kaide,ksaisi)
                        niveau.generer(sa1,joueur,1)  #copie fichier txt en tableau plus tard pour gestion save
                        niveau.afficher(fenetre) #lecture du niveau
                        majtmp=0
                        #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                        pygame.display.flip()
                        creation=1 #pour ne pas bouclé la grille
                    if creation==1:
                            tempaddi=0 #temps additionnel, dans la suite
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)    ##/!\ impossible de revenir dans le menu precedent pdt une saisie /!\
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()#**--> ne pas mettre a jour l'affichae entre les stats apres stats efface
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      #OPTIMISATION: on ne lance les fonctions de verification/doublon seulement si il y a eu un saisie pdt ce tour!
                                    victoire=0                #c est intuile de verifier plusieurs fois la meme grille si aucune modification na etait apporte par le joueur
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              #on dit qu'une saisie erroné reste une saisie (saisi=1) car il y a eu une duree pdt laquelle le joueur a perdu du temp pour ecrire,
                                    victoire+=niveau.doublon_horizontale(fenetre)   #il faut donc la comptabilisé on faisant une maj
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    if victoire==4:
                                        choixniv=0
                                        fond3=0
                                        meilleurstats("niva1.txt",kaide,ksaisi,temps,joueur)
                                                                                                #temps=tempaddi #ici tempadii est le temps de jeu, avec la duree de la derniere saisie
                            if choixpartie==1:
                                choixniv=0
                                fond3=0
                            if choixpartie==2:
                                creation=0


                while choixniv==2:
                    if creation==0: 
                        if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsniva2.txt"):
                            kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsniva2.txt") 
                            print "tu continues ton ancienne partie"
                        else:
                            temps=0             
                            kaide=0
                            ksaisi=0
                        fenetre.blit(partie,(0,0))
                        niveau=Niveau()
                        niveau.initcharge("niva2.txt",joueur,kaide,ksaisi)
                        niveau.generer(sa2,joueur,1)  
                        niveau.afficher(fenetre) 
                        majtmp=0
                        pygame.display.flip()
                        #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                        creation=1 
                    if creation==1:
                            tempaddi=0 
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)   
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      
                                    victoire=0                
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              
                                    victoire+=niveau.doublon_horizontale(fenetre)  
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    if victoire==4:
                                        meilleurstats("niva2.txt",kaide,ksaisi,temps,joueur)
                                        choixniv=0
                                        fond3=0                                                                 
                            if choixpartie==1:
                                choixniv=0
                                fond3=0
                            if choixpartie==2:
                                creation=0
                                
                                        



                while choixniv==3:
                    if creation==0: 
                        if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsniva3.txt"):
                            kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsniva3.txt") 
                            print "tu continues ton ancienne partie"
                        else:
                            temps=0             
                            kaide=1
                            ksaisi=0
                        fenetre.blit(partie,(0,0))
                        niveau=Niveau()
                        niveau.initcharge("niva3.txt",joueur,kaide,ksaisi)
                        niveau.generer(sa3,joueur,1)  
                        niveau.afficher(fenetre) 
                        majtmp=0
                        pygame.display.flip()
                        #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                        creation=1 
                    if creation==1:
                            tempaddi=0 
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)   
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      
                                    victoire=0                
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              
                                    victoire+=niveau.doublon_horizontale(fenetre)  
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    if victoire==4:
                                        meilleurstats("niva3.txt",kaide,ksaisi,temps,joueur)
                                        choixniv=0
                                        fond3=0                                                                 
                            if choixpartie==1:
                                choixniv=0
                                fond3=0
                            if choixpartie==2:
                                creation=0
                                
                while choixniv==4:
                    if creation==0: 
                        if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsniva4.txt"):
                            kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsniva4.txt") 
                            print "tu continues ton ancienne partie"
                        else:
                            temps=0             
                            kaide=1
                            ksaisi=0
                        fenetre.blit(partie,(0,0))
                        niveau=Niveau()
                        niveau.initcharge("niva4.txt",joueur,kaide,ksaisi)
                        niveau.generer(sa4,joueur,1)  
                        niveau.afficher(fenetre) 
                        majtmp=0
                        pygame.display.flip()
                        #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                        creation=1 
                    if creation==1:
                            tempaddi=0 
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)   
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      
                                    victoire=0                
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              
                                    victoire+=niveau.doublon_horizontale(fenetre)  
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    if victoire==4:
                                        meilleurstats("niva4.txt",kaide,ksaisi,temps,joueur)
                                        choixniv=0
                                        fond3=0                                                                 
                            if choixpartie==1:
                                choixniv=0
                                fond3=0
                            if choixpartie==2:
                                creation=0


                while choixniv==5:
                    if creation==0: 
                        if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsniva5.txt"):
                            kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsniva5.txt") 
                            print "tu continues ton ancienne partie"
                        else:
                            temps=0             
                            kaide=1
                            ksaisi=0
                        fenetre.blit(partie,(0,0))
                        niveau=Niveau()
                        niveau.initcharge("niva5.txt",joueur,kaide,ksaisi)
                        niveau.generer(sa5,joueur,1)  
                        niveau.afficher(fenetre) 
                        majtmp=0
                        pygame.display.flip()
                        #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                        creation=1 
                    if creation==1:
                            tempaddi=0 
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)   
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      
                                    victoire=0                
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              
                                    victoire+=niveau.doublon_horizontale(fenetre)  
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    if victoire==4:
                                        meilleurstats("niva5.txt",kaide,ksaisi,temps,joueur)
                                        choixniv=0
                                        fond3=0                                                                 
                            if choixpartie==1:
                                choixniv=0
                                fond3=0
                            if choixpartie==2:
                                creation=0
                while choixniv==6:
                    if creation==0: 
                        if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsniva6.txt"):
                            kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsniva6.txt") 
                            print "tu continues ton ancienne partie"
                        else:
                            temps=0             
                            kaide=1
                            ksaisi=0
                        fenetre.blit(partie,(0,0))
                        niveau=Niveau()
                        niveau.initcharge("niva6.txt",joueur,kaide,ksaisi)
                        niveau.generer(sa6,joueur,1)  
                        niveau.afficher(fenetre) 
                        majtmp=0
                        pygame.display.flip()
                        #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                        creation=1 
                    if creation==1:
                            tempaddi=0 
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)   
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      
                                    victoire=0                
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              
                                    victoire+=niveau.doublon_horizontale(fenetre)  
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    if victoire==4:
                                        meilleurstats("niva6.txt",kaide,ksaisi,temps,joueur)
                                        choixniv=0
                                        fond3=0                                                                 
                            if choixpartie==1:
                                choixniv=0
                                fond3=0
                            if choixpartie==2:
                                creation=0
        







###########################.......................................................................................................................###########################  
##########################################......................................... FACILE ........................................##########################################
#########################################################.......................... FACILE ........................##########################################################         
##########################################################################.........................##########################################################################
#############################################################################################################################################################################
#############################################################################################################################################################################
##########################################################################.........................##########################################################################
#########################################################.......................... MOYEN .........................##########################################################
##########################################......................................... MOYEN .........................................##########################################
###########################.......................................................................................................................###########################  
                
            while choix3=="moyen":
                if fond3==0:
                    enteteselec(choix3)
                    musiquejeu.stop()
                    fond3=1
                choixniv=choixgrille(joueur)
                creation=0 #oui et en haut
                if choixniv==-2:
                    print "bye"
                    choix3=""
                    fond2=0
                

                while choixniv==1: #cette boucle permet de jouer au niva1, soit la 1er grille du niveau facile
                    if creation==0: 
                        if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsnivb1.txt"):
                            kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsnivb1.txt") 
                            print "tu continues ton ancienne partie"
                        else:
                            temps=0             
                            kaide=2
                            ksaisi=0
                        fenetre.blit(partie,(0,0))
                        niveau=Niveau()
                        niveau.initcharge("nivb1.txt",joueur,kaide,ksaisi)
                        niveau.generer(sb1,joueur,1)  
                        niveau.afficher(fenetre) 
                        majtmp=0
                        pygame.display.flip()
                        #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                        creation=1 
                    if creation==1:
                            tempaddi=0 
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)   
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      
                                    victoire=0                
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              
                                    victoire+=niveau.doublon_horizontale(fenetre)  
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    if victoire==4:
                                        meilleurstats("nivb1.txt",kaide,ksaisi,temps,joueur)
                                        choixniv=0
                                        fond3=0                                                                 
                            if choixpartie==1:
                                choixniv=0
                                fond3=0
                            if choixpartie==2:
                                creation=0
                                
                while choixniv==2:#cette boucle permet de jouer au niva2, soit la 2eme grille du niveau moyen
                    if creation==0: 
                        if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsnivb2.txt"):
                            kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsnivb2.txt") 
                            print "tu continues ton ancienne partie"
                        else:
                            temps=0             
                            kaide=2
                            ksaisi=0
                        fenetre.blit(partie,(0,0))
                        niveau=Niveau()
                        niveau.initcharge("nivb2.txt",joueur,kaide,ksaisi)
                        niveau.generer(sb2,joueur,1)  
                        niveau.afficher(fenetre) 
                        majtmp=0
                        pygame.display.flip()
                        #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                        creation=1 
                    if creation==1:
                            tempaddi=0 
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)   
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      
                                    victoire=0                
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              
                                    victoire+=niveau.doublon_horizontale(fenetre)  
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    if victoire==4:
                                        meilleurstats("nivb2.txt",kaide,ksaisi,temps,joueur)
                                        choixniv=0
                                        fond3=0                                                                 
                            if choixpartie==1:
                                choixniv=0
                                fond3=0
                            if choixpartie==2:
                                creation=0
                                
                while choixniv==3:
                    if creation==0: 
                        if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsnivb3.txt"):
                            kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsnivb3.txt") 
                            print "tu continues ton ancienne partie"
                        else:
                            temps=0             
                            kaide=2
                            ksaisi=0
                        fenetre.blit(partie,(0,0))
                        niveau=Niveau()
                        niveau.initcharge("nivb3.txt",joueur,kaide,ksaisi)
                        niveau.generer(sb3,joueur,1)  
                        niveau.afficher(fenetre) 
                        majtmp=0
                        pygame.display.flip()
                        #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                        creation=1 
                    if creation==1:
                            tempaddi=0 
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)   
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      
                                    victoire=0                
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              
                                    victoire+=niveau.doublon_horizontale(fenetre)  
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    if victoire==4:
                                        meilleurstats("nivb3.txt",kaide,ksaisi,temps,joueur)
                                        choixniv=0
                                        fond3=0                                                                 
                            if choixpartie==1:
                                choixniv=0
                                fond3=0
                            if choixpartie==2:
                                creation=0
                                
                while choixniv==4:
                    if creation==0: 
                        if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsnivb4.txt"):
                            kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsnivb4.txt") 
                            print "tu continues ton ancienne partie"
                        else:
                            temps=0             
                            kaide=1
                            ksaisi=0
                        fenetre.blit(partie,(0,0))
                        niveau=Niveau()
                        niveau.initcharge("nivb4.txt",joueur,kaide,ksaisi)
                        niveau.generer(sb4,joueur,1)  
                        niveau.afficher(fenetre) 
                        majtmp=0
                        pygame.display.flip()
                        #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                        creation=1 
                    if creation==1:
                            tempaddi=0 
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)   
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      
                                    victoire=0                
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              
                                    victoire+=niveau.doublon_horizontale(fenetre)  
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    if victoire==4:
                                        meilleurstats("nivb4.txt",kaide,ksaisi,temps,joueur)
                                        choixniv=0
                                        fond3=0                                                                 
                            if choixpartie==1:
                                choixniv=0
                                fond3=0
                            if choixpartie==2:
                                creation=0
                while choixniv==5:
                    if creation==0: 
                        if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsnivb5.txt"):
                            kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsnivb5.txt") 
                            print "tu continues ton ancienne partie"
                        else:
                            temps=0             
                            kaide=1
                            ksaisi=0
                        fenetre.blit(partie,(0,0))
                        niveau=Niveau()
                        niveau.initcharge("nivb5.txt",joueur,kaide,ksaisi)
                        niveau.generer(sb5,joueur,1)  
                        niveau.afficher(fenetre) 
                        majtmp=0
                        pygame.display.flip()
                        #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                        creation=1 
                    if creation==1:
                            tempaddi=0 
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)   
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      
                                    victoire=0                
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              
                                    victoire+=niveau.doublon_horizontale(fenetre)  
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    if victoire==4:
                                        meilleurstats("nivb5.txt",kaide,ksaisi,temps,joueur)
                                        choixniv=0
                                        fond3=0                                                                 
                            if choixpartie==1:
                                choixniv=0
                                fond3=0
                            if choixpartie==2:
                                creation=0
                while choixniv==6:
                    if creation==0: 
                        if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsnivb6.txt"):
                            kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsnivb6.txt") 
                            print "tu continues ton ancienne partie"
                        else:
                            temps=0             
                            kaide=2
                            ksaisi=0
                        fenetre.blit(partie,(0,0))
                        niveau=Niveau()
                        niveau.initcharge("nivb6.txt",joueur,kaide,ksaisi)
                        niveau.generer(sb6,joueur,1)  
                        niveau.afficher(fenetre) 
                        majtmp=0
                        pygame.display.flip()
                        #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                        creation=1 
                    if creation==1:
                            tempaddi=0 
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)   
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      
                                    victoire=0                
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              
                                    victoire+=niveau.doublon_horizontale(fenetre)  
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    if victoire==4:
                                        meilleurstats("nivb6.txt",kaide,ksaisi,temps,joueur)
                                        choixniv=0
                                        fond3=0                                                                 
                            if choixpartie==1:
                                choixniv=0
                                fond3=0
                            if choixpartie==2:
                                creation=0

                
###########################.......................................................................................................................###########################  
##########################################......................................... MOYEN .........................................##########################################
#########################################################.......................... MOYEN .........................##########################################################         
##########################################################################.........................##########################################################################
#############################################################################################################################################################################
#############################################################################################################################################################################
##########################################################################.........................##########################################################################
#########################################################........................ DIFFICILE .......................##########################################################
##########################################....................................... DIFFICILE .......................................##########################################
###########################.......................................................................................................................###########################  



            while choix3=="difficile":
                if fond3==0:
                    enteteselec(choix3)
                    #print "ixi"
                    #fenetre.blit(difficile,(0,0))
                    #pygame.display.flip()
                    musiquejeu.stop()
                    fond3=1
                choixniv=choixgrille(joueur)
                creation=0 #oui et en haut
                if choixniv==-2:
                    print "bye"
                    choix3=""
                    fond2=0


                while choixniv==1: 
                    if creation==0: 
                        if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsnivc1.txt"):
                            kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsnivc1.txt") 
                            print "tu continues ton ancienne partie"
                        else:
                            temps=0             
                            kaide=1
                            ksaisi=0
                        fenetre.blit(partie,(0,0))
                        niveau=Niveau()
                        niveau.initcharge("nivc1.txt",joueur,kaide,ksaisi)
                        niveau.generer(sc1,joueur,1)  
                        niveau.afficher(fenetre) 
                        majtmp=0
                        pygame.display.flip()
                        #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                        creation=1 
                    if creation==1:
                            tempaddi=0 
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)   
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      
                                    victoire=0                
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              
                                    victoire+=niveau.doublon_horizontale(fenetre)  
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    if victoire==4:
                                        meilleurstats("nivc1.txt",kaide,ksaisi,temps,joueur)
                                        choixniv=0
                                        fond3=0                                                                 
                            if choixpartie==1:
                                choixniv=0
                                fond3=0
                            if choixpartie==2:
                                creation=0
                while choixniv==2:
                    if creation==0: 
                        if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsnivc2.txt"):
                            kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsnivc2.txt") 
                            print "tu continues ton ancienne partie"
                        else:
                            temps=0             
                            kaide=1
                            ksaisi=0
                        fenetre.blit(partie,(0,0))
                        niveau=Niveau()
                        niveau.initcharge("nivc2.txt",joueur,kaide,ksaisi)
                        niveau.generer(sc2,joueur,1)  
                        niveau.afficher(fenetre) 
                        majtmp=0
                        pygame.display.flip()
                        #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                        creation=1 
                    if creation==1:
                            tempaddi=0 
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)   
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      
                                    victoire=0                
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              
                                    victoire+=niveau.doublon_horizontale(fenetre)  
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    if victoire==4:
                                        meilleurstats("nivc2.txt",kaide,ksaisi,temps,joueur)
                                        choixniv=0
                                        fond3=0                                                                 
                            if choixpartie==1:
                                choixniv=0
                                fond3=0
                            if choixpartie==2:
                                creation=0
                while choixniv==3:
                    if creation==0: 
                        if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsnivc3.txt"):
                            kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsnivc3.txt") 
                            print "tu continues ton ancienne partie"
                        else:
                            temps=0             
                            kaide=2
                            ksaisi=0
                        fenetre.blit(partie,(0,0))
                        niveau=Niveau()
                        niveau.initcharge("nivc3.txt",joueur,kaide,ksaisi)
                        niveau.generer(sc3,joueur,1)  
                        niveau.afficher(fenetre) 
                        majtmp=0
                        pygame.display.flip()
                        #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                        creation=1 
                    if creation==1:
                            tempaddi=0 
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)   
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      
                                    victoire=0                
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              
                                    victoire+=niveau.doublon_horizontale(fenetre)  
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    if victoire==4:
                                        meilleurstats("nivc3.txt",kaide,ksaisi,temps,joueur)
                                        choixniv=0
                                        fond3=0                                                                 
                            if choixpartie==1:
                                choixniv=0
                                fond3=0
                            if choixpartie==2:
                                creation=0
                while choixniv==4:
                    if creation==0: 
                        if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsnivc4.txt"):
                            kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsnivc4.txt") 
                            print "tu continues ton ancienne partie"
                        else:
                            temps=0             
                            kaide=2
                            ksaisi=0
                        fenetre.blit(partie,(0,0))
                        niveau=Niveau()
                        niveau.initcharge("nivc4.txt",joueur,kaide,ksaisi)
                        niveau.generer(sc4,joueur,1)  
                        niveau.afficher(fenetre) 
                        majtmp=0
                        pygame.display.flip()
                        #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                        creation=1 
                    if creation==1:
                            tempaddi=0 
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)   
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      
                                    victoire=0                
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              
                                    victoire+=niveau.doublon_horizontale(fenetre)  
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    if victoire==4:
                                        meilleurstats("nivc4.txt",kaide,ksaisi,temps,joueur)
                                        choixniv=0
                                        fond3=0                                                                 
                            if choixpartie==1:
                                choixniv=0
                                fond3=0
                            if choixpartie==2:
                                creation=0
                while choixniv==5:
                    if creation==0: 
                        if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsnivc5.txt"):
                            kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsnivc5.txt") 
                            print "tu continues ton ancienne partie"
                        else:
                            temps=0             
                            kaide=2
                            ksaisi=0
                        fenetre.blit(partie,(0,0))
                        niveau=Niveau()
                        niveau.initcharge("nivc5.txt",joueur,kaide,ksaisi)
                        niveau.generer(sc5,joueur,1)  
                        niveau.afficher(fenetre) 
                        majtmp=0
                        pygame.display.flip()
                        #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                        creation=1 
                    if creation==1:
                            tempaddi=0 
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)   
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      
                                    victoire=0                
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              
                                    victoire+=niveau.doublon_horizontale(fenetre)  
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    if victoire==4:
                                        meilleurstats("nivc5.txt",kaide,ksaisi,temps,joueur)
                                        choixniv=0
                                        fond3=0                                                                 
                            if choixpartie==1:
                                choixniv=0
                                fond3=0
                            if choixpartie==2:
                                creation=0
                while choixniv==6:
                    if creation==0: 
                        if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsnivc6.txt"):
                            kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsnivc6.txt") 
                            print "tu continues ton ancienne partie"
                        else:
                            temps=0             
                            kaide=1
                            ksaisi=0
                        fenetre.blit(partie,(0,0))
                        niveau=Niveau()
                        niveau.initcharge("nivc6.txt",joueur,kaide,ksaisi)
                        niveau.generer(sc6,joueur,1)  
                        niveau.afficher(fenetre) 
                        majtmp=0
                        pygame.display.flip()
                        #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                        creation=1 
                    if creation==1:
                            tempaddi=0 
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)   
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      
                                    victoire=0                
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              
                                    victoire+=niveau.doublon_horizontale(fenetre)  
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    if victoire==4:
                                        meilleurstats("nivc6.txt",kaide,ksaisi,temps,joueur)
                                        choixniv=0
                                        fond3=0                                                                 
                            if choixpartie==1:
                                choixniv=0
                                fond3=0
                            if choixpartie==2:
                                creation=0

###########################.......................................................................................................................###########################  
##########################################....................................... DIFFICILE .........................................########################################
#########################################################........................ DIFFICILE .........................########################################################      
##########################################################################.........................##########################################################################
#############################################################################################################################################################################
#############################################################################################################################################################################
##########################################################################.........................##########################################################################
#########################################################......................... LIBRE .......................#############################################################
##########################################........................................ LIBRE .......................................#############################################
###########################.......................................................................................................................###########################  

            while choix3=="perso":#cette boucle permet de jouer au niveau crée et choisi par le joueur
                
                if creation==0:
                    if os.path.isfile("joueurs"+"//"+joueur+"//"+"statsedition"+str(numniv)+".txt"):
                        kaide,ksaisi,temps=reprendre_stats("joueurs"+"//"+joueur+"//"+"statsedition"+str(numniv)+".txt") #on verifie s'il existe une sauvegarde de la grille du joueur, si c'est le cas on lui charges les stats
                        print "tu continues ton ancienne partie"
                    else:
                        temps=0            
                        kaide=2
                        ksaisi=0
                    fenetre.blit(partie,(0,0))
                    niveau=Niveau()
                    sp=lire_solution("savesolution"+str(numniv)+".txt",joueur)
                    print sp
                    niveau.initcharge("edition"+str(numniv)+".txt",joueur,kaide,ksaisi)
                    niveau.generer(sp,joueur,0)
                    niveau.afficher(fenetre)
                    pygame.display.flip()
                    #musiquejeu.play(loops=-1,maxtime=0,fade_ms=0)
                    creation=1                      
                if creation==1:
                            tempaddi=0 
                            saisi=0
                            (choixpartie,saisi,kaide,ksaisi,tempaddi,majtmp)=niveau.saisir(fenetre,temps)   
                            efface_stats()
                            stats_gochrono(temps)
                            temps+=1
                            stats_aide(kaide)
                            stats_saisi(ksaisi)
                            pygame.display.flip()
                            if majtmp==1:
                                temps=tempaddi
                            if saisi==1:                      
                                    victoire=0                
                                    victoire+=niveau.verif_horizontale()
                                    victoire+=niveau.verif_verticale()              
                                    victoire+=niveau.doublon_horizontale(fenetre)  
                                    victoire+=niveau.doublon_verticale(fenetre)
                                    print victoire
                                    if victoire==4:
                                        choix3=0
                                        fond2=0                                                              
                            if choixpartie==1:
                                choix3=0
                                fond2=0
                            if choixpartie==2:
                                creation=0
                                
                


        while choix2=="editer": #cette boucle permet au joueur de creer une grille
            if creation==0:
                creation=1
                nivedite=Niveau()
                nivedite.initedite(joueur)
                fenetre.blit(editer,(0,0))
                pygame.display.flip()
                while creation==1:
                        creation,kedit=nivedite.saisir_editer(fenetre,kedit)
                        #bsave()
                        #bverif()
                        pygame.display.flip()
                        #if creation==2:
                           # nivedite.recharge()
                        if creation==0:
                                choix2=0
                                fond2=0
                                fond1=0
                                
###########################.......................................................................................................................###########################  
##########################################......................................... LIBRE .........................................##########################################
#########################################################.......................... LIBRE .........................##########################################################    
##########################################################################.........................##########################################################################
#############################################################################################################################################################################
#############################################################################################################################################################################
##########################################################################.........................##########################################################################
#########################################################........................ PRAMAMETRE .......................#########################################################
##########################################....................................... PRAMAMETRE .......................................#########################################
###########################.......................................................................................................................########################### 

        while choix2=="parametre": 
            if fond4==0:
                fenetre.fill((185,122,87))
                #fenetre.blit(menuparam,(0,0))
               # pygame.display.flip()
                fond4=1
            choixparam=fchoixparam(joueur)
            pygame.display.flip()
            fond1=0
            fond5=0
            afftxt=0
            if choixparam==1:
                choix2=""
                fond2=0



            while choixparam=="score":
                if fond5==0:
                    fenetre.fill((185,122,87))
                   
                    fond5=1
                choixscore=fchoixscore(joueur)
                pygame.display.flip()
                affscore=0
                if choixscore==1:
                    choixparam=""
                    fond4=0

                while choixscore=="sc_facile":
                    if affscore==0:
                        #fenetre.fill((185,122,87))
                        entetesc(choixscore)
                        #affichescoref("a")
                       # pygame.display.flip()
                        affscore=1
                    while affscore==1:
                        choixsimple=fsimple(joueur)
                        if choixsimple==1:
                            choixscore=""
                            affscore=0
                            fond5=0

                while choixscore=="sc_moyen":
                    if affscore==0:
                        #fenetre.fill((185,122,87))
                        entetesc(choixscore)
                        #affichescoref("b")
                        #pygame.display.flip()
                        affscore=1
                    while affscore==1:
                        choixsimple=fsimple(joueur)
                        if choixsimple==1:
                            choixscore=""
                            affscore=0
                            fond5=0

                while choixscore=="sc_difficile":
                    if affscore==0:
                       # fenetre.fill((185,122,87))
                        entetesc(choixscore)
                        #affichescoref("c")
                        #pygame.display.flip()
                        affscore=1
                    while affscore==1:
                        choixsimple=fsimple(joueur)
                        if choixsimple==1:
                            choixscore=""
                            affscore=0
                            fond5=0


            while choixparam=="regle":
                if afftxt==0:
                    affregle()
                    afftxt=1
                while afftxt==1:
                    choixsimple=fsimple(joueur)
                    if choixsimple==1:
                        choixparam=""
                        afftxt=0
                        fond4=0

            while choixparam=="credit":
                if afftxt==0:
                    affcredit()
                    afftxt=1
                while afftxt==1:
                    choixsimple=fsimple(joueur)
                    if choixsimple==1:
                        choixparam=""
                        afftxt=0
                        fond4=0
                    
                            

                   
                                            
                                            


            
            
            
            
                                
