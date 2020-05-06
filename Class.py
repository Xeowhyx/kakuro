#! /usr/bin/env python
# -*- coding: utf-8 -*-


from Constante import*
from Fonction import*
from random import*


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
                                                    #classe
#############################################################################################################################



class Niveau:
        def __init__(self):
            self.structure = 0 #grille brute
            self.long_brute = 0 #nbr de caractere par ligne du txt
            self.grillemodifiable=0 # pour savoir si la case est modifiable
            self.noirsup=0  #[[noir_sup,x,y],[noir_sup2,x2,y2],...] x->col y->ligne
            self.noirinf=0 
            self.solutiontot=0 #contient uniquement tout les nbr modifiable solution dans ordre

            self.joueur=0
            self.nsolution=0 #nbr de fois que le gars clic sur solution en partie edite au cas ou

#caracteristique utile seulement pour mode editer:
            
            self.bloc=0 #contient le dernier type de bloc clic en mode edition
            self.blocn=0 #contient le dernier type de bloc chiffre en mode jeu classique
            self.structuredite=0
            self.structuredite2=0
           
            
#stats:
            self.kaide=0
            self.ksaisi=0
#carac des etats des boutons:
            self.curseursave=1  #1:exterieur  #0:interieur
            self.curseursolu=1
            


        def initedite(self,joueur):
            """
            initiatilisation du mode editer, le programme genere une grille vierge de taille 7x7 
            remplie uniquement de case modifiable vide
            --------------------------------------
            joueur:(string) le nom du joueur
            """
            self.joueur=joueur
            self.structuredite=[]
            for col in range (0,7):
                tmp=[]
                for ligne in range(0,7): #0a6
                    tmp.append('_')
                    if ligne==6:
                        self.structuredite.append(tmp)
                        
            print(self.structuredite)




        def initcharge(self,fichier,joueur,kaide,ksaisi):
            """
            initialisation des parametres associer a la classe
            ----------------------------------------------------
            fichier:(string) le nom du fichier txt
            joueur:(string) le nom du joueur
            kaide:(int) le nombre d'aide maximum autorisé
            ksaisi:(int) le nombre de saisi totale
            """
            self.joueur=joueur
            self.kaide=kaide
            self.fichier=fichier
            self.ksaisi=ksaisi
           


    




        def save_stats(self,tempp):#sauvegarde du nbr aide restant, coup utilise, temps utilise d'une partie qui n'est termine, pour que le joueur puisse reprendre sa grille et ces stats là ou il s'etait arrete
            """
            sauvegarde les stats de la grille en cour, pour pouvoir recupérer les stats lorsque le joueur veut reprendre la meme grille
            ------------------------------------------------
            tempp:(int) le temps ecoulé en secondes*60
            """
            fichier=open("joueurs"+"//"+self.joueur+"//"+"stats"+self.fichier,'w')
            fichier.write(str(self.kaide)+"\n"+str(self.ksaisi)+"\n"+str(tempp))
            fichier.close()
            
                                            
        
        def save_grille(self):
            """
            sauvegarde l'etat d'avancement de la grille en cour, pour pouvoir la recupérer quand le joueur veut reprendre la partie
            """
            print"avant_save structure"
            print self.structure
            dbtligne=0
            dbtcol=0
            for ligne in range(0,7):#0a6
                for col in range(0,len(self.structure[ligne])):
                    #if self.structure[ligne][col]=='_':
                    if self.structure[ligne][col]=='_' or self.structure[ligne][col]=='a'or self.structure[ligne][col]=='b'or self.structure[ligne][col]=='c'or self.structure[ligne][col]=='d'or self.structure[ligne][col]=='e'or self.structure[ligne][col]=='f'or self.structure[ligne][col]=='g'or self.structure[ligne][col]=='h'or self.structure[ligne][col]=='i':
                        tmpligne,tmpcol,self.structure[ligne][col]=recherche(dbtligne,dbtcol,self.grillemodifiable)
                        dbtligne=tmpligne
                        dbtcol=tmpcol
#("joueurs"+"//"+self.joueur+"//"+nom,'
 #nom="edition"+str(pnum)+".txt"#+1 a la save
           
            fichier=open("joueurs"+"//"+self.joueur+"//"+self.fichier,'w')
            ligne=""
            for element in self.structure:
                for sselement in element:
                    ligne=ligne+sselement
                fichier.write(ligne+"\n")
                ligne=""
                                
            fichier.close()
       
            
            
            
                
            

        def save(self):#save edite
            """
            enregistre sur un fichier associé au joueur la partie du joueur qu'il viens de creer en mode editon
            ------------------------------------------------------------
            Remarque:
            a cause de convertion la self.structuredite a etait modifié, elle reprend sont ancienne valeur qui
            a etait conservé dans un fichier .txt (si nous n'avons fait uniquement une copie de la variable et convertie la copie, a cause
            des adresses, nous auront perdu l'information contenu dans la variable original, donc le passage en .txt etait une possibilité pour recupérer l'information
            """
            
            fnum=open("joueurs"+"//"+self.joueur+"//"+'num.txt','r')#on lis a quel save on est
            num=0
            for element in fnum:
                num=num+int(element)
            pnum=num+1
            fnum.close()
                
            fnum=open("joueurs/"+"//"+self.joueur+"//"+'num.txt','w')
            fnum.write(str(pnum))
            fnum.close()
                
            nom="edition"+str(pnum)+".txt"#+1 a la save
                
                


                ##################################################################################################################
                #
                #
            with open("img/tmp.txt",'r') as fichier: #txt en chaine
                structure=[]
                for ligne in fichier:
                    ligne_structure=[]
                    for sprite in ligne:
                        if sprite!='\n':
                            ligne_structure.append(sprite)
                    structure.append(ligne_structure)

            print "structureAV"
            print structure
            print "structureAV"
                
            chaine="" #chaine en pseudo brute
            for ligne in range(0,7):
                for col in range(0,7):
                    if structure[ligne][col]=='(':
                        chaine='('
                        del structure[ligne][col]
                        while  structure[ligne][col] != ')':
                                #col+=1
                                #print structure[ligne][col]
                            chaine=chaine+structure[ligne][col]
                            del structure[ligne][col]
                        chaine=chaine+')'
                        structure[ligne][col]=chaine
                            
            print "structure"
            print structure
            print "structure"
            print "self.structure"
            print self.structuredite
            print "self.structure"
            #self.structuredite=structure
            self.structuredite=structure
            print '\n'*3
            print "structure"
            print structure
            print "structure"
            print "self.structure"
            print self.structuredite
            print "self.structure"
                #
                #
                ##################################################################################################################     
        
                
                #fichier=open("ici"+"//"+nom,'w')#save sur ici
                ##fichier=open(self.joueur+"//"+nom,'w')
            fichier=open("joueurs"+"//"+self.joueur+"//"+nom,'w')
                #fichier=open("/img/"+nom,'w')
                
            ligne=""
            for element in self.structuredite:
                    for sselement in element:
                            ligne=ligne+sselement
                    fichier.write(ligne+"\n")
                    ligne=""
                        
            fichier.close()
            txtedite(pnum)
           # print "tu as save ta partie: ",pnum
            #print "dans le menu de selection difficulte appuye ' e ' et mets '",pnum,"' pour y jouer"
                           
                        
                
          
                



