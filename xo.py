import random
import os



# Graphic Function
def graphic(list_xo):
    xo = list_xo
    
    
    g = f"""
  {xo[0]} | {xo[1]} | {xo[2]}
  {xo[3]} | {xo[4]} | {xo[5]}
  {xo[6]} | {xo[7]} | {xo[8]}
    """
    print(g)


# Ai part
class Ai:

    def __init__(self,list_xo,my_):

        self.xo = list_xo
        self.moves_X = []
        self.moves_O = []
        self.win = ["123","456","789","147","258","369","753","159"]
        # AI 
        if my_ == "X":
            self.nut = "X"
            self.p = "O"
            self.ai_moves = self.moves_X
            self.p_moves = self.moves_O
        else:
            self.nut = "O"
            self.p = "X"
            self.ai_moves = self.moves_O         
            self.p_moves = self.moves_X

        # ===============
        self.moves()
        
        

    # Choose best move
    def choose(self):
        a1 = self.win_move()
        a2 = self.def_move()
        a3 = self.defend_moves()
        a4 = self.atack_moves()
        
        lis = []

        if a1 != None:
            return a1
        elif a2 != None:
            return a2
        elif a3 != [] and a4 != []:
            for a in a3:
                if  0 < a4.count(a):
                    lis.append(a)
            
            return random.choice(lis)
        elif a3 != [] :
            return random.choice(a3)

            
        else:
            return 5
            

        


    # Cheak all Moves (x,o)
    def moves(self):
        
        n = 1
        for x_o in self.xo:
            
            if x_o != " " and x_o == "X":
                self.moves_X.append(n)

            elif x_o != " " and x_o == "O":
                self.moves_O.append(n)
            n += 1

    # AI win move 
    def win_move(self):
        
       

        for win in self.win:

            find = 0
            for nut in self.ai_moves:
                
                
                nut=str(nut)
                win = list(win)

                if 0 < win.count(nut):
                    find = find + 1
                    win.remove(nut)
                    
                if find == 2 and self.xo[int(win[0])-1] != self.nut and self.xo[int(win[0])-1] != self.p:
                    return win[0]

    # Find The best defense
    def def_move(self):

        for win in self.win:

            find = 0
            for nut in self.p_moves:
                nut=str(nut)
                win = list(win)


                if 0 < win.count(nut):
                    find = find + 1
                    win.remove(nut)
                    
                    

                if find == 2 and self.xo[int(win[0])-1] != self.p and self.xo[int(win[0])-1] != self.nut:
                    return win[0]

    # All defend moves
    def defend_moves(self):
        list_def = []

        for win in self.win:
            
            for nut in self.p_moves:
                
                nut=str(nut)
                win = list(win)

                if 0 < win.count(nut):
                
                    win.remove(nut)

                    

                    for f in win:
                        
                        if self.xo[int(f)-1] == "X" or self.xo[int(f)-1] == "O":
                            break
                        else:
                            list_def.append(f)
                        
                    

        return list_def

    # Atack moves
    def atack_moves(self):
        list_def = []

        for win in self.win:
            
            for nut in self.ai_moves:
                
                nut=str(nut)
                win = list(win)

                if 0 < win.count(nut):
                
                    win.remove(nut)

                    for f in win:
                        
                        if self.xo[int(f)-1] == "X" or self.xo[int(f)-1] == "O":
                            break
                        else:
                            list_def.append(f)
                        
                    

        return list_def
#         1   2   3   4   5   6   7   8   9
ai = Ai( ["O","O"," "," ","X"," ","X"," "," "] , my_="X" )


class game:
    def __init__(self):
        
        self.p = "O"
        self.borad = [" "," "," "," "," "," "," "," "," "]
        self.ai = "X"
        
        self.rand = random.choice(["X","O"])
        self.turn = self.rand
        self.win_ = ["123","456","789","147","258","369","753","159"]
        while True:
            self.win()
            self.game()
        
    def win(self):
        
        for ox in self.win_:
            
            if self.borad[int(ox[0])-1] == self.ai and self.borad[int(ox[1])-1] == self.ai and self.borad[int(ox[2])-1] == self.ai:
                print(f"&&&&&&&&&&& Ai Win &&&&&&&&&&&&")
                graphic(self.borad)
                input()

            elif self.borad[int(ox[0])-1] == self.p and self.borad[int(ox[1])-1] == self.p and self.borad[int(ox[2])-1] == self.p :
                print(f"&&&&&&&&&&& You Win &&&&&&&&&&&&")
                graphic(self.borad)
                input()
                
            elif self.borad.count("X") + self.borad.count("O") == 9:
                print(f"&&&&&&&&&&& Draw &&&&&&&&&&&&")
                graphic(self.borad)
                input()               


            

    def game(self):
        
        
        if self.turn == self.p:
            grahic(self.borad)
            turn = input("Type (1,2,3,..): ")
            if self.borad[int(turn)-1] == "X" or self.borad[int(turn)-1] == "O":
                print("You cant")
                input()
            else:
                self.borad[int(turn)-1] = self.p
                self.turn = self.ai

        elif self.turn == self.ai:
            ai = Ai(self.borad, my_=self.ai)
            self.borad[int(ai.choose())-1] = self.ai  
            self.turn = self.p         

        os.system("cls")       

game()
        



input()
