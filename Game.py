from typing import TypeVar
from Object import Object
from random import randint

Game = TypeVar("Game")

class Game:
        width=1250
        height=750
        dx=1
        dy=1
        def __init__(self):
            self.__aliens = []
            self.__sensAliens = 1
            self.__sensSpaceShip = 1
            self.__missiles = []
            self.__missilesAliens = []
            self.__obstacles = [Object('Obstacle',300,500,30,"brown",life=3),Object('Obstacle',330,500,30,"brown",life=3),
                                Object('Obstacle',360,500,30,"brown",life=3),Object('Obstacle',300,530,30,"brown",life=3),
                                Object('Obstacle',330,530,30,"brown",life=3),Object('Obstacle',360,530,30,"brown",life=3),
                                Object('Obstacle',390,500,30,"brown",life=3),Object('Obstacle',390,530,30,"brown",life=3),
                                Object('Obstacle',420,500,30,"brown",life=3),Object('Obstacle',420,530,30,"brown",life=3),
                                Object('Obstacle',300,560,30,"brown",life=3),Object('Obstacle',420,560,30,"brown",life=3),
                                
                                Object('Obstacle',600,500,30,"brown",life=3),Object('Obstacle',630,500,30,"brown",life=3),
                                Object('Obstacle',660,500,30,"brown",life=3),Object('Obstacle',600,530,30,"brown",life=3),
                                Object('Obstacle',630,530,30,"brown",life=3),Object('Obstacle',660,530,30,"brown",life=3),
                                Object('Obstacle',690,500,30,"brown",life=3),Object('Obstacle',690,530,30,"brown",life=3),
                                Object('Obstacle',720,500,30,"brown",life=3),Object('Obstacle',720,530,30,"brown",life=3),
                                Object('Obstacle',600,560,30,"brown",life=3),Object('Obstacle',720,560,30,"brown",life=3),
                                
                                Object('Obstacle',900,500,30,"brown",life=3),Object('Obstacle',930,500,30,"brown",life=3),
                                Object('Obstacle',960,500,30,"brown",life=3),Object('Obstacle',900,530,30,"brown",life=3),
                                Object('Obstacle',930,530,30,"brown",life=3),Object('Obstacle',960,530,30,"brown",life=3),
                                Object('Obstacle',990,500,30,"brown",life=3),Object('Obstacle',990,530,30,"brown",life=3),
                                Object('Obstacle',1020,500,30,"brown",life=3),Object('Obstacle',1020,530,30,"brown",life=3),
                                Object('Obstacle',900,560,30,"brown",life=3),Object('Obstacle',1020,560,30,"brown",life=3)]
                                
            self.__color = ["red","red","blue","green","black"]
            self.__alienSpaceShips=[]
            self.__alienSSpass=0 #est a 1 si une AlienSpaceShip est passer recament
            self.__texts=[]
            self.__score=0
            self.__niveau=1

    #getteur setteur ... AlienSpaceShip
        def getAlienSSpass(self) -> int:
            return self.__alienSSpass    
        def setAlienSSpass(self, alienSSpass:int) -> Game:
            self.__alienSSpass=alienSSpass
            return alienSSpass
    #getteur setteur ... Niveau
        def getNiveau(self) -> int:
            return self.__niveau    
        def setNiveau(self, niveau:int) -> Game:
            self.__niveau=niveau
            return niveau
        def addNiveau(self) -> Game:
            niveau = self.getNiveau()
            niveau+=1
            self.setNiveau(niveau)
            print(niveau)
            return self
    #getteur setteur .. Texts
        def getTexts(self) -> "texts":  
            return self.__texts
        def setTexts(self, texts:"texts") -> Game:
            self.__texts = texts
            return self
    #Score getteur setteur 
        def getScore(self) -> int: 
            return self.__score
        def setScore(self,score:int) -> Game:
            self.__score=score
            return self
        def plusScore(self, val:int) -> Game:
            self.setScore(self.getScore()+val)
            return self
    #SensSpaceShip getteur setteur ...
        def getSensSpaceShip(self) -> int:
            return self.__sensSpaceShip
        def setSensSpaceShip(self, sensSpaceShip:int) -> Game:
            self.__sensSpaceShip = sensSpaceShip
            return self
    #SpaceShip getteur setteur ...
        def getSpaceShip(self) -> "SpaceShip": 
            return self.__spaceShip
        def setSpaceShip(self, spaceShip:'SpaceShip') -> Game:
            self.__spaceShip=spaceShip
            return self        
        def moveSpaceShip(self) -> tuple:
            dy=0
            dx=15
            self.getSpaceShip().move(self.getSensSpaceShip()*dx,dy)
            return (dx, dy)
    #AlienSpaceShips getteur setteur    
        def getAlienSpaceShips(self) -> "alienSpaceShip":  
            return self.__alienSpaceShips
        def setAlienSpaceShips(self, alienSpaceShip:"alienSpaceShip") -> Game:
            self.__alienSpaceShips = alienSpaceShip
            return self
        def createAlienSpacShip(self,canvas:'Canvas Tkinter') -> Game:
            alienSpaceShip = Object('AlienSpaceShip', 50,50,25,'red',score=randint(1,4)*50)
            (x1, y1, x2, y2) = alienSpaceShip.getIdBox()
            size = x2-x1
            alienSpaceShip.setDraw(canvas.create_polygon(x1, y1, x2, y2, x1, y1+0.2*size, x2, y2-size*0.5, x1, y2, fill=alienSpaceShip.getColor()))
            self.addAlienSpaceShip(alienSpaceShip)
            return self
        def addAlienSpaceShip(self, alienSpaceShip:"alienSpaceShip") -> Game:
            alienSpaceShips = self.getAlienSpaceShips()
            alienSpaceShips.append(alienSpaceShip)
            self.setAlienSpaceShips(alienSpaceShips)
            return self
        def removeAlienSpaceShip(self, del_alienSpaceShip:"Obstacle") -> Game :
            alienSpaceShips = self.getAlienSpaceShips()
            alienSpaceShips.remove(del_alienSpaceShip)
            self.setAlienSpaceShips(alienSpaceShips)
            return self
        def moveAlienSpaceShips(self) -> tuple:
            dx=1.2
            for alienSpaceShip in self.getAlienSpaceShips():
                alienSpaceShip.move(dx,0)
            return (dx,0)  
    #Obstacle getteur setteur addeur removeur
        def getObstacles(self) -> list:
            return self.__obstacles
        def setObstacles(self, obstacles:list) -> Game:
            self.__obstacles=obstacles
            return self
        def addObstacle(self, obstacle:"Obstacle") -> Game:
            obstacles = self.getObstacles()
            obstacles.append(obstacle)
            self.setObstacles(obstacles)
            return self
        def removeObstacle(self, del_obstacle:"Obstacle") -> Game :
            obstacles = self.getObstacles()
            obstacles.remove(del_obstacle)
            self.setObstacles(obstacles)
            return self
    #Alien getteur setteur addeur removeur moveur
        def getAliens(self) -> list:
            return self.__aliens
        def setAliens(self, aliens:list) -> Game:
            if type(aliens)!=list:
                aliens=[]
            self.__aliens = aliens
            return self
        def addAlien(self, alien:"Alien") -> Game:
            aliens = self.getAliens()
            self.setAliens(aliens.append(alien))
            return self
        def removeAlien(self, del_alien:"Alien") -> Game:
            aliens = self.getAliens()
            aliens.remove(del_alien)
            self.setAliens(aliens)
            return self
        def moveAliens(self) -> tuple:
            dy=0
            if not self.checkWallColisionAliens():
                self.ChangeSensAliens()
                if self.getSensAliens()==1:
                    dy = self.dy*self.getNiveau()+15

            for alien in self.getAliens():
                alien.move(self.getSensAliens()*self.dx*self.getNiveau()*0.65,dy)
            return (self.getSensAliens()*self.dx*self.getNiveau()*0.65,dy)
    #particuliar methode for Aliens
        def getAliensIdBox(self) -> list:
            return [alien.getIdBox() for alien in self.getAliens()]
    #SensAleins getteur setteur
        def getSensAliens(self) -> int:
            return self.__sensAliens
        def ChangeSensAliens(self) -> Game:
            self.__sensAliens = -1 if self.__sensAliens==1 else 1
            return self
    #Missile getteur setteur ...
        def createMissile(self,x:int, canvas:'Canvas Tkinter') -> Game:
            missile = Object('Missile', x,700,25,'grey')
            (x1, y1, x2, y2) = missile.getIdBox()
            missile.setDraw(canvas.create_oval(x1, y1, x2, y2, fill=missile.getColor()))
            self.addMissile(missile)
            return self
        def getMissiles(self) -> list:
            return self.__missiles
        def setMissiles(self, missiles:list) -> Game:
            if type(missiles)!=list:
                missiles=[]
            self.__missiles = missiles
            return self
        def addMissile(self, missile:"Missile") -> Game:
            missiles = self.getMissiles()
            missiles.append(missile)
            self.setMissiles(missiles)
            return self
        def removeMissile(self, del_missile:"Missile") -> Game:
            missiles = self.getMissiles()
            missiles.remove(del_missile)
            self.setMissiles(missiles)
            return self
        def moveMissiles(self) -> tuple:
            for missile in self.getMissiles():
                missile.move(0,-2)
            return (0,-2)
        def getMissilesIdBox(self) -> list:
            return [missile.getIdBox() for missile in self.getMissiles()]#
    #MissileAlien getteur setteur ...
        def createMissileAlien(self,x:int, y:int, canvas:'Canvas Tkinter') -> Game:
            missileAlien = Object('MissileAlien', x,y,25,'black')
            (x1, y1, x2, y2) = missileAlien.getIdBox()
            missileAlien.setDraw(canvas.create_rectangle(x1, y1, x1+3, y2, fill=missileAlien.getColor()))
            self.addMissileAlien(missileAlien)
            return self
        def getMissilesAliens(self) -> list:
            return self.__missilesAliens
        def setMissilesAliens(self, missilesAliens:list) -> Game:
            if type(missilesAliens)!=list:
                missilesAliens=[]
            self.__missilesAliens = missilesAliens
            return self
        def addMissileAlien(self, missileAlien:"MissileAlien") -> Game:
            missilesAliens = self.getMissilesAliens()
            missilesAliens.append(missileAlien)
            self.setMissilesAliens(missilesAliens)
            return self
        def removeMissileAlien(self, del_missileAlien:"MissileAlien") -> Game:
            missilesAliens = self.getMissilesAliens()
            missilesAliens.remove(del_missileAlien)
            self.setMissilesAliens(missilesAliens)
            return self
        def moveMissilesAliens(self) -> tuple:
            dy=0
            for missileAlien in self.getMissilesAliens():
                dy=self.dy*self.getNiveau()*0.8
                missileAlien.move(0,dy)
            return(0,dy)
        def getMissilesAliensIdBox(self) -> list:
            return [missileAlien.getIdBox() for missileAlien in self.getMissilesAliens()]