#joueur represente le dossier d'acces au joueur
        def generer(self,solution,joueur,normal): #si normal est 1 alors on charge un niveau normal sinon on charge un niveau editer et on doit donc changer le chemin acces du fichier a generer
                """
                lis un fichier txt qui correspondra au niveau chargé
                remplie le tableau self.structure de caractere contenu dans le fichier .txt
                chaque ligne du fichier (de longueur pas forcement identique) constitue un sous-tableau de self.structure
                --------------------------------------------------------
                ENTRE:
                solution:(tableau int)contient les solutions de la grilles (nbr modifiable) dans l'ordre de lecture classique
                joueur:(string)le nom du joueur
                normal:(boolean) si 1: on charge une partie en mode classique, si 0 on charge une partie en mode edition
                ---------------------------------------------------------
                Remarque:
                _le parametre normal permet de savoir quel fichier le programme va lire, car le chemin d'acces est differents des
                _le fichier .txt est constituté de forcement 7ligne et d'au moins 7caracteres par ligne
                _self.structure contient TOUTES les informations d'une grille
                """

            
                if normal==1:                     
                        joueur="joueurs"+"//"+self.joueur+"//"
                else:
                        joueur="joueurs"+"//"+joueur+"//"
                        
                        
                k=0
                self.long_brute=[]
                with open(joueur+self.fichier, "r") as fichier: #pas besoin de fermer le fichier avec 'with', python le fait automatiquement
                        structure_niveau = []
                        for ligne in fichier:
                                ligne_niveau = []
                                for sprite in ligne:
                                        if sprite != '\n':
                                                ligne_niveau.append(sprite)
                                                k+=1
                                self.long_brute.append(k)
                                k=0
                                structure_niveau.append(ligne_niveau)
                        self.structure = structure_niveau
                self.solutiontot=solution
                print(self.structure)
                        
                       
                        
                        

        def afficher(self,fenetre):
            """
            lis self.structure et faits les affichages sur la grille selon un codage definis.
            le programme associe un caractere de self.structure a une image(.png) a une position dans la grille (cas simple):
                ex: '_' -> case modifiable vide
                    'x' -> case obstacle
                    'a' -> case modifiable valeur 1
                    'b' -> case modifiable valeur 2
                    ...
                    'i' -> case modifiable valeur 9
                    
            /!\ mais il n'existe pas assez de caractere pour faire toutes les combinaisons, donc les caracteres situté entre '(' et ')' code uniquement
            pour une case dans la grille
                exemple d'une sequence dans self.structure:
                ex: '(','1','3','2','7',')' -> 13/27
                donc affiche la case somme 13/27 dans la meme case de la grille
                dans ce cas special, la case de la grille est composé de 4images superposé avec un jeu de transparence, car il faut 4 chiffres pour afficher 13/27
                donc le programme affichera une image pour le chffre des unités du nombre inferieur (1)
                                          une image pour le chffre des dizaines du nombre inferieur (3)
                                            une image pour le chffre des unités du nombre superieur (2)
                                         une image pour le chffre des dizaines du nombre superieur (7)
                le jeu permettant de faire des sommes de 1a39 nous avons donc les images necessaire des cases somme inferieur et superieur,
                avec le chiffre des unités variant de 0a9 et celui des dizaine qui vaut 1,2,3 ou rien

            le caractere 'z' permet de faire la distinction du caractere '0', en effet '0' affiche 0 sur la grille alors que 'z' n'affiche rien (vide)
            cela permet de differencié l'affichage de 08 et 8 par exemple

            

            lorsqu'on parcour self.strucutre on en profite pour créer d'autre tableau qui nous serviront a la suite du prgrm
            _self.noirsup
            _self.noirinf
            _self.grillemodifiable

            self.noirsup:(tableau int) contient plusieurs sous-tableau, avec pour chaque sous-tableau 3 valeurs (int).
                ex: [[n,x,y],[n2,x2,y2],[n3,x3,y3]]
                qui se traduit par: "il y a une case somme superieur qui a pour valeur n et elle se situe a la x eme colonne et y eme ligne,
                                    il y a une case somme superieur qui a pour valeur n1 et elle se situe a la x2 eme colonne et y2 eme ligne,
                                    il y a une case somme superieur qui a pour valeur n2 et elle se situe a la x2 eme colonne et y2 eme ligne"
                                    Remarque: la 1er cases se situe en x=0 et y=0

            self.noirunf:(tableau int) meme chose mais cette fois pour les cases sommes inferieurs


            self.grillemodifiable:(tableau int et caractere) est de taille 7x7 quelque soit la grille, il est composé de 7sous-tableau representant les lignes de la grille
                                    et chaque ligne constitué de 7elements qui corresponde aux 7 colonnes de la grille
                ex:[['x', 'x', 'x', 'x', 'x', 'x', 'x'],
                    ['x', 0, 1, 'x', 'x', 'x', 'x'],
                    ['x', 3, 9, 'x', 'x', 'x', 'x'],
                    ...]

                    0->case modifiable vide
                    1->case modifiable valeur 1
                    ...
                    9->case modifiable valeur 9
                    'x'->case non modifiable (elle peut etre une case sommes ou obtacle)
                cette grille permet de simplifier les calculs et la visualisation de la grille car 1 element correspond a une case de la grille


            AFFICHAGE A SAVOIR:
            la grille a une dimension de 358px*358px
            l'image(ou la composé d'image) que l'on affiche dans une case a pour dimension 50px*50px
            entre chaque image (horizontalement et verticalement) il y a 1px d'espace
            d'ou 358=50*7+8
            et d'ou le decalage du curseur a chaque img, cet espace est complété par le fond d'ecran qui donne l'impression d'une grille
            ----------------------------------------------------------------------------------------------------------------
            ENTRE:
            fenetre:(viens de pygame definis dans CONSTANTE.py)
                    necessaire pour pouvoir faire des collages d'image dans cette fonction
            ----------------------------------------------------------------------------------------------------------------
            SORTIE:
            self.grillemodifiable: deja detaillé
            """
            num_ligne=0
            decalx=1
            decaly=1
            chaine=[]
            ligne=0
            k=-1
            decompteur=0
            bloquer=0

           


            self.noirsup=[]
            self.noirinf=[]
            tmp_noir=[]
            ## num_col=-1 #pour l extraction
            

            self.grillemodifiable=[]

            while k<6: #6
                    k+=1
                    i=0
                    num_case=0 #pour affichage nbr somme/modifiable
                    ligne_tmp=[]
                
                  
                    for i in range (0,self.long_brute[k]):        #(num_case !=i  ##num_ligne==k)
                                


                                # num_col+=1
                                x = ((num_case) * taille_sprite)+grillex+decalx #plus op de bloque lorsqu'il y a nbr somme pdt 6t
                                y = (num_ligne * taille_sprite)+grilley+decaly
                           
                                if (self.structure[k][i])=='(': #affichage nbr inf, compose de 2 images
                                        
                                        
                                        
                                        kk=1
                                        nbr_noir_inf=[]
                                        ligne_tmp.append('x')
                                        while   kk+i<=self.long_brute[k] and (self.structure[k][i+kk])!=',': #(ordre condition and important)
                                                nbr_noir_inf.append(self.structure[k][i+kk])                #la 1er condition permet de ne pas faire planter le programme si on oublie une virgule dans le fichier txt
                                                kk+=1                                                       #ajoute les 2 caracteres compris entre '(' et ',' dans un tableau
                                       
                                        tmp_noir=[]
                                        tmp_noir.append(char_nbr(nbr_noir_inf))
                                        tmp_noir.append(num_case) # le mettre ici car si apres tour x3
                                        tmp_noir.append(k)

                                        
                                        if tmp_noir[0]!=0: #AJOUT: sinon quelque bug lors des comptages de ligne/colonnes (cas particuliers remarqué)
                                                self.noirinf.append(tmp_noir)
                                                                                
                                        if nbr_noir_inf[0]=='1': 
                                                fenetre.blit(inf2_1,(x,y)) 
                                        if nbr_noir_inf[0]=='2':
                                                fenetre.blit(inf2_2,(x,y))
                                        if nbr_noir_inf[0]=='3':
                                                fenetre.blit(inf2_3,(x,y))

                                        if nbr_noir_inf[0]=='z' and nbr_noir_inf[1]=='z':
                                                fenetre.blit(inf_noir,(x,y))
                                                
                                        p=-1
                                        while p<9:
                                                p+=1
                                                if nbr_noir_inf[1]==chiffre[p]:
                                                        fenetre.blit(inf1[p],(x,y))  #meme chose qu'en bas(en commentaire) mais en + propre
                                                        p+=9
                                                        
                        

                                     
                                                
                                elif (self.structure[k][i])==',': #affichage nbr sup, compose de 2 images
                                        x=x-3*(taille_sprite+1)
                                        kk=1
                                        nbr_noir_sup=[]
                                        while  kk+i<=self.long_brute[k] and (self.structure[k][i+kk])!=')': #(ordre condition and important)                                                           
                                                nbr_noir_sup.append(self.structure[k][i+kk])                #la 1er condition permet de ne pas faire planter le programme si on oublie une virgule dans le fichier txt 
                                                kk+=1                                                       #ajoute les 2 caracteres compris entre ',' et ')' dans un tableau


                                        tmp_noir=[]
                                        tmp_noir.append(char_nbr(nbr_noir_sup))
                                        tmp_noir.append(num_case-3) # le mettre ici car si apres tour x3
                                        tmp_noir.append(k)
                                        
                                        if tmp_noir[0]!=0: #AJOUT: sinon quelque bug lors des comptages de ligne/colonnes (cas particuliers remarqué)
                                                self.noirsup.append(tmp_noir)
                                        
                        
                                        
                                        if nbr_noir_sup[0]=='1': #superpositon d'image transparent(4au max)
                                                fenetre.blit(sup2_1,(x,y)) #un nombre allant de 1a39 est composé d'un chiffre variant de 0a9 et un autre de 1a3 s'il y en as
                                        if nbr_noir_sup[0]=='2':
                                                fenetre.blit(sup2_2,(x,y))#fleme dee boucler
                                        if nbr_noir_sup[0]=='3':
                                                fenetre.blit(sup2_3,(x,y))


                                        if nbr_noir_sup[0]=='z' and nbr_noir_sup[1]=='z':
                                                fenetre.blit(sup_noir,(x,y))



                                        p=-1
                                        while p<9:
                                                p+=1
                                                if nbr_noir_sup[1]==chiffre[p]:
                                                        fenetre.blit(sup1[p],(x,y))  #meme chose qu'en bas mais en + propre
                                                        p+=9
                                                
                                        
                                        num_case=num_case-6
                                        decalx-=6   #on fait un decalage de 2*3 a gauche a cause des 7 caractere compris dans la parenthese qui ne code que pour 1 case, il y a donc 6caractere en trop
                                                    #--> recule le curseur car on a pas bloque l'incrementation de x pdt 6t




                                elif (self.structure[k][i])=='x': #afficahge mur          
                                        fenetre.blit(case_noir,(x,y))
                                        ligne_tmp.append('x')

                                       
                                        
                                               
                                elif (self.structure[k][i])=='a':  #affichage des nombres modifiable, on utilise les lettres pour evite les interferences avec les nbr dans parenthese
                                        ligne_tmp.append(1)
                                        
                                        fenetre.blit(nbr_1,(x,y))
                                elif (self.structure[k][i])=='b':
                                        ligne_tmp.append(2)
                                        fenetre.blit(nbr_2,(x,y))
                                elif (self.structure[k][i])=='c':
                                        ligne_tmp.append(3)
                                        fenetre.blit(nbr_3,(x,y))
                                elif (self.structure[k][i])=='d':
                                        ligne_tmp.append(4)
                                        fenetre.blit(nbr_4,(x,y))
                                elif (self.structure[k][i])=='e':
                                        ligne_tmp.append(5)
                                        fenetre.blit(nbr_5,(x,y))
                                elif (self.structure[k][i])=='f':
                                        ligne_tmp.append(6)
                                        fenetre.blit(nbr_6,(x,y))
                                elif (self.structure[k][i])=='g':
                                        ligne_tmp.append(7)
                                        fenetre.blit(nbr_7,(x,y))
                                elif (self.structure[k][i])=='h':
                                        ligne_tmp.append(8)
                                        fenetre.blit(nbr_8,(x,y))
                                elif (self.structure[k][i])=='i':
                                        ligne_tmp.append(9)
                                        fenetre.blit(nbr_9,(x,y))
                                        



                                 #pas encore utilisé
                                        
