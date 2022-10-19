'''
Because the left_right movement demand exact amount of space which is 40 to perform properly. Lead to the fact that one have to use the big amount of time delay to 
prevent too much movement. Hence make the program run kind of glitch and unefficent.
Beside that, one's just to lazy to even make the alright end_game and restart_game method() nor add sound and background picture. 
And the check_line() method looks kind of messy.
Another fact is that one could use the numpy.array to make the program run more smoothly. But for now one just have much more work to do and loose interest in this project.
'''

from copy import deepcopy
import pygame,sys,random

width = 400 
height = 600 

screen = pygame.display.set_mode((width,height))

#Create grid : 
grid = [pygame.Rect(x*40,y*40,40,40) for x in range(10) for y in range(15)]

#fingure : 
L = [(1,0),(1,1),(1,2),(2,1)]
_ = [(1,0),(2,0),(3,0),(4,0)]
R = [(1,0),(1,1),(2,0),(2,1)]
T = [(1,0),(1,1),(1,2),(2,1)]
Z = [(2,0),(1,1),(2,1),(1,2)]

fingure = T,Z,L,R,_

#color 
color = (255,255,255),(0,255,255),(0,255,0),(0,0,255),(255,0,0)

#delay 
clock = pygame.time.Clock()

#main 
class Main :
    def __init__(self) -> None:
        self.fingure = [pygame.Rect(rect[0]*40,rect[1]*40,40,40) for rect in random.choice(deepcopy(fingure))]
        self.color = random.choice(color)
        self.board = []
        self.fall = 20
        self.move_right_left = 0
    def draw_fingure(self) :
        color_ = (255,0,0)
        [pygame.draw.rect(screen,self.color,coor) for coor in self.fingure]
        [pygame.draw.rect(screen,color_,coor) for coor in self.board]
    def fall_down(self) :
        fingure = deepcopy(self.fingure)
        for rect in self.fingure :
            rect.y += self.fall
            if self.check_fall_fingure() :
                self.board.extend(fingure)
                self.new_fingure()
                break 
    def move_horientially(self) :
        fingure = deepcopy(self.fingure)
        for rect in self.fingure :
            rect.x += self.move_right_left
            if self.check_fall_fingure() :
                self.fingure = fingure 
                break 
            if rect.x < -1 or rect.x > width - 39 :
                self.fingure = fingure 
                break
    def check_fall_fingure(self) :
        for rect in self.fingure :
            if rect.bottom > height  : return True 
            for board in self.board :
                if rect.bottom > board.top and rect.x == board.x : return True 
        return False 
    def new_fingure(self) :
        self.color = random.choice(color)
        self.fingure =  [pygame.Rect(rect[0]*40,rect[1]*40,40,40) for rect in random.choice(deepcopy(fingure))]
    def check_line(self) :
        list = []
        for y in range(15) :
            for board in self.board :
                if board.y == y*40 : list.append(board) 
            if len(list) == 10 : 
                for rect in list : 
                    self.board.remove(rect)
                self.fall_board_check(y)
            list =[]
    def fall_board_check(self,y) :
        for rect in self.board :
            if rect.y <= (y*40) : 
                rect.y += 40 
    def rotate(self) :
        fingure = deepcopy(self.fingure)
        for rect in self.fingure :
            x = rect.y - self.fingure[0].y 
            y = rect.x - self.fingure[0].x 
            rect.x = self.fingure[0].x -x 
            rect.y = self.fingure[0].y +y 
            if self.check_fall_fingure() :
                self.fingure = fingure
                break 
            if rect.x < -1 or rect.x > width - 39 :
                self.fingure = fingure 
                break
    def game_over(self) :
        for rect in self.board : 
            if rect.y <= 0 : return True 
        return False 
    def start_new_game(self) :
        if self.game_over() :
            self.board.clear() 
    def run(self) :
        self.draw_fingure() 
        self.fall_down()
        self.move_horientially()
        self.check_line()
        self.start_new_game()

main = Main()

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : 
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT : main.move_right_left += 40
            if event.key == pygame.K_LEFT  : main.move_right_left -= 40
            if event.key == pygame.K_DOWN  : main.fall += 0
            if event.key == pygame.K_SPACE : main.rotate()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT : main.move_right_left -= 40
            if event.key == pygame.K_LEFT  : main.move_right_left += 40
            if event.key == pygame.K_DOWN  : main.fall -= 0
    screen.fill((0,0,0))
    main.run()
    [pygame.draw.rect(screen,(255,255,255),coor,1)for coor in grid]
    pygame.time.delay(60)
    pygame.display.update()
