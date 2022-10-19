# what a mess. But do not have intention to put these into class. 

import pygame, sys
import numpy as np
from pygame.constants import K_0 

pygame.init()

#Colour : (Red, Green, White)
Grey = (100,100,100)
Red = (255,0, 0)
Green=(0,255,0)
White = (0,0,255)

# width and height of the board :
width = 500 
height = 500 

# cordinate :
cordinate1 = 100
cordinate2 = 200
cordinate3 = 300 
cordinate4 = 400
#Function to draw a board :
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("GAME TIC TOC TOE")
display.fill(Grey)

#Function to draw a line :
def draw_line() :
   # The first vertical line :
   pygame.draw.line(display,Green,(0, cordinate1),(500, cordinate1), 10)
   # The second vertical line :
   pygame.draw.line(display,Green,( 0,cordinate2),(500,cordinate2), 10)
   #The third vertical line :
   pygame.draw.line(display,Green,( 0,cordinate3),(500,cordinate3), 10)
   #The forth vertical line :
   pygame.draw.line(display,Green,( 0,cordinate4),(500,cordinate4), 10)

   # The first horizental line :
   pygame.draw.line(display,Green,(cordinate1, 0),(cordinate1, 500), 10)

   pygame.draw.line(display,Green,( cordinate2, 0),(cordinate2, 500), 10)

   pygame.draw.line(display,Green,(cordinate3, 0),(cordinate3, 500), 10)

   pygame.draw.line(display,Green,(cordinate4, 0),(cordinate4, 500), 10)

#Set value for row and col in board :
row_len = 5 
col_len = 5 


# Set matrix fill with 0 for board :
board = np.full((row_len, col_len), 0)

#function to mark the square :
def mark_square(row,col,play) :
    board[row][col] = play 

def is_square_available(row,col) :
    return board[row][col] ==0 

def draw_fingure() :
    for row in range(row_len) :
        for col in range(col_len) :
            if board[row][col] == 1 :
                pygame.draw.circle(display,Red,(int(row*100 + 50),int(col*100 +50)),30,10)
            elif board[row][col] == 2:
                pygame.draw.line(display,White,(row* 100+ 30,col*100 +30),(row*100 +100 -30,col* 100 +100 -30 ), 10)
                pygame.draw.line(display,White,(row* 100+ 30,col *100 +100 -30),(row * 100 +100 - 30, col * 100 +30 ), 10)
def draw_vertical_line(row,play) :
    if play == 1 :
        colour = Red 
    elif play == 2 :
        colour = White 
    pygame.draw.line(display,colour,(row*100+ 50,50),(row*100 +50,500- 50),10)

def draw_horizontial_line(col,play) :
    if play == 1 :
        colour = Red 
    elif play == 2 :
        colour = White 
    pygame.draw.line(display,colour,(50,col * 100 + 50),(500- 50,col * 100 +50),10)

def draw_diagnol_line1() :
    if play == 1 :
        colour = Red 
    elif play == 2 :
        colour = White
    pygame.draw.line(display,colour,(50,50),(500 - 50, 500 - 50), 10)
    
def draw_diagnol_line2() :
    if play == 1 :
        colour = Red 
    elif play == 2 :
        colour = White 
    pygame.draw.line(display, colour,(50, 500 - 50),(500 - 50, 50), 10)

def check_win() :
    for row in range (row_len) :
        if board[row][0] == play and board[row][1] == play and board[row][2] == play and board[row][3] == play and board[row][4] == play :
            draw_vertical_line(row,play)
            return True 
    for col in range(col_len) :
        if board[0][col] == play and board[1][col] == play and board[2][col] == play and board[3][col] == play and board[4][col] == play :
            draw_horizontial_line(col,play)
            return True 
    if board[0][0] == play and board[1][1] == play and board[2][2] == play and board[3][3] == play and board[4][4] == play :
            draw_diagnol_line1()
            return True 
    if board[0][4] == play and board[1][3] == play and board[2][2] == play and board[3][1] == play and board[0][4] == play :
            draw_diagnol_line2()
            return True 

def restart() :
   display = pygame.display.set_mode((width, height))
   pygame.display.set_caption("GAME TIC TOC TOE")
   display.fill(Grey)
   draw_line()
   for row in range(row_len) :
      for col in range(col_len) :
         board[row][col] = 0 

play = 1 
end_game = False


while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
        draw_line()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not end_game :
            X = event.pos[0]
            Y = event.pos[1]
        
            click_row = int(X // 100)
            click_col = int(Y // 100)

            if is_square_available(click_row, click_col) :
                if play == 1 :
                    mark_square(click_row,click_col , 1 )
                    if check_win() :
                       end_game = True 
                    
                    play = 2 
            
                elif play == 2 :
                    mark_square(click_row,click_col, 2)
                    if check_win() :
                       end_game = True 
                    
                    play = 1 
                draw_fingure()

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE or event.key == pygame.K_BACKSPACE :
               restart()
               play = 1 
               end_game = False
    
    pygame.display.update()