##                                elif (self.structure[k][i])=='A':  #affichage des nombres modifiable reponse, on utilise les lettres pour evite les interferences avec les nbr dans parenthese
##                                        fenetre.blit(nbr_r1,(x,y))
##                                elif (self.structure[k][i])=='B':          
##                                        fenetre.blit(nbr_r2,(x,y))
##                                elif (self.structure[k][i])=='C': 
##                                        fenetre.blit(nbr_r3,(x,y))
##                                elif (self.structure[k][i])=='D':          
##                                        fenetre.blit(nbr_r4,(x,y))
##                                elif (self.structure[k][i])=='E':          
##                                        fenetre.blit(nbr_r5,(x,y))
##                                elif (self.structure[k][i])=='F':          
##                                        fenetre.blit(nbr_r6,(x,y))
##                                elif (self.structure[k][i])=='G':          
##                                        fenetre.blit(nbr_r7,(x,y))
##                                elif (self.structure[k][i])=='H':          
##                                        fenetre.blit(nbr_r8,(x,y))
##                                elif (self.structure[k][i])=='I':          
##                                        fenetre.blit(nbr_r9,(x,y))


                                elif (self.structure[k][i]=='_'):
                                        ligne_tmp.append(0)
                                        


                                
                                num_case+=1
                                decalx+=1 #on espace chaque image horizontale pour l'esthetique, en effet elle serra completer par les traits du grillage en arriere plan (de largeur 1 pixel)

                    self.grillemodifiable.append(ligne_tmp)
                        

        
                    num_ligne+=1
                    decaly+=1 #on espace aussi les images verticales
                    decalx=1
                    num_col=-1 #pour l extraction
            

            return self.grillemodifiable
                


        def solution_utile(self): #seulement si k_h
            """
            compare les nombre modifiable (obtenu dans self.grillemodifiable) qui correspondent avec les solutions contenu dans self.solutiontot
            Si se sont les memes nombre alors le nombre modifiable est correcte
            Sinon le nombre mis n'est pas correcte et ont l'ajoute dans res avec sa position x et y           
            ---------------------------------------------------------
            SORTIE:
            res:(tableau int) constitué de sous-tableau de taille 3
                ex:[[nbr,x,y][nbr2,x2,y2][nbr3,x3,y3]...]
            """
            res=[]
            rang=-1
            tmp=[]
            num_ligne=0
            decaly=1
            for ligne in range (0,7):
                num_case=0
                decalx=1
                for col in range (0,7):
                    x = ((num_case) * taille_sprite)+grillex+decalx 
                    y = (num_ligne * taille_sprite)+grilley+decaly            
                    if self.grillemodifiable[ligne][col]=='x':
                        pass                            
                    else:
                        rang+=1
                        if self.grillemodifiable[ligne][col]!=self.solutiontot[rang]:
                            tmp.append(self.solutiontot[rang])
                            tmp.append(col) 
                            tmp.append(ligne) #[[nbr1,x,y][nbr2,x,y][nbr3,x,y]...] x,y->ordonn dans la grille
                            res.append(tmp)  
                            tmp=[] 
                                                
                                        
                                    
                    num_case+=1
                    decalx+=1
                num_ligne+=1
                decaly+=1
                                
            return res 
                
                



#self.grillemodifiable
        
#1:exterieur  #0:interieur
        
        def saisir(self,fenetre,tempp):
                """
                gestion de toutes les interractions possible du joueur par clavier/souris pendant une partie classique
                ---------------------------------------------------------------------------------------------------------------
                ENTRE:
                fenetre:(viens de pygame definis dans CONSTANTE.py)
                        necessaire pour pouvoir faire des collages d'image dans cette fonction
                tempp:(int)contient le nombre de temps de jeu totale en seconde fois 60 a partir du moment où il a etait lancé
                ----------------------------------------------------------------------------------------------------------------
                REMARQUE:
                le tempp est envoyé ici car dans certaine situation il serra augmenté, comme par exemple pendant le saisie au clavier (correcte ou incorrecte)
                on reinitialisera un deuxieme chronometre qui commencera au tempp de celui-ci
                ----------------------------------------------------------------------------------------------------------------
                SORTIE:
                de type: "action"(int) boolean(int 0 ou int 1) self.aide(int) self.saisi(int) "temp"(int) boolean2

                "action": permet au joueur de gerer la navigation pendant le jeu
                        1->le jeu ira au menu precdent
                        2->reinitialisation de la partie jusqu'a la derniere sauvegarde(quitte et remets le jeu, sans avoir d'effet flash sur ecran)
                        0->rien est fait

                "boolean": permet de savoir si la grille a etait modifié
                        0->grille non modifier
                        1->grille modifier
                        cette sortie permet de savoir si le programme doit lancé les fonctions qui permette par exemple de compter chaque ligne/colonne de grille,
                        ou par exemple si le jeu doit mettre a jour l'affichage de la grille.
                        (il n'est pas necessaire de lancé des calculs, ou mettre a jour l'affichage de la grille si elle meme n'a pas etait modifié)

                self.aide: le nombre d'aide totale qui reste, il est decrementer a chaque aide utilisé

                self.saisi: le nombre totale de saisi (nombre de coup) se fait incrementer a chaque saisie et utilisation d'aide

                "temp": renvoit un temps.
                        tempp->renvoit le temps au moment ou la fonction a etait appelé
                        tempaddi-> renvoit un autre temps, qui correspond au temps du moment ou la fonction a etait appelé plus la duré de la saisie, donc tempp>tempaddi
                        0-> reinitialise le temps

                "boolean2": renvoit int 0 ou int 1
                        0->le temps ne serra pas mis a jour
                        1->le temps serra maj
                        il permet de mettre a jour le temps meme lorsque la grille n'a pas etait modifier mais a eu une saisie
                        ex: lorsque le joueur saisie une chaine de caractere au lieu d'un nombre dans la grille, il utilise le tempaddi mais ne modifier pas la grille car le programme refuse la chaine de caractere,
                                il faut donc augmenter la valeur du temps.
                        ---> c'est le seul moment où on mets a jour le temps sans que l'on modifie la grille
              """
                
                (sx,sy)=pygame.mouse.get_pos()
                if sx>34 and sx<190 and sy>406 and sy<437: #and sx<251
                    
                    if self.curseursolu==1:    
                        efface_verif()    #car la position du texte de 'solution' est contenu dans 'verification'                  
                    bsolucolor()
                    self.curseursolu=0
                else:
                    if self.curseursolu==0:
                        efface_verif()
                    bsolu()
                    self.curseursolu=1

                    
                if sx>34 and sx<261 and sy>356 and sy<388: #pos exacte du rectangle cree pour le clic 'sauvegarder' dans efface_save
                        if self.curseursave==1: #permet d'effacer la surface qu'une lorsque que le curseur est dans la zone de clic alors qu'avant il etait a l'exterieur de la zone
                                efface_save() #cela empeche les superpositions de couleurs differentes qui rend moche (qlq pixel noircissent sinon), mais n'empeche pas la superposition de meme couleur (rendu progressif)                     
                        bsavecolor()
                        self.curseursave=0
                else:
                        if self.curseursave==0: #permet d'effacer la surface qu'une fois lorsque que le curseur est dans la zone exterieur de clic alors qu'avant il etait a l'interieur de la zone
                                efface_save()
                        bsave()
                        self.curseursave=1
        
                        
                for event in pygame.event.get():
                        touche2=pygame.key.get_pressed()
                        
                        if event.type==KEYDOWN:
                            if event.key == K_ESCAPE:
                                return (1,0,self.kaide,self.ksaisi,0,0)


                            elif touche2[K_LCTRL] and event.key==K_r:
                                self.grillemodifiable=reset_grille(self.grillemodifiable)
                                print self.grillemodifiable
                                print "gros reset"
                                #return (0,1,0,0,0,1)
                                self.ksaisi=0
                                return (0,1,0,self.ksaisi,0,1)
                                

                            elif event.key==K_r:
                                print "petit reset" #retour a la derniere save
                                return (2,0,self.kaide,self.ksaisi,0,1)