#
        def removeObject(self, obj:Object, canvas:"Canvas Tkinter") -> Game:
            """Delete Object of different Type"""
            canvas.delete(obj.getDraw())
            ScoreObj = self.getTexts()['score']
            ScoreObj.setDescription('Score : '+str(self.getScore()))
            canvas.itemconfig(ScoreObj.getDraw(), text=ScoreObj.getDescription())
            if obj.getType()=='Alien':
                self.removeAlien(obj)
            elif obj.getType()=='Missile':
                self.removeMissile(obj)
            elif obj.getType()=='MissileAlien':
                self.removeMissileAlien(obj)
            elif obj.getType()=='Obstacle':
                self.removeObstacle(obj)
            elif obj.getType()=='AlienSpaceShip':
                self.removeAlienSpaceShip(obj)
            return self

        #Méthode qui permet d'afficher nos objets de manière graphique et initialise la partie
        def setUp(self, canvas:"Canvas Tkiter") -> Game:
            """ Fonction initialisation de nos objets au début de la partie """
            canvas.delete("all")
            self.__spaceShip=Object('SpaceShip',500,700,35,"black",life=3)
            self.setTexts({'score':Object('Text',1150,700,0,"black",description='Score : '+str(self.getScore())),
                        'life':Object('Text',1150,720,0,"black", description='Vie : '+str(self.getSpaceShip().getLife())),
                        'info':Object('Text',1150,740,0,"black", description='Toucher Q pour quitter!')})
            self.setAliens([Object('Alien', 50,50,25,"red",score=20),Object('Alien', 100,50,25,"red",score=20),
                            Object('Alien', 150,50,25,"red",score=20),Object('Alien', 200,50,25,"red",score=20),
                            Object('Alien', 250,50,25,"red",score=20),Object('Alien', 300,50,25,"red",score=20),
                            Object('Alien', 350,50,25,"red",score=20),Object('Alien', 400,50,25,"red",score=20),
                            Object('Alien', 450,50,25,"red",score=20),Object('Alien', 400,50,25,"red",score=20),
                            Object('Alien', 550,50,25,"red",score=20),Object('Alien', 500,50,25,"red",score=20),
                            Object('Alien', 650,50,25,"red",score=20),Object('Alien', 600,50,25,"red",score=20),
                            Object('Alien', 750,50,25,"red",score=20),Object('Alien', 700,50,25,"red",score=20),

                            Object('Alien', 50,100,20,"orange",score=20),Object('Alien', 100,100,20,"orange",score=20),
                            Object('Alien', 150,100,20,"orange",score=20),Object('Alien', 200,100,20,"orange",score=20),
                            Object('Alien', 250,100,20,"orange",score=20),Object('Alien', 300,100,20,"orange",score=20),
                            Object('Alien', 350,100,20,"orange",score=20),Object('Alien', 400,100,20,"orange",score=20),
                            Object('Alien', 450,100,20,"orange",score=20),Object('Alien', 400,100,20,"orange",score=20),
                            Object('Alien', 550,100,20,"orange",score=20),Object('Alien', 500,100,20,"orange",score=20),
                            Object('Alien', 650,100,20,"orange",score=20),Object('Alien', 600,100,20,"orange",score=20),
                            Object('Alien', 750,100,20,"orange",score=20),Object('Alien', 700,100,20,"orange",score=20),

                            Object('Alien', 50,150,25,"yellow",score=10),Object('Alien', 100,150,25,"yellow",score=10),
                            Object('Alien', 150,150,25,"yellow",score=10),Object('Alien', 200,150,25,"yellow",score=10),
                            Object('Alien', 250,150,25,"yellow",score=10),Object('Alien', 300,150,25,"yellow",score=10),
                            Object('Alien', 350,150,25,"yellow",score=10),Object('Alien', 400,150,25,"yellow",score=10),
                            Object('Alien', 450,150,25,"yellow",score=10),Object('Alien', 400,150,25,"yellow",score=10),
                            Object('Alien', 550,150,25,"yellow",score=10),Object('Alien', 500,150,25,"yellow",score=10),
                            Object('Alien', 650,150,25,"yellow",score=10),Object('Alien', 600,150,25,"yellow",score=10),
                            Object('Alien', 750,150,25,"yellow",score=10),Object('Alien', 700,150,25,"yellow",score=10)])
            self.setMissiles([])
            self.setMissilesAliens([])
            self.setAlienSpaceShips([])
            for text in self.getTexts().values():
                (x,y,a,b) = text.getIdBox()
                text.setDraw(canvas.create_text(x,y,text=text.getDescription()))
            #Affiche les aliens
            for alien in self.getAliens():
                (x1, y1, x2, y2) = alien.getIdBox()
                size = x1-x2
                alien.setDraw(canvas.create_polygon(x1, y1, x1, y1+0.2*size, x2, y2,  x2, y2-size*0.5, x1, y2, fill=alien.getColor()))
            #Affiche les obstacles
            for obstacle in self.getObstacles():
                (x1, y1, x2, y2) = obstacle.getIdBox()
                obstacle.setDraw(canvas.create_rectangle(x1, y1, x2, y2, fill=obstacle.getColor()))
            #Affiche notre vaisseau
            spaceShip = self.getSpaceShip()
            (x1, y1, x2, y2) = spaceShip.getIdBox()
            spaceShip.setDraw(canvas.create_polygon(x1+size*0.5, y1, x1, y1+0.4*size, x2, y2+0.3*size,  x2, y2-size*0.2, x1, y2,  fill=spaceShip.getColor()))

            return self

        def GameOver(self, canvas:"Canvas Tkiner", pnd:'fenetre Tkinter') -> Game:
            """Méthode appelée lorsqu'on perd la partie"""
            #On reinitialise les variables 
            self.setObstacles([Object('Obstacle',300,500,30,"brown",life=3),Object('Obstacle',330,500,30,"brown",life=3),
                                Object('Obstacle',360,500,30,"brown",life=3),Object('Obstacle',300,530,30,"brown",life=3),
                                Object('Obstacle',330,530,30,"brown",life=3),Object('Obstacle',360,530,30,"brown",life=3),
                                Object('Obstacle',390,500,30,"brown",life=3),Object('Obstacle',390,530,30,"brown",life=3),
                                Object('Obstacle',420,500,30,"brown",life=3),Object('Obstacle',420,530,30,"brown",life=3),
                                Object('Obstacle',300,560,30,"brown",life=3),Object('Obstacle',420,560,30,"brown",life=3),
                                
                                Object('Obstacle',600,500,30,"brown",life=3),Object('Obstacle',630,500,30,"brown",life=3),
                                Object('Obstacle',660,500,30,"brown",life=3),Object('Obstacle',600,530,30,"brown",life=3),
                                Object('Obstacle',630,530,30,"brown",life=3),Object('Obstacle',660,530,30,"brown",life=3),
                                Object('Obstacle',690,500,30,"brown",life=3),Object('Obstacle',690,530,30,"brown",life=3),
                                Object('Obstacle',720,500,30,"brown",life=3),Object('Obstacle',720,530,30,"brown",life=3),
                                Object('Obstacle',600,560,30,"brown",life=3),Object('Obstacle',720,560,30,"brown",life=3),
                                
                                Object('Obstacle',900,500,30,"brown",life=3),Object('Obstacle',930,500,30,"brown",life=3),
                                Object('Obstacle',960,500,30,"brown",life=3),Object('Obstacle',900,530,30,"brown",life=3),
                                Object('Obstacle',930,530,30,"brown",life=3),Object('Obstacle',960,530,30,"brown",life=3),
                                Object('Obstacle',990,500,30,"brown",life=3),Object('Obstacle',990,530,30,"brown",life=3),
                                Object('Obstacle',1020,500,30,"brown",life=3),Object('Obstacle',1020,530,30,"brown",life=3),
                                Object('Obstacle',900,560,30,"brown",life=3),Object('Obstacle',1020,560,30,"brown",life=3)])
            self.setScore(0)
            self.dx=self.dy=1
            canvas.delete('all')
            canvas.create_text(625,300,text="Vous avez perdu ...")
            canvas.create_text(625,320,text="Votre score est : "+str(self.getScore()))
            canvas.create_text(625,340,text="Pressez Entrer pour rejouer et echap pour quitter !")
            def click(event):
                if event.keysym == 'Return':
                    self.setUp(canvas)
                    return self
                elif event.keysym == 'Escape' or event.keysym == 'q':
                    pnd.destroy()
                    return self
            canvas.bind('<KeyPress>', click)
            
            
        def Tick(self, canvas:"Canvas Tkinter", pnd:'fenetre Tkinter') -> Game:
            """ Gère le rafraichissement du jeu toutes les 4 ??? """ 
            def click(event):
                """Effectue different action quand une touche du clavier est pressée"""
                if event.keysym == 'Left':
                    self.setSensSpaceShip(-1)
                    (dx,dy)=self.moveSpaceShip()
                    draw = self.getSpaceShip().getDraw()
                    canvas.move(draw,self.getSensSpaceShip()*dx,dy)
                elif event.keysym == 'Right':
                    self.setSensSpaceShip(1)
                    (dx,dy)=self.moveSpaceShip()
                    draw = self.getSpaceShip().getDraw()
                    canvas.move(draw,self.getSensSpaceShip()*dx,dy)
                elif event.keysym == 'F1':
                    spaceShip = self.getSpaceShip()
                    spaceShip.addLife()
                    numberLife=self.getTexts()['life']
                    numberLife.setDescription('Vie : '+str(spaceShip.getLife()))
                    canvas.itemconfig(numberLife.getDraw(), text=numberLife.getDescription())
                elif event.keysym == 'F12':
                    self.dx += 0.1
                    self.dy += 0.2
                    print(self.dx)
                elif event.keysym == 'F11':
                    self.dx -= 0.1
                    self.dy -= 0.2
                    if self.dx<1:
                        self.dx=self.dy=1
                    print(self.dx)
                elif event.keysym == 'q':
                    pnd.destroy()
            def shot(event):
                """Effectue differente action quand une touche du clavier est relachée"""
                if event.keysym == 'space':
                    self.createMissile(self.getSpaceShip().getX(), canvas)
            canvas.focus_set()
            canvas.bind('<KeyPress>',click)
            canvas.bind('<KeyRelease>', shot)
            
            if self.getSpaceShip().getLife()<=0: #Le vaisseau a t il toujours de la vie ?
                self.GameOver(canvas,pnd)

            if len(self.getAliens())<=0: #Reste t il des aliens ?
                self.setUp(canvas)
                self.addNiveau()
        #Gestion des mouvements 
            (dx, dy) = self.moveAliens()
            for alien in self.getAliens():
                draw = alien.getDraw()
                canvas.move(draw, dx, dy)
            (dx, dy) = self.moveMissiles()
            for missile in self.getMissiles():
                draw = missile.getDraw()
                canvas.move(draw, dx, dy)
            (dx, dy) = self.moveMissilesAliens()
            for missileAlien in self.getMissilesAliens():
                draw = missileAlien.getDraw()
                canvas.move(draw, dx, dy)
            (dx, dy) = self.moveAlienSpaceShips()
            for alienSpaceShip in self.getAlienSpaceShips():
                draw = alienSpaceShip.getDraw()
                canvas.move(draw, dx, dy)
            for obj in self.checkColision(canvas):
                self.removeObject(obj, canvas)

            if self.getScore()%50==0 and randint(0,1000)==0 and self.getAlienSSpass()==0:
                self.setAlienSSpass(1)
                self.createAlienSpacShip(canvas)

            if randint(0,100)==0 and len(self.getAlienSpaceShips())!=0:
                alien = self.getAlienSpaceShips()[randint(0,len(self.getAlienSpaceShips())-1)]
                self.createMissileAlien(alien.getX(),alien.getY(),canvas)
            
            if randint(0,250-self.getNiveau()*10)==0:
                alien = self.getAliens()[randint(0,len(self.getAliens())-1)]
                if alien.getScore()>10:
                    self.createMissileAlien(alien.getX(),alien.getY(),canvas)

        

            def recall():
                self.Tick(canvas,pnd)
        
            
            return canvas.after(4,recall)

        #Check collisions entre les extrémités du jeu et les aliens
        def checkWallColisionAliens(self) -> bool:
            for alien in self.getAliens():
                (x1, y1, x2, y2)=alien.getIdBox()
                if x1<=self.dx or y1<=self.dy or x2>=self.width-self.dx or y2>=self.height-self.dy:
                    
                    return False
            return True

       
        def checkColision(self, canvas:"Canvas Tkinter") -> list:
            """ Fonction chargée de gérer les collisions"""
            delete=[]

            #Check collision beetween Aliens and SpaceShip
            spaceShip = self.getSpaceShip()
            (x1s, y1s, x2s, y2s)=spaceShip.getIdBox()
            for alien in self.getAliens():
                (x1, y1, x2, y2)=alien.getIdBox()
                if y1s < y1:
                    spaceShip.setLife(0)
                    delete.append(spaceShip)

            #Check collision between Missiles, MissilesAliens and Obstacles
            for obstacle in self.getObstacles():
                (x1, y1, x2, y2)=obstacle.getIdBox()
                for missile in self.getMissiles()+self.getMissilesAliens():
                    (x1m, y1m, x2m, y2m)=missile.getIdBox()
                    if (x1 < x2m and x2 > x1m and y1 < y2m and y2 > y1m):
                        if obstacle.reduceLife()==0:
                            delete.append(obstacle)
                        if missile.reduceLife()==0:
                            delete.append(missile) 
                        #permet de changer la couleur de l'obstacle
                        obstacle.setColor(self.__color[obstacle.getLife()])
                        canvas.itemconfig(obstacle.getDraw(), fill=obstacle.getColor())         
            
            #Check collision between aliens and Missiles
            for alien in self.getAliens()+self.getAlienSpaceShips():
                (x1, y1, x2, y2)=alien.getIdBox()
                for missile in self.getMissiles():
                    (x1m, y1m, x2m, y2m)=missile.getIdBox()
                    if (x1 < x2m and x2 > x1m and y1 < y2m and y2 > y1m):
                        if alien.reduceLife()==0:
                            delete.append(alien)
                        if missile.reduceLife()==0:
                            delete.append(missile)
                        self.plusScore(alien.getScore())
                        self.setAlienSSpass(0)
            #Check collision between SpaceShip and MissilesAliens
            spaceShip = self.getSpaceShip()
            (x1, y1, x2, y2)=spaceShip.getIdBox()
            for missileAlien in self.getMissilesAliens():
                (x1m, y1m, x2m, y2m)=missileAlien.getIdBox()
                if (x1 < x2m and x2 > x1m and y1 < y2m and y2 > y1m):
                    if spaceShip.reduceLife()==0:
                        delete.append(spaceShip)
                    if missileAlien.reduceLife()==0:
                        delete.append(missileAlien)
                        
                    numberLife=self.getTexts()['life']
                    numberLife.setDescription('Vie : '+str(spaceShip.getLife()))
                    canvas.itemconfig(numberLife.getDraw(), text=numberLife.getDescription())

                    
            #Check collision between Missiles and Walls
            for missile in self.getMissiles():
                (x1, y1, x2, y2)=missile.getIdBox()
                if x1<=self.dx or y1<=self.dy or x2>=self.width-self.dx or y2>=self.height-self.dy:
                    delete.append(missile)

            #Check collision between MissilesAliens and Walls
            for missileAlien in self.getMissilesAliens():
                (x1, y1, x2, y2)=missileAlien.getIdBox()
                if x1<=self.dx or y1<=self.dy or x2>=self.width-self.dx or y2>=self.height-self.dy:
                    delete.append(missileAlien)

            #Check collision between AlienSpaceShips and Walls
            for alienSpaceShip in self.getAlienSpaceShips():
                (x1, y1, x2, y2)=alienSpaceShip.getIdBox()
                if x1<=self.dx or y1<=self.dy or x2>=self.width-self.dx or y2>=self.height-self.dy:
                    delete.append(alienSpaceShip)

            

            return delete



