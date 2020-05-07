import cherrypy
import sys
from cherrypy.lib.static import serve_file
import copy
import random
class arbre:
    def __init__(self, grille, pion, pionadversaire):
        self.liste = grille
        self.pion = pion
        self.pionadversaire= pionadversaire
        self.direction= [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    def possiblemove(self):
        liste=[]
        for ligne in range(9):
            for colonne in range(9):
                for elem in self.direction:
                    move={}
                    if ligne+elem[0]>=0 and colonne+elem[1] >=0:
                        try:
                            if len(self.liste[ligne][colonne])!=0 and len(self.liste[ligne+elem[0]][colonne+elem[1]]) !=0:
                                if len(self.liste[ligne][colonne])+len(self.liste[ligne+elem[0]][colonne+elem[1]]) <=5:
                                    move["from"]=[ligne,colonne]
                                    move["to"] = [ligne+elem[0],colonne+elem[1]]
                                    liste.append(move)
                        except IndexError:
                            pass
        
        return liste
    
    def equalsmoves(self):
        liste= self.possiblemove()
        for elem in liste:
            grid=copy.deepcopy(self.liste)
            ligne1=elem["from"][0]
            colonne1=elem["from"][1]
            ligne2=elem["to"][0]
            colonne2=elem["to"][1]
            grid[ligne2][colonne2] += grid[ligne1][colonne1]
            grid[ligne1][colonne1] = []
            elem["score"] = self.score(grid)
        return liste

    def DoMove(self):
        bestlist=[]
        bestlist2=[]
        bestlist3=[]
        bestlist4=[]
        self.goodlist=[]
        scoreA=self.score(self.liste)[0]
        scoreB=self.score(self.liste)[1]
        for elem in self.equalsmoves():
            if elem["score"][0] > scoreA:
                bestlist.append(elem)
                if self.liste[elem["to"][0]][elem["to"][1]] == self.pionadversaire:
                    bestlist2.append(elem)
                if elem["score"][0] >= scoreA+2:
                    bestlist3.append(elem)
                if elem["score"][0] >= scoreA+3:
                    bestlist4.append(elem)

            if elem["score"][1] == scoreB:
                self.goodlist.append(elem)
        if len(bestlist4)!=0:
            move=random.choice(bestlist4)
        if len(bestlist3)!= 0 and len(bestlist4)==0:
            move=random.choice(bestlist3)
        if len(bestlist2)!=0 and len(bestlist3)==0 and len(bestlist4)==0:
            move=random.choice(bestlist2)
        if len(bestlist)!=0 and len(bestlist2)==0 and len(bestlist3)==0 and len(bestlist4)==0:
            move=random.choice(bestlist)
        if len(self.goodlist)!=0 and len(bestlist)==0 and len(bestlist2)==0 and len(bestlist3)==0 and len(bestlist4)==0:
            self.goodlist2=[]
            move=random.choice(self.goodlist)
            for elem in self.goodlist:
                if self.notgoodmove(elem)==False:
                    self.goodlist2.append(elem)
            if len(self.goodlist2) != 0:
                move=random.choice(self.goodlist2)



        if len(self.goodlist)==0 and len(bestlist)==0 and len(bestlist2)==0 and len(bestlist3)==0 and len(bestlist4)==0:
            move=random.choice(self.equalsmoves())
            with open('text.txt','a')as file:
                file.write(str(move))

        return move
    def notgoodmove(self, move):
        grid=copy.deepcopy(self.liste)
        ligne1=move["from"][0]
        colonne1=move["from"][1]
        ligne2=move["to"][0]
        colonne2=move["to"][1]
        grid[ligne2][colonne2] += grid[ligne1][colonne1]
        grid[ligne1][colonne1] = []
        for direction in self.direction:
            try :
                if ligne2+direction[0]>=0 and colonne2+direction[1]>= 0:
                    if grid[ligne2+direction[0]][colonne2+direction[1]][-1]== self.pionadversaire and len(grid[ligne2][colonne2])+len(grid[ligne2+direction[0]][colonne2+direction[1]])==5:
                        return True
            except IndexError:
                pass
        return False
        
    def score(self, liste):
        scoreA=0
        scoreB=0
        
        for ligne in range(9):
            for colonne in range(9):
                if len(liste[ligne][colonne])==5:
                       if liste[ligne][colonne][-1] == self.pion:
                           scoreA+=1
                       if liste[ligne][colonne][-1] == self.pionadversaire:
                           scoreB+=1
                if len(liste[ligne][colonne])!=5:
                    compteur=0
                    for direction in self.direction:
                        
                        if ligne+direction[0] >=0 and colonne+direction[1]>=0:
                            try:
                                if liste[ligne][colonne][-1] == self.pion:
                                    if  len(liste[ligne][colonne])+len(liste[ligne+direction[0]][colonne+direction[1]]) >5 or len(liste[ligne+direction[0]][colonne+direction[1]])==0:
                                        compteur+=1
                                if liste[ligne][colonne][-1] == self.pionadversaire:
                                    if  len(liste[ligne][colonne])+len(liste[ligne+direction[0]][colonne+direction[1]]) >5 or len(liste[ligne+direction[0]][colonne+direction[1]])==0:
                                        compteur+=1
                            except IndexError:
                                compteur+=1
                        if ligne+direction[0] <0 or colonne+direction[1]<0:
                            compteur+=1
                        
                        if compteur == 8 and len(liste[ligne][colonne])!=0:
                            if liste[ligne][colonne][-1] == self.pion:
                                scoreA+=1
                            if liste[ligne][colonne][-1] == self.pionadversaire:
                                scoreB+=1
        return scoreA,scoreB    



class Server:
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # Deal with CORS
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        if cherrypy.request.method == "OPTIONS":
            return ''
        pion=1
        pionadversaire=0
        #pionadversaire=0
        body = cherrypy.request.json
        if body["players"][0]==body["you"]:
            pion=0
            pionadversaire=1
        MeruemSama = arbre(body["game"], pion, pionadversaire)
        Move = MeruemSama.DoMove()
        listemessages = ['you can do it (or not) !',"KAHHH MEEEE HAAAA MEEEE HAAAAAAA !!!","ooyoooo je t'ai eu", "tu joues comme une mauviette :("," ... ","encore un peu", " j'ai gagné :)"]
        i=(Move["score"][0]-Move["score"][1])
        message=random.choice(["salut "+ str(body["players"][pionadversaire])])
        if i>=0 and len(MeruemSama.possiblemove())<270:
            try: 
                message= listemessages[i]
            except IndexError:
                message= "assez joué"
        if i < 0:
            message='tu crains :(, laisse moi gagner'
        
        return {
            "move": {"from":Move["from"],
            "to": Move["to"]},
            "message": message
            }
        
    @cherrypy.expose
    def ping(self):
        return "pong"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=9090

    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': port})
    cherrypy.quickstart(Server())