########################################################################################### code TRICHE (debut) ################################################################################################################
                        
                        #le raccourci CTRL+h permet d'utiliser une aide sans quel soit compter dans le compteur aide
                        #seulement utile dans la demonstration de soutenance de projet pour finir une grille rapidement
                        
                            elif touche2[K_LCTRL] and event.key==K_h: #code TRICHE
                                            solution_utile=self.solution_utile()
                                            
                                            aide=choice(solution_utile) #prend un sous tableau aleatoire parmis les sous tableaus de solution_utile
                                            if aide[0]==1:
                                                    fenetre.blit(nbr_r1,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=1 #ecriture du nbr manuellement
                                            elif aide[0]==2:
                                                    fenetre.blit(nbr_r2,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=2
                                            elif aide[0]==3:
                                                    fenetre.blit(nbr_r3,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=3
                                            elif aide[0]==4:
                                                    fenetre.blit(nbr_r4,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=4                                        
                                            elif aide[0]==5:
                                                    fenetre.blit(nbr_r5,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=5                                                         
                                            elif aide[0]==6:
                                                    fenetre.blit(nbr_r6,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=6                                    
                                            elif aide[0]==7:
                                                    fenetre.blit(nbr_r7,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=7
                                            elif aide[0]==8:
                                                    fenetre.blit(nbr_r8,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=8
                                            elif aide[0]==9:
                                                    fenetre.blit(nbr_r9,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=9
                                            print(self.grillemodifiable)
                                            return (0,1,self.kaide,self.ksaisi,0,0)                                      
########################################################################################### code TRICHE (fin)################################################################################################################                            

                            if event.key==K_h:
                                    if self.kaide>0:
                                            self.kaide-=1
                                            self.ksaisi+=1
                                            solution_utile=self.solution_utile()
                                            
                                            aide=choice(solution_utile) #prend un sous tableau aleatoire parmis les sous tableaus de solution_utile
                                            if aide[0]==1:
                                                    fenetre.blit(nbr_r1,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=1 #ecriture du nbr manuellement
                                            elif aide[0]==2:
                                                    fenetre.blit(nbr_r2,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=2
                                            elif aide[0]==3:
                                                    fenetre.blit(nbr_r3,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=3
                                            elif aide[0]==4:
                                                    fenetre.blit(nbr_r4,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=4                                        
                                            elif aide[0]==5:
                                                    fenetre.blit(nbr_r5,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=5                                                         
                                            elif aide[0]==6:
                                                    fenetre.blit(nbr_r6,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=6                                    
                                            elif aide[0]==7:
                                                    fenetre.blit(nbr_r7,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=7
                                            elif aide[0]==8:
                                                    fenetre.blit(nbr_r8,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=8
                                            elif aide[0]==9:
                                                    fenetre.blit(nbr_r9,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=9
                                                    
                                            
                                            print(self.grillemodifiable)

                                    else:
                                        print "tu utilise touts les aides"
                                        erreuraide()
                                        
                                    return (0,1,self.kaide,self.ksaisi,0,0)
                                        

                        
                        elif event.type==QUIT:
                                print("a+ mon amis")
                                logout(self.joueur)
                                jeu=False
                                pygame.quit()
                                return (0,0,self.kaide,self.ksaisi,0,0)

                        
                        elif event.type==MOUSEBUTTONDOWN:  
                                if event.button==1:
                                    ligne=0
                                    col=0
                                    i=0
                                    for ligne in range (0,7): #de 0 a 6
                                            for col in range (0,7):
                                                    if  (sx>grillex+taille_sprite*col+col and sx<grillex+taille_sprite*(col+1)+col) and (sy>grilley+taille_sprite*ligne+ligne and sy<grilley+taille_sprite*(ligne+1)+ligne):
                                                        
                                                        if (self.grillemodifiable[ligne][col]!='x'):
                                                            achiffre=self.grillemodifiable[ligne][col]
                                                            if self.blocn==0:
                                                            
                                                                            entre,tempaddi= saisir_nombre( grillex+taille_sprite*col+col+1, grilley+taille_sprite*ligne+ligne+1,tempp)
                                                                            print entre
                                                                            print(self.grillemodifiable)
                                                                            efface()
                                                                            if entre!=0:      
                                                                                    self.grillemodifiable[ligne][col]=entre #affichage du nbr et maj du nbr ajouté
                                                                                    self.ksaisi+=1
                                                                                    anti_doublon_horizontale(achiffre,self.grillemodifiable[ligne],grilley+taille_sprite*ligne+ligne)
                                                                                    anti_doublon_verticale(achiffre,self.grillemodifiable,col,grillex+taille_sprite*col+col)
                                                                                    return (0,1,self.kaide,self.ksaisi,tempaddi,1)
                                                                            else:
                                                                                print "erruer"
                                                                                erreurchiffre()
                                                                                return (0,0,self.kaide,self.ksaisi,tempaddi,1)
                                                                                                                                                        
                                                                            print(self.grillemodifiable)


                                                                            
                                                            else:
                                                            
                                                                self.grillemodifiable[ligne][col]=self.blocn
                                                                fenetre.blit(nbrmodif[self.blocn-1],(grillex+taille_sprite*col+col+1, grilley+taille_sprite*ligne+ligne+1)) #nbrmodif defini dans Constante.py
                                                                self.ksaisi+=1
                                                                anti_doublon_horizontale(achiffre,self.grillemodifiable[ligne],grilley+taille_sprite*ligne+ligne)
                                                                anti_doublon_verticale(achiffre,self.grillemodifiable,col,grillex+taille_sprite*col+col)
                                                                self.blocn=0
                                                                fenetre.blit(saisie_blocn,(70,60))
                                                                print(self.grillemodifiable)
                                                                return (0,1,self.kaide,self.ksaisi,0,0)
                                                                        
                                                                    #efface()
                                                                    

                                                                   
                                                                    #anti_doublon: si au moment de la saisie, l ancien nombre (qui est ecrasé par la nouvelle  saisie) etait present 2 fois, (erreur en rouge), il n'y est donc qu'une plus fois mtn entre 2 case obtacles/sommes
                                                                    #alors on ecrase par dessus la valeur de ce meme nombre sur toute la ligne/colonne (et non pas entre 2case obtacles/somme car necessite de faire d'autre fonction...) si elle n'est plus presente qu'une seule fois
                                                                    #il peut donc avoir un collage de meme nombre par dessus le meme (situation rare mais possible qui gene en rien le prgrm) si ce nombre repete etait present dans la meme ligne/colonne mais pas entre le meme intervalle de case obtacle/somme
                                                                    #-->il n'y a aucune effet clignotant car la fenetre n'est jamais mis a jour entre anti_doublon et doublon.
                                                                    
                                                        else:
                                                            print("bloc clic")
                                                    

                                    ligne=0
                                    col=0
                                    i=-1
                                    tab=[9,8,7,6,5,4,3,2,1]
                                    for ligne in range(0,3):
                                            for col in range(0,3):
                                                      i+=1
                                                      if  (sx>grillex-taille_sprite*(col+2)-col and sx<grillex-taille_sprite*(col+1)-col) and (sy>grilley+taille_sprite*ligne+ligne and sy<grilley+taille_sprite*(ligne+1)+ligne):
                                                             x=grillex-taille_sprite*(col+2)-col-2
                                                             y=grilley+taille_sprite*ligne+ligne
                                                             fenetre.blit(saisie_blocn,(70,60))
                                                             fenetre.blit(focus,(x,y))
                                                             self.blocn=tab[i]
                                                             print (tab[i])


                                 
                                
                                        

                                    if sx>34 and sx<261 and sy>356 and sy<388:
                                        print "tu sauvegarde ta grille"
                                        self.save_grille()
                                        self.save_stats(tempp)

                                    if sx>34 and sx<190 and sy>406 and sy<437:
                                        print "tu triches :("
                                  
                                        solution_utile=self.solution_utile()
                                           
                                        while solution_utile!=[]:
                                            
                                            aide=choice(solution_utile) #prend un sous tableau aleatoire parmis les sous tableaus de solution_utile
                                            if aide[0]==1:
                                                fenetre.blit(nbr_1,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                self.grillemodifiable[aide[2]][aide[1]]=1 #ecriture du nbr manuellement
                                            elif aide[0]==2:
                                                    fenetre.blit(nbr_2,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=2
                                            elif aide[0]==3:
                                                    fenetre.blit(nbr_3,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=3
                                            elif aide[0]==4:
                                                    fenetre.blit(nbr_4,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=4                                        
                                            elif aide[0]==5:
                                                    fenetre.blit(nbr_5,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=5                                                         
                                            elif aide[0]==6:
                                                    fenetre.blit(nbr_6,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=6                                    
                                            elif aide[0]==7:
                                                    fenetre.blit(nbr_7,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=7
                                            elif aide[0]==8:
                                                    fenetre.blit(nbr_8,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=8
                                            elif aide[0]==9:
                                                    fenetre.blit(nbr_9,(aide[1]*taille_sprite+grillex+aide[1]*1+1 , aide[2]*taille_sprite+grilley+1*aide[2]+1))
                                                    self.grillemodifiable[aide[2]][aide[1]]=9
                                            solution_utile=self.solution_utile()
                                        
                                        


                                if event.button==3:
                                    ligne=0
                                    col=0
                                    i=0
                                    for ligne in range (0,7): #de 0 a 6
                                            for col in range (0,7):
                                                    if  (sx>grillex+taille_sprite*col+col and sx<grillex+taille_sprite*(col+1)+col) and (sy>grilley+taille_sprite*ligne+ligne and sy<grilley+taille_sprite*(ligne+1)+ligne):
                                                            if (self.grillemodifiable[ligne][col]!='x'):
                                                                    achiffre=self.grillemodifiable[ligne][col]
                                                                    self.grillemodifiable[ligne][col]= 0
                                                                    fenetre.blit(case_blanc,(grillex+col*taille_sprite+col+1 , grilley+ligne*taille_sprite+ligne+1))
                                                                   
                                                                    print(self.grillemodifiable)
                                                                
                                                                    anti_doublon_horizontale(achiffre,self.grillemodifiable[ligne],grilley+taille_sprite*ligne+ligne)
                                                                    anti_doublon_verticale(achiffre,self.grillemodifiable,col,grillex+taille_sprite*col+col)
                                                                    return (0,1,self.kaide,self.ksaisi,0,0)

                                                            else:
                                                                print("bloc clic")
                                    
                                                    
                                                            
                                          
                                    #return (0,self.grillemodifiable,1)
                           # else:
                                    
                                return (0,0,self.kaide,self.ksaisi,0,0)
                else:
                        return (0,0,self.kaide,self.ksaisi,0,0)


                

        def saisir_editer(self,fenetre,kedit):
                """
                gestion de toutes les interractions possible du joueur par clavier/souris pendant le mode edition (qui permet au joueur de creer sa grille)
                ---------------------------------------------------------------------------------------------------------------
                ENTRE:
                fenetre:(viens de pygame definis dans CONSTANTE.py)
                        necessaire pour pouvoir faire des collages d'image dans cette fonction
                kedit:(int) compteur qui permet de bloquer le bouton a une utilisation par programme de la fonction solution,
                            car si on l'utilise plus d'une fois par jeu le prgrm plante...(par manque de temps c'est notre seul solution)
                            /!\un joueur peut creer autant de grille qu'il souhaite, mais qu'une seule grille par jeu lancé, pour créer deux grilles il devra donc relancer le jeu/!\
                ---------------------------------------------------------------------------------------------------------------
                SORTIE:
                boolean "de type int"
                        0-> retour au menu precedent
                        1->rien ne se passe
                boolean "de type int"
                        0->la fonction solution n'a pas etait lancé
                        1->la fonction solution a etait lancé

                """
                
                (sx,sy)=pygame.mouse.get_pos()
                

                if sx>34 and sx<261 and sy>356 and sy<388: #pos exacte du rectangle cree pour le clic 'sauvegarder' dans efface_save
                        if self.curseursave==1: #permet d'effacer la surface qu'une lorsque que le curseur est dans la zone de clic alors qu'avant il etait a l'exterieur de la zone
                                efface_save() #cela empeche les superpositions de couleurs differentes qui rend moche (qlq pixel noircissent sinon), mais n'empeche pas la superposition de meme couleur (rendu progressif)                     
                        bsavecolor()
                        self.curseursave=0
                else:
                        if self.curseursave==0: #permet d'effacer la surface qu'une fois lorsque que le curseur est dans la zone exterieur de clic alors qu'avant il etait a l'interieur de la zone
                                efface_save()
                        bsave()
                        self.curseursave=1

                for event in pygame.event.get():
                        if event.type==KEYDOWN:
                                if event.key == K_ESCAPE:
                                        return 0,kedit

                                        
                        elif event.type==QUIT:
                                logout(self.joueur)
                                jeu=False
                                pygame.quit()
                                return -1,kedit
                        
                        elif event.type==MOUSEBUTTONDOWN:
                                    
                            if event.button==1:
                               
                                        
                                        if (sx>76 and sx<76+taille_sprite+1) and (sy>64 and sy<64+taille_sprite+1):
                                                print("selection bloc obtacle")
                                                fenetre.blit(saisie_bloc,(70,60))
                                                fenetre.blit(focus,(76,64))                      
                                                self.bloc="obstacle"

                                        elif (sx>76+taille_sprite*2 and sx<76+taille_sprite*3+1) and (sy>64 and sy<63+taille_sprite+1):
                                                print("selection bloc somme")
                                                fenetre.blit(saisie_bloc,(70,60))
                                                fenetre.blit(focus,(76+taille_sprite*2,64))
                                                self.bloc="somme"

                                        elif (sx>76 and sx<114+taille_sprite+1) and (sy>64+taille_sprite*2+2 and sy<64+taille_sprite*3+3):
                                                print("selection bloc somme inf")
                                                fenetre.blit(saisie_bloc,(70,60))
                                                fenetre.blit(focus,(76,64+taille_sprite*2+2))
                                                self.bloc="inf"

                                        elif (sx>76+taille_sprite*2 and sx<76+taille_sprite*3+1) and (sy>64+taille_sprite*2+2 and sy<63+taille_sprite*3+3):
                                                print("selection bloc somme sup")
                                                fenetre.blit(saisie_bloc,(70,60))
                                                fenetre.blit(focus,(76+taille_sprite*2,64+taille_sprite*2+2))
                                                self.bloc="sup"

                                        elif sx>34 and sx<261 and sy>356 and sy<388 and kedit==0:
                                                kedit=1
                                                print "tu sauvegarde ta grille"
                                                self.nsolution+=1       #on convertit tmp de sorte a pour utilisé la fonction de solution
                                                                #si le prgrm trouve autant de reponse que de nombre modifiable, alors il n'existe qu'une unique solution

                                                                #a cause de la fonction qui convertit appliqué sur tmp, self.structure a etait modifié(adresse)... on la recupere donc dans le txt

                                                                #on enregistre la grille du joueur seulement si la solution est unique, et dans un autre fichier on enregistre la solution
                                        
                                       
                                                
                                                chaine="" #tabl en chaine
                                                for element in self.structuredite:
                                                           for sselement in element:
                                                               chaine=chaine+sselement
                                                print "chaine"
                                                print chaine
                                                print "chaine"

                                                ligne="" #chaine en txt
                                                fichierr=open("img/tmp.txt",'w')
                                                print "self.structuredite"
                                                print self.structuredite
                                                print "self.structuredite"
                                
                                                
                                                for element in self.structuredite:
                                                          for sselement in element:
                                                              ligne=ligne+sselement
                                                          fichierr.write(ligne+"\n")
                                                          ligne=""
                                                fichierr.close()


                                               

                                                tmp=self.structuredite
                                                tmp=conv(tmp)#conversion avec brick blank et tout...
                                                print solution(tmp)
                                                #nbtrait=nbtrait(tmp)
                                                #if solution(tmp)!=[]:
                                                fichier=open("img/tmp.txt",'r')
                                                txtbrute=fichier.read()
                                                print "txtbrute"
                                                print txtbrute
                                                print "txtbrute"
                                                print "ntrait"
                                                print nbtrait(txtbrute)
                                                print "ntrait"
                                                
                                                if len(solution(tmp))==nbtrait(txtbrute):
                                                    print("tu saves solution unique")
                                                    print solution(tmp)
                                                    self.save()
                                                    save_solution(self.joueur,solution(tmp))
                                                    
        ##                                            return 2
        ##                                        
        ##
        ##
        ##                                    
                                                else:
                                                    print("niv impossible")
                                                    if len(solution(tmp))>0:
                                                        print("trop de solution enfaite")
                                                        print solution(tmp)
                                                    with open("img//tmp.txt",'r') as fichier: #txt en chaine
                                                        structure=[]
                                                        for ligne in fichier:
                                                            ligne_structure=[]
                                                            for sprite in ligne:
                                                                if sprite!='\n':
                                                                    ligne_structure.append(sprite)
                                                            structure.append(ligne_structure)

                         
                                                    
                                                    chaine="" #chaine en pseudo brute
                                                    for ligne in range(0,7):
                                                        for col in range(0,7):
                                                            if structure[ligne][col]=='(':
                                                                chaine='('
                                                                del structure[ligne][col]
                                                                while  structure[ligne][col] != ')':
                                                                    #col+=1
                                                                    #print structure[ligne][col]
                                                                    chaine=chaine+structure[ligne][col]
                                                                    del structure[ligne][col]
                                                                chaine=chaine+')'
                                                                structure[ligne][col]=chaine
                                                                
         
                                                    
                                                    self.structuredite=structure
                                                return 1,1
                                                        

                                        

                                        ligne=0
                                        col=0
                                        i=0
                                        nbr_inf=0
                                        nbr_sup=0
                                        for ligne in range (0,7): #de 0 a 6
                                                for col in range (0,7):
                                                        if  (sx>grillex+taille_sprite*col+col and sx<grillex+taille_sprite*(col+1)+col) and (sy>grilley+taille_sprite*ligne+ligne and sy<grilley+taille_sprite*(ligne+1)+ligne):
                                                                
                                                                x=grillex+col*taille_sprite+col+1
                                                                y=grilley+ligne*taille_sprite+ligne+1
                                                                
                                                                
                                                                if self.bloc=="obstacle":
                                                                        fenetre.blit(case_noir,(x,y))
                                                                        self.structuredite[ligne][col]='x' #maj structure brute
                                                                elif self.bloc=="somme":
                                                                        nbr_inf=saisir_nombredite("nombre inferieur")
                                                                        nbr_sup=saisir_nombredite("nombre superieur")
                                                                        efface()
                                                                       
                                                                        
                                                                        fenetre.blit(case_blanc,(x,y))         #ont affiche le fond blanc, car dans certaine situation, il y a un bug d affichage
                                                                                                               #car on colle des images avec des trous, il faut boucher ces trous, sinon le joueur pourra voir l'image d'avant par les "trous"
                                                                                                               #alors on definis par defaut les trous par des case_blanc qui est l'image par defaut de la grille (grille vide)
                                                                        
                                                                        p=-1
                                                                        while p<9: #affichage auto
                                                                                p+=1
                                                                                if nbr_inf[1]==chiffre[p]:
                                                                                        fenetre.blit(inf1[p],(x,y))
                                                                                        p+=9
                                                                        p=-1
                                                                        while p<9:
                                                                                p+=1
                                                                                if nbr_sup[1]==chiffre[p]:
                                                                                        fenetre.blit(sup1[p],(x,y))
                                                                                        p+=9

                                                                        if nbr_inf[0]=='1': #affichage a la main
                                                                                fenetre.blit(inf2_1,(x,y)) 
                                                                        if nbr_inf[0]=='2':
                                                                                fenetre.blit(inf2_2,(x,y))
                                                                        if nbr_inf[0]=='3':
                                                                                fenetre.blit(inf2_3,(x,y))



                                                                        if nbr_sup[0]=='1':
                                                                                fenetre.blit(sup2_1,(x,y)) 
                                                                        if nbr_sup[0]=='2':
                                                                                fenetre.blit(sup2_2,(x,y))
                                                                        if nbr_sup[0]=='3':
                                                                                fenetre.blit(sup2_3,(x,y))
                                                                
                                                                        self.structuredite[ligne][col]=('('+nbr_inf+','+nbr_sup+')') #maj de la structure brute edite

                                                                        
                                                                        
                                                                elif self.bloc=="inf":
                                                                        nbr_inf=saisir_nombredite("nombre inferieur")
                                                                        efface()
                                                                        fenetre.blit(case_blanc,(x,y))
                                                                        nbr_sup="zz"

                                                                        if nbr_inf[0]=='1': #affichage a la main
                                                                                fenetre.blit(inf2_1,(x,y)) 
                                                                        elif nbr_inf[0]=='2':
                                                                                fenetre.blit(inf2_2,(x,y))
                                                                        elif nbr_inf[0]=='3':
                                                                                fenetre.blit(inf2_3,(x,y))
                                                                        #else:
                                                                                #fenetre.blit(case_blanc,(x,y))

                                                                                
                                                                                

                                                                        p=-1
                                                                        while p<9: #affichage auto
                                                                                p+=1
                                                                                if nbr_inf[1]==chiffre[p]:
                                                                                        fenetre.blit(inf1[p],(x,y))
                                                                                        p+=9

                                                                        fenetre.blit(sup_noir,(x,y)) #forcement car nb_sup est "zz"
                                                                        
                                                                        self.structuredite[ligne][col]=('('+nbr_inf+','+nbr_sup+')') #on code de la meme facon le fichier texte pour que self.structuredite et self.structure soit compatible
                                                                                                                                     #de cette maniere le joueur pourra jouer a son niveau sans a devoir modifier ce qui est fait precedement



                                                                elif self.bloc=="sup":
                                                                        nbr_inf="zz"
                                                                        nbr_sup=saisir_nombredite("nombre superieur")
                                                                        fenetre.blit(case_blanc,(x,y))
                                                                        efface()

                                                                        if nbr_sup[0]=='1':
                                                                                fenetre.blit(sup2_1,(x,y)) 
                                                                        elif nbr_sup[0]=='2':
                                                                                fenetre.blit(sup2_2,(x,y))
                                                                        elif nbr_sup[0]=='3':
                                                                                fenetre.blit(sup2_3,(x,y))
                                                                       # else:
                                                                               # fenetre.blit(case_blanc,(x,y)) 
                                                                                                               
                                                                                                               

                                                                        p=-1
                                                                        while p<9:
                                                                                p+=1
                                                                                if nbr_sup[1]==chiffre[p]:
                                                                                        fenetre.blit(sup1[p],(x,y))
                                                                                        p+=9


                                                                        fenetre.blit(inf_noir,(x,y))
                                                                        self.structuredite[ligne][col]=('('+nbr_inf+','+nbr_sup+')')
                                                                        
                                                                print(self.structuredite)
                                                                


                            elif event.button==3:
                                        ligne=0
                                        col=0
                                        i=0
                                        for ligne in range (0,7): #de 0 a 6
                                                for col in range (0,7):
                                                        if  (sx>grillex+taille_sprite*col+col and sx<grillex+taille_sprite*(col+1)+col) and (sy>grilley+taille_sprite*ligne+ligne and sy<grilley+taille_sprite*(ligne+1)+ligne):
                                                                        fenetre.blit(case_blanc,(grillex+col*taille_sprite+col+1 , grilley+ligne*taille_sprite+ligne+1))
                                                                        self.structuredite[ligne][col]='_'
                                                                        print(self.structuredite)
                                        

                               
                                        

                return 1,kedit
                
                                                                
                                                                
                                                                
                                                
                                        

        

#print(self.noirsup)

        def verif_horizontale(self):
                """
                verifie si la somme de la rangé des nombres modifiable corresponde au nombre superieur noir qui lui est associé
                ---------------------------------------------------------------------------------------------------------------
                SORTIE:
                boolean "de type int"
                        1-> TOUTS les sommes horizontale corresponde au nombre noir superieur qui lui est associé
                        0-> il y a au moin une rangé où la somme des cases modifiable ne correspond pas au nombre noir superieur
                ---------------------------------------------------------------------------------------------------------------
                REMARQUE:
                voir la fonction "afficher(self,fenetre)" dans Class.py pour avoir plus de details sur self.noirsup

                dans une meme ligne (horizontale) il peut y avoir plusieurs rangées, une rangé commence a un nombre somme et termine: soit au prochain obstacle, soit au prochain case somme, soit juste avant la sortie de la grille

                cette fonction fait partie des 4 conditions necessaires pour que le programme detecte qu'une grille a etait gagné par le joueur:
                        condition1: touts les nombres modifiables horizontales corresponde au nombre somme associé
                        condition2: touts les nombres modifiables verticales corresponde au nombre somme associé
                        condition3: aucun doublon dans la meme rangé horizontale
                        condition4: aucun doublon dans la meme rangé verticale
                """



                k=0
                longg=len(self.noirsup)
                for element in self.noirsup:
                        #if element[0]==0 and sommehori(self.grillemodifiable[element[2]],element[1])==0: #car on init k=0 dans la fonction, il ne faut pas compter pour 0 les cases vides!
                               # pass #ne fait rien                                                   #sinon en jeu le programe validera la ligne: 8=0+ 8 --> alors qu il y a un trou
                                #print("ici")
                       # print element[0],self.grillemodifiable[element[2]],element[1]
                        if element[0]==sommehori(self.grillemodifiable[element[2]],element[1]):
                                k+=1
                                if k==longg:
                                        print("somme horizontale")
                                        return 1
                                      
                return 0
#si 1 alors teste bon




        def verif_verticale(self):
                """
                verifie si la somme de la rangé des nombres modifiable corresponde au nombre inferieur noir qui lui est associé
                ---------------------------------------------------------------------------------------------------------------
                SORTIE:
                boolean "de type int"
                        1-> TOUTS les sommes verticale corresponde au nombre noir inferieur qui lui est associé
                        0-> il y a au moin une rangé où la somme des cases modifiable ne correspond pas au nombre noir inferieur
                ---------------------------------------------------------------------------------------------------------------
                REMARQUE:
                voir la fonction "afficher(self,fenetre)" dans Class.py pour avoir plus de details sur self.noirsup

                dans une meme colonne (verticale) il peut y avoir plusieurs rangées, une rangé commence a un nombre somme et termine: soit au prochain obstacle, soit au prochain case somme, soit juste avant la sortie de la grille

                cette fonction fait partie des 4 conditions necessaires pour que le programme detecte qu'une grille a etait gagné par le joueur:
                        condition1: touts les nombres modifiables horizontales corresponde au nombre somme associé
                        condition2: touts les nombres modifiables verticales corresponde au nombre somme associé
                        condition3: aucun doublon dans la meme rangé horizontale
                        condition4: aucun doublon dans la meme rangé verticale
                """
                
                k=0
                longg=len(self.noirinf)
                for element in self.noirinf:
                        if element[0]==sommeverti(self.grillemodifiable,element[2],element[1]):  #/!\ mettre if pas elif /!\
                                        k+=1
                                        if k==longg:
                                                print("somme verticale")
                                                return 1
                        
                       
                return 0
#si 1 alors teste bon






        def doublon_horizontale(self,fenetre):
                """
                verifie qu'il n'y a aucun doublon (meme nombre modifiable) dans la rangé horizontale
                ---------------------------------------------------------------------------------------------------------------
                ENTRE:
                fenetre:(viens de pygame definis dans CONSTANTE.py)
                        necessaire pour pouvoir faire des collages d'image dans cette fonction
                ---------------------------------------------------------------------------------------------------------------
                SORITE:
                boolean "de type int"
                        0->il y a au moin un doublon
                        1->il n'y a aucun doublon
                ---------------------------------------------------------------------------------------------------------------
                REMARQUE:
                plusieurs nombre modifiable vide dans la meme rangé n'est pas concidéré comme un doublon

                dans la fonction, au debut on suppose qu'il n'y a aucun doublon, on cree 9compteurs different (correspond au chiffre 1a9) qui vont s'incrementer a chaque fois
                que le prgrm retrouve le chiffre qui correspond au compteur

                il est necessaire de conserver dans une variable la position du 1er nombre rencontré, car en cas de doublon le 1er nombre rencontré peut etre potentiellement faux
                (sinon le prgrm comprendra qu'a partir de la 2eme occurence du chiffre, tout les chiffres de cette valeur sont faux, alors que le 1er l'est peut etre aussi)

                le prgrm affiche une image avec le nombre barré pour chaque doublon

                cette fonction fait partie des 4 conditions necessaires pour que le programme detecte qu'une grille a etait gagné par le joueur:
                        condition1: touts les nombres modifiables horizontales corresponde au nombre somme associé
                        condition2: touts les nombres modifiables verticales corresponde au nombre somme associé
                        condition3: aucun doublon dans la meme rangé horizontale
                        condition4: aucun doublon dans la meme rangé verticale
                """
                
                num_ligne=0
                decaly=1
                verif=1 #booleen de sortie, il suffit qu'il y a au moin une erreur et la grille est sur de ne peut pas etre valide, verif=1(pas erreur), verif=0(il y a erreur)
                for ligne in self.grillemodifiable:  #--> on suppose donc qu il n y a pas d erreur jusqu a qu en on voit une
                        num_case=0
                        decalx=1
                        
                        un=0 #on compte pas les zeros
                        pun=0 #on sauvegarde la position de la 1er recurence du chiffre pour l'afficher SI il y a d'autre meme nombre dans la ligne
                        
                        deux=0 
                        pdeux=0
                        
                        trois=0
                        ptrois=0
                        
                        quatre=0
                        pquatre=0
                        
                        cinq=0
                        pcinq=0
                        
                        six=0
                        psix=0
                        
                        sept=0
                        psept=0
                        
                        huit=0
                        phuit=0
                        
                        neuf=0
                        pneuf=0
                        for element in ligne:
                                x = ((num_case) * taille_sprite)+grillex+decalx 
                                y = (num_ligne * taille_sprite)+grilley+decaly
                                if element=='x':
                                        un=0 #on compte pas les zeros, mais seulement les nbr de 1a9
                                        pun=0
                                        
                                        deux=0
                                        pdeux
                                        
                                        trois=0
                                        ptrois=0
                                        
                                        quatre=0
                                        pquatre=0
                                        
                                        cinq=0
                                        pcinq=0
                                        
                                        six=0
                                        psix=0
                                        
                                        sept=0
                                        psept=0
                                        
                                        huit=0
                                        phuit=0
                                        
                                        neuf=0
                                        pneuf=0
                                else:
                                        if element==1:
                                                un+=1
                                                if un==1:
                                                        pun=(x,y)#on save la position du nbr, si le nbr est affiché +1fois alors la 1er occurence est potentiellement fausse
                                                if un>1:
                                                        fenetre.blit(nbr_f1,(x,y)) #on affiche le nbr qui est repeté +1 fois a partir de la 2eme fois
                                                        fenetre.blit(nbr_f1,(pun)) #on affiche notre sauvegarde qui est la 1er occurence du nbr, car sinon le 1er nbr n est pas afficher
                                                        verif=0
                                                       # print("il ya trop de 1")
                                                
                                        elif element==2:
                                                deux+=1
                                                if deux==1:
                                                        pdeux=(x,y)
                                                if deux>1:
                                                        fenetre.blit(nbr_f2,(x,y))
                                                        fenetre.blit(nbr_f2,(pdeux))
                                                        verif=0
                                                       # print("il ya trop de 2")
                                                
                                        elif element==3:
                                                trois+=1
                                                if trois==1:
                                                        ptrois=(x,y)
                                                if trois>1:
                                                        fenetre.blit(nbr_f3,(x,y))
                                                        fenetre.blit(nbr_f3,(ptrois))
                                                        verif=0
                                                       # print("il ya trop de 3")
                                                
                                        elif element==4:
                                                quatre+=1
                                                if quatre==1:
                                                        pquatre=(x,y)
                                                if quatre>1:
                                                        fenetre.blit(nbr_f4,(x,y))
                                                        fenetre.blit(nbr_f4,(pquatre))
                                                        verif=0
                                                        #print("il ya trop de 4")
                                                
                                        elif element==5:
                                                cinq+=1
                                                if cinq==1:
                                                        pcinq=(x,y)
                                                if cinq>1:
                                                        fenetre.blit(nbr_f5,(x,y))
                                                        fenetre.blit(nbr_f5,(pcinq))
                                                        verif=0
                                                       # print("il ya trop de 5")
                                                
                                        elif element==6:
                                                six+=1
                                                if six==1:
                                                        psix=(x,y)
                                                if six>1:
                                                        fenetre.blit(nbr_f6,(x,y))
                                                        fenetre.blit(nbr_f6,(psix))
                                                        verif=0
                                                        #print("il ya trop de 6")
                                                
                                        elif element==7:
                                                sept+=1
                                                if sept==1:
                                                        psept=(x,y)
                                                if sept>1:
                                                        fenetre.blit(nbr_f7,(x,y))
                                                        fenetre.blit(nbr_f7,(psept))
                                                        verif=0
                                                       # print("il ya trop de 7")
                                                
                                        elif element==8:
                                                huit+=1
                                                if huit==1:
                                                        phuit=(x,y)
                                                if huit>1:
                                                        fenetre.blit(nbr_f8,(x,y))
                                                        fenetre.blit(nbr_f8,(phuit))
                                                        verif=0
                                                        #print("il ya trop de 8")
                                                
                                        elif element==9:
                                                neuf+=1
                                                if neuf==1:
                                                        pneuf=(x,y)
                                                if neuf>1:
                                                        fenetre.blit(nbr_f9,(x,y))
                                                        fenetre.blit(nbr_f9,(pneuf))
                                                        verif=0
                                                        #print("il ya trop de 9")

                            
                                num_case+=1
                                decalx+=1
                        num_ligne+=1
                        decaly+=1
                        
                return verif
#si 1 alors teste bon
                                                
                                
        def doublon_verticale(self,fenetre):
                """
                verifie qu'il n'y a aucun doublon (meme nombre modifiable) dans la rangé verticale
                ---------------------------------------------------------------------------------------------------------------
                ENTRE:
                fenetre:(viens de pygame definis dans CONSTANTE.py)
                        necessaire pour pouvoir faire des collages d'image dans cette fonction
                ---------------------------------------------------------------------------------------------------------------
                SORITE:
                boolean "de type int"
                        0->il y a au moin un doublon
                        1->il n'y a aucun doublon
                ---------------------------------------------------------------------------------------------------------------
                REMARQUE:
                plusieurs nombre modifiable vide dans la meme rangé n'est pas concidéré comme un doublon

                dans la fonction, au debut on suppose qu'il n'y a aucun doublon, on cree 9compteurs different (correspond au chiffre 1a9) qui vont s'incrementer a chaque fois
                que le prgrm retrouve le chiffre qui correspond au compteur

                il est necessaire de conserver dans une variable la position du 1er nombre rencontré, car en cas de doublon le 1er nombre rencontré peut etre potentiellement faux
                (sinon le prgrm comprendra qu'a partir de la 2eme occurence du chiffre, tout les chiffres de cette valeur sont faux, alors que le 1er l'est peut etre aussi)

                le prgrm affiche une image avec le nombre barré pour chaque doublon

                cette fonction fait partie des 4 conditions necessaires pour que le programme detecte qu'une grille a etait gagné par le joueur:
                        condition1: touts les nombres modifiables horizontales corresponde au nombre somme associé
                        condition2: touts les nombres modifiables verticales corresponde au nombre somme associé
                        condition3: aucun doublon dans la meme rangé horizontale
                        condition4: aucun doublon dans la meme rangé verticale
                """
                
                num_case=0
                decalx=1
                verif=1
                for col in range(0,7):
                        num_ligne=0      #<==> for col in range(0,len(self.grillemodifiable+1)):    
                        decaly=1        #car tout les grilles ont une longueur de 7

                        un=0            #on compte pas les zeros
                        pun=0 
                        
                        deux=0
                        pdeux=0
                        
                        trois=0
                        ptrois=0
                        
                        quatre=0
                        pquatre=0
                        
                        cinq=0
                        pcinq=0
                        
                        six=0
                        psix=0
                        
                        sept=0
                        psept=0
                        
                        huit=0
                        phuit=0
                        
                        neuf=0
                        pneuf=0
                        for ligne in range(0,7):
                        
                                x = ((num_case) * taille_sprite)+grillex+decalx 
                                y = (num_ligne * taille_sprite)+grilley+decaly
                                
 
                                if self.grillemodifiable[ligne][col]=='x':
                                                un=0 #on compte pas les zeros, mais seulement les nbr de 1a9
                                                pun=0
                                                
                                                deux=0
                                                pdeux=0
                                                
                                                trois=0
                                                ptrois=0
                                                
                                                quatre=0
                                                pquatre=0
                                                
                                                cinq=0
                                                pcinq=0
                                                
                                                six=0
                                                psix=0
                                                
                                                sept=0
                                                psept=0
                                                
                                                huit=0
                                                phuit=0
                                                
                                                neuf=0
                                                pneuf=0
                                else:
                                                if self.grillemodifiable[ligne][col]==1:
                                                        un+=1
                                                        if un==1:
                                                                pun=(x,y)
                                                        if un>1:
                                                                fenetre.blit(nbr_f1,(x,y))
                                                                fenetre.blit(nbr_f1,(pun))
                                                                verif=0
                                                                #print("il ya trop de 1")
                                                                
                                                elif self.grillemodifiable[ligne][col]==2:
                                                        deux+=1
                                                        if deux==1:
                                                                pdeux=(x,y)
                                                        if deux>1:
                                                                fenetre.blit(nbr_f2,(x,y))
                                                                fenetre.blit(nbr_f2,(pdeux))
                                                                
                                                        
                                                elif self.grillemodifiable[ligne][col]==3:
                                                        trois+=1
                                                        if trois==1:
                                                                ptrois=(x,y)
                                                        if trois>1:
                                                                fenetre.blit(nbr_f3,(x,y))
                                                                fenetre.blit(nbr_f3,(ptrois))
                                                               
                                                                
                                                elif self.grillemodifiable[ligne][col]==4:
                                                        quatre+=1
                                                        if quatre==1:
                                                                pquatre=(x,y)
                                                        if quatre>1:
                                                                fenetre.blit(nbr_f4,(x,y))
                                                                fenetre.blit(nbr_f4,(pquatre))
                                                                verif=0
                                                               

                                                elif self.grillemodifiable[ligne][col]==5:
                                                        cinq+=1
                                                        if cinq==1:
                                                                pcinq=(x,y)
                                                        if cinq>1:
                                                                fenetre.blit(nbr_f5,(x,y))
                                                                fenetre.blit(nbr_f5,(pcinq))
                                                                verif=0
                                                            
                                                                
                                                elif self.grillemodifiable[ligne][col]==6:
                                                        six+=1
                                                        if six==1:
                                                                psix=(x,y)
                                                        if six>1:
                                                                fenetre.blit(nbr_f6,(x,y))
                                                                fenetre.blit(nbr_f6,(psix))
                                                                verif=0
                                                               
                                                                
                                                elif self.grillemodifiable[ligne][col]==7:
                                                        sept+=1
                                                        if sept==1:
                                                                psept=(x,y)
                                                        if sept>1:
                                                                fenetre.blit(nbr_f7,(x,y))
                                                                fenetre.blit(nbr_f7,(psept))
                                                                verif=0
                                                                
                                                                
                                                elif self.grillemodifiable[ligne][col]==8:
                                                        huit+=1
                                                        if huit==1:
                                                                phuit=(x,y)
                                                        if huit>1:
                                                                fenetre.blit(nbr_f8,(x,y))
                                                                fenetre.blit(nbr_f8,(phuit))
                                                                verif=0
                                                               
                                                                
                                                elif self.grillemodifiable[ligne][col]==9:
                                                        neuf+=1
                                                        if neuf==1:
                                                                pneuf=(x,y)
                                                        if neuf>1:
                                                                fenetre.blit(nbr_f9,(x,y))
                                                                fenetre.blit(nbr_f9,(pneuf))
                                                                verif=0
                   
                                num_ligne+=1
                                decaly+=1
                        
                                
                            
                        
                        num_case+=1
                        decalx+=1
                return verif                                          
#si 1 alors teste bon                                            

           
                        
            
