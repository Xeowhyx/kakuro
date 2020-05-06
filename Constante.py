#! /usr/bin/env python
# -*- coding: utf-8 -*-




import pygame
import pygame.mixer
from pygame.locals import*

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







#############################################################################################################################
                                                    #constante
#############################################################################################################################



pygame.init()

#chargement des polices d'ecritures
font = pygame.font.Font(None, 20) #petit en sc
font1=pygame.font.Font(None,28)
font2 = pygame.font.Font(None, 35) #bleu acceuill

titre=pygame.font.Font(None,50) #titre selec niv
fontedite=pygame.font.Font(None,15) #ce qui est mis par defaut dans rect, grille, user ...
titrespe=pygame.font.Font('img/PWPerspective.ttf',25)
fontregle=pygame.font.Font('img/Black Carrot.ttf',12)
fontregle2=pygame.font.Font('img/Black Carrot.ttf',20)#20
fontmenu=pygame.font.Font('img/MEEGOREN.ttf',30)


#chargement des sons
pygame.mixer.init()
musiquejeu = pygame.mixer.Sound("img/Tigra.wav")


img_partie="img/partie.png"
img_partie_editer="img/partie_editer.png"
img_facile="img/facile.png"
img_moyen="img/moyen.png"
img_difficile="img/difficile.png"
img_descartes="img/descartes.png"

#variable constante
cote_fenetrex=900-154-30
cote_fenetrey=500
taille_sprite=50
grillex=464-154-30
grilley=64
pgrillex=63 #pos des (petitee) grilles dans selection niv
pgrilley=96
pgrilleyy=310 #pos de la 2eme ligne en y
taille_pgrille=154 #taille (petite) grilles dans selection niv (carre)

#autre
img_case_noir="img/case_noir.png"
img_inf_noir="img/inf_noir.png"
img_sup_noir="img/sup_noir.png"
img_case_somme="img/case_somme.png"
img_case_blanc="img/case_blanc.png"
img_focus="img/focus.png"
img_saisie_blocn="img/saisie_blocn.png" 
img_saisie_bloc="img/saisie_bloc.png"


#nombre somme
##taille 12 gras
img_nbr_inf1_0="img/inf1_0.png"
img_nbr_inf1_1="img/inf1_1.png"
img_nbr_inf1_2="img/inf1_2.png"
img_nbr_inf1_3="img/inf1_3.png"
img_nbr_inf1_4="img/inf1_4.png"
img_nbr_inf1_5="img/inf1_5.png"
img_nbr_inf1_6="img/inf1_6.png"
img_nbr_inf1_7="img/inf1_7.png"
img_nbr_inf1_8="img/inf1_8.png"
img_nbr_inf1_9="img/inf1_9.png"

img_nbr_inf2_1="img/inf2_1.png"
img_nbr_inf2_2="img/inf2_2.png"
img_nbr_inf2_3="img/inf2_3.png"

img_nbr_sup1_0="img/sup1_0.png"
img_nbr_sup1_1="img/sup1_1.png"
img_nbr_sup1_2="img/sup1_2.png"
img_nbr_sup1_3="img/sup1_3.png"
img_nbr_sup1_4="img/sup1_4.png"
img_nbr_sup1_5="img/sup1_5.png"
img_nbr_sup1_6="img/sup1_6.png"
img_nbr_sup1_7="img/sup1_7.png"
img_nbr_sup1_8="img/sup1_8.png"
img_nbr_sup1_9="img/sup1_9.png"


img_nbr_sup2_1="img/sup2_1.png"
img_nbr_sup2_2="img/sup2_2.png"
img_nbr_sup2_3="img/sup2_3.png"

#nombre modifiable
#taille 20 pas gras

img_nbr_1="img/nbr_1.png"
img_nbr_2="img/nbr_2.png"
img_nbr_3="img/nbr_3.png"
img_nbr_4="img/nbr_4.png"
img_nbr_5="img/nbr_5.png"
img_nbr_6="img/nbr_6.png"
img_nbr_7="img/nbr_7.png"
img_nbr_8="img/nbr_8.png"
img_nbr_9="img/nbr_9.png"

#nombre modifiable apres aide
#taille 20 pas gras rouge
img_nbr_r1="img/nbr_r1.png"
img_nbr_r2="img/nbr_r2.png"
img_nbr_r3="img/nbr_r3.png"
img_nbr_r4="img/nbr_r4.png"
img_nbr_r5="img/nbr_r5.png"
img_nbr_r6="img/nbr_r6.png"
img_nbr_r7="img/nbr_r7.png"
img_nbr_r8="img/nbr_r8.png"
img_nbr_r9="img/nbr_r9.png"


#nombre faux si doublons
img_nbr_f1="img/nbr_f1.png"
img_nbr_f2="img/nbr_f2.png"
img_nbr_f3="img/nbr_f3.png"
img_nbr_f4="img/nbr_f4.png"
img_nbr_f5="img/nbr_f5.png"
img_nbr_f6="img/nbr_f6.png"
img_nbr_f7="img/nbr_f7.png"
img_nbr_f8="img/nbr_f8.png"
img_nbr_f9="img/nbr_f9.png"







#############################################################################################################################
                                                    #chargement des images
#############################################################################################################################

#icone = pygame.image.load(image_icone)

#joueur=pygame.image.load(img_joueur).convert()

#RESIZABLE FULLSCREEN
#fenetre=pygame.display.set_mode((cote_fenetrex,cote_fenetrey), RESIZABLE)
fenetre=pygame.display.set_mode((cote_fenetrex,cote_fenetrey))


