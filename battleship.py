from random import randint
"""
Battleship Project
Name:MEHBUB
Roll No:
"""

import battleship_tests as test
project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["rows"]=10
    data["cols"]=10
    data["boardsize"]=500
    data["cellsize"]=50
    data["numships"]=5
    data["Computerboard"]=[[]]
    data["Userboard"]=[[]]
    data["Computerboard"]=emptyGrid(data["rows"],data["cols"])
    data["Userboard"]=emptyGrid(data["rows"],data["cols"])
    data["Computerboard"]=addShips(data["Computerboard"],data["numships"])
    data["Userboard"]=addShips(data["Userboard"],data["numships"])
    return
# rows=10
    # columns=10
    # boardsize=500
    # cellsize=50
    # numships=5
    

'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,userCanvas,data["Userboard"],True) # grid for userboard
    drawGrid(data,compCanvas,data["Computerboard"],True) # grid for computerboard
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid=[]
    for i in range(rows):
        columnlist = []
        for j in range(cols):
            columnlist.append(EMPTY_UNCLICKED)
        grid.append(columnlist)
    return grid


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    row=randint(1,8)
    cols=randint(1,8)
    direction=randint(0,1)
    if(direction==1):
        c1=[]                    
        for i in range(row-1,row+2,1):
            c1.append([i,cols])
    else:
        c1=[]       
        for i in range(cols-1,cols+2,1):
            c1.append([row,i])
    return c1
    

'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship): 
    for i in range(len(ship)):
        if grid[ship[i][0]][ship[i][1]]!=EMPTY_UNCLICKED:
            return False
    return True
'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    count=0
    while count<numShips:
        ship=createShip() # ship variable is assigned with the create ship function
        if (checkShip(grid,ship)):
            for i in range(len(ship)):
                grid[ship[i][0]][ship[i][1]]=SHIP_UNCLICKED
            count+=1
    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for i in range(0,data["rows"],1):
        for j in range(0,data["cols"],1):
                x1=data["cellsize"]*j
                y1=data["cellsize"]*i
                x2=x1+data["cellsize"]
                y2=y1+data["cellsize"]
                canvas.create_rectangle(x1,y1,x2,y2,outline='black',fill='blue')
                if(grid[i][j]==SHIP_UNCLICKED):
                    x3=data["cellsize"]*j
                    y3=data["cellsize"]*i
                    x4=x3+data["cellsize"]
                    y4=y3+data["cellsize"]
                    canvas.create_rectangle(x3,y3,x4,y4,outline='black',fill='yellow')

    return

    #grid=canvas.create_rectangle(data["rows"],data["columns"])
    # row=data["rows" and "cols"]
    # column=data["rows" and "cols"]
    # cell=data["cellsize"]
    # for i in range(data["rows" and "cols"]):
    #     for j in range(data["rows" and "cols"]):
    #         # if showShips==True:
    #         #     x='yellow'
            
            
    #         if grid[i][j]==SHIP_UNCLICKED:
                
    #             canvas.create_rectangle(x1,y1,x3,y3,outline='black',
    #             fill="blue") 
    #         x1=50*j 
    #         x3=x1+50
    #         y1=50*i 
    #         y3=y1+50    
               
    #     canvas.create_rectangle(x1,y1,x3,y3,outline='black')
    # return        
    # for i in grid:
    #     if (grid[[i][0]][i[i][1]]==SHIP_UNCLICKED):
    #         grid=canvas.create_rectangle(data["boardsize"],data["cellsize"],fill="yellow")
    #     else:
    #         grid=canvas.create_rectangle(data["boardsize"],data["cellsize"],fill="blue")
    


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    return


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    return


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
     return [int(event.y/data["cellsize"]),int(event.x/data["cellsize"])]


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    return


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    return


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    test.testGetClickedCell()
    #test.testGrid()
    #test.testDrawGrid()
    #test.week1Tests()

    #test.testMakeModel()
    #test.testEmptyGrid() 
    #test.testCreateShip()
    #test.testCheckShip()
    #test.testAddShips()
    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)