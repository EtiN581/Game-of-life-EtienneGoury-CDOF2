import random
import os
import time
#maybe graphical interface ?

width=30
height=10
nbiter=10
#False : dead/no cell
#True : alive cell

#une cellule morte possédant exactement trois cellules voisines vivantes devient vivante (elle naît)
#une cellule vivante possédant deux ou trois cellules voisines vivantes le reste, sinon elle meurt.

def count_neighbors(x,y):
    k=0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if 0<=i<width and 0<=j<height and (i!=x or j!=y):
                if space[i][j]:
                    k+=1
    return k

def updateCell(x,y):
    k=count_neighbors(x, y)
    state=space[x][y]
    if (not state and k==3) or (state and (k==2 or k==3)):
        newSpace[x][y]=True
        
def printSpace():
    s=""
    for j in range(height):
        line=""
        for i in range(width):
            s+= "#" if space[i][j] else " "
        s+="\n"+line
    os.system('cls') #clear terminal
    print(s)
        
def initSpace():
    return [[True if random.random()<0.5 else False for _ in range(height)] for _ in range(width)]

space=initSpace()
for _ in range(nbiter):
    newSpace=[[False for _ in range(height)] for _ in range(width)]
    for x in range(width):
        for y in range(height):
            updateCell(x, y)
    space=[[newSpace[i][j] for j in range(height)] for i in range(width)]
    printSpace()
    time.sleep(1) #freeze for 1s to have time to see before clearing the terminal