ecran=pygame.Surface(fenetre.get_size())


pygame.display.set_caption("Kakuro")
#icone = pygame.image.load(image_icone).convert() 



logo_kakuro=pygame.image.load("img/logo.png")
pygame.display.set_icon(logo_kakuro)


#menu_joueur=pygame.image.load(img_joueur)
#menu1=pygame.image.load(img_menu1)
#menu2=pygame.image.load(img_menu2)
#menuparam=pygame.image.load(img_menuparam)
partie=pygame.image.load(img_partie)
editer=pygame.image.load(img_partie_editer)
facile=pygame.image.load(img_facile)
moyen=pygame.image.load(img_moyen)
difficile=pygame.image.load(img_difficile)
descartes=pygame.image.load(img_descartes)



case_noir=pygame.image.load(img_case_noir)
inf_noir=pygame.image.load(img_inf_noir)
sup_noir=pygame.image.load(img_sup_noir)
case_somme=pygame.image.load(img_case_somme)
case_blanc=pygame.image.load(img_case_blanc)
focus=pygame.image.load(img_focus)
saisie_blocn=pygame.image.load(img_saisie_blocn)
saisie_bloc=pygame.image.load(img_saisie_bloc)

inf1_0=pygame.image.load(img_nbr_inf1_0)
inf1_1=pygame.image.load(img_nbr_inf1_1)
inf1_2=pygame.image.load(img_nbr_inf1_2)
inf1_3=pygame.image.load(img_nbr_inf1_3)
inf1_4=pygame.image.load(img_nbr_inf1_4)
inf1_5=pygame.image.load(img_nbr_inf1_5)
inf1_6=pygame.image.load(img_nbr_inf1_6)
inf1_7=pygame.image.load(img_nbr_inf1_7)
inf1_8=pygame.image.load(img_nbr_inf1_8)
inf1_9=pygame.image.load(img_nbr_inf1_9)

inf2_1=pygame.image.load(img_nbr_inf2_1)
inf2_2=pygame.image.load(img_nbr_inf2_2)
inf2_3=pygame.image.load(img_nbr_inf2_3)

sup1_0=pygame.image.load(img_nbr_sup1_0)
sup1_1=pygame.image.load(img_nbr_sup1_1)
sup1_2=pygame.image.load(img_nbr_sup1_2)
sup1_3=pygame.image.load(img_nbr_sup1_3)
sup1_4=pygame.image.load(img_nbr_sup1_4)
sup1_5=pygame.image.load(img_nbr_sup1_5)
sup1_6=pygame.image.load(img_nbr_sup1_6)
sup1_7=pygame.image.load(img_nbr_sup1_7)
sup1_8=pygame.image.load(img_nbr_sup1_8)
sup1_9=pygame.image.load(img_nbr_sup1_9)

sup2_1=pygame.image.load(img_nbr_sup2_1)
sup2_2=pygame.image.load(img_nbr_sup2_2)
sup2_3=pygame.image.load(img_nbr_sup2_3)



nbr_1=pygame.image.load(img_nbr_1)
nbr_2=pygame.image.load(img_nbr_2)
nbr_3=pygame.image.load(img_nbr_3)
nbr_4=pygame.image.load(img_nbr_4)
nbr_5=pygame.image.load(img_nbr_5)
nbr_6=pygame.image.load(img_nbr_6)
nbr_7=pygame.image.load(img_nbr_7)
nbr_8=pygame.image.load(img_nbr_8)
nbr_9=pygame.image.load(img_nbr_9)

nbr_r1=pygame.image.load(img_nbr_r1)
nbr_r2=pygame.image.load(img_nbr_r2)
nbr_r3=pygame.image.load(img_nbr_r3)
nbr_r4=pygame.image.load(img_nbr_r4)
nbr_r5=pygame.image.load(img_nbr_r5)
nbr_r6=pygame.image.load(img_nbr_r6)
nbr_r7=pygame.image.load(img_nbr_r7)
nbr_r8=pygame.image.load(img_nbr_r8)
nbr_r9=pygame.image.load(img_nbr_r9)

nbr_f1=pygame.image.load(img_nbr_f1)
nbr_f2=pygame.image.load(img_nbr_f2)
nbr_f3=pygame.image.load(img_nbr_f3)
nbr_f4=pygame.image.load(img_nbr_f4)
nbr_f5=pygame.image.load(img_nbr_f5)
nbr_f6=pygame.image.load(img_nbr_f6)
nbr_f7=pygame.image.load(img_nbr_f7)
nbr_f8=pygame.image.load(img_nbr_f8)
nbr_f9=pygame.image.load(img_nbr_f9)


#on mets images dans tableau pour pas faire 10 condition if a la main au moment des afficahges
#ces tableaux serront utilisé pour differentes utilisatons differentes
inf1=[inf1_0,inf1_1,inf1_2,inf1_3,inf1_4,inf1_5,inf1_6,inf1_7,inf1_8,inf1_9]
sup1=[sup1_0,sup1_1,sup1_2,sup1_3,sup1_4,sup1_5,sup1_6,sup1_7,sup1_8,sup1_9]
chiffre=['0','1','2','3','4','5','6','7','8','9'] #unite
chiffred=['1','2','3']#dizaine

nbrmodif=[nbr_1,nbr_2,nbr_3,nbr_4,nbr_5,nbr_6,nbr_7,nbr_8,nbr_9]




