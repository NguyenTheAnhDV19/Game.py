#Just watch this from another youtuber and change a bit of method. Could've had better end_game and restart_game but do not care enough to do such a thing.
#I do think using sprite is a bit unessential and messy with its group and stuff but just dont want to change it cause i have another thing more interesting to do. At least more than these. 

import pygame,sys 
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init() 
clock= pygame.time.Clock()  

width = 1280  
height = 800
grey = (200,200,200)

gamefont= pygame.font.Font("freesansbold.ttf",32)

class block(pygame.sprite.Sprite) :
    def __init__(self,path,posx,posy) :
        super().__init__() 
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (posx,posy))

class PLAYER1(block) :
    def __init__(self, path, posx,posy) :
        super().__init__(path,posx,posy)  
        self.movement = 0 
    def constrain(self) :
        if self.rect.top <= 0 :
            self.rect.top = 0 
        if self.rect.bottom >= height :
            self.rect.bottom = height 
    def update(self) :
        self.rect.y += self.movement
        self.constrain()

class PLAYER2(block) :
    def __init__(self, path,posx,posy):
        super().__init__(path,posx,posy)
    def constrain(self) :
        if self.rect.top <=0 :
            self.rect.top = 0 
        if self.rect.bottom >= height :
            self.rect.bottom = height 
    def update(self,ball_group) :
        if self.rect.top > ball_group.sprite.rect.y :
            self.rect.y -= 7 
        if self.rect.bottom < ball_group.sprite.rect.y :
            self.rect.y += 7
        self.constrain()

class BALL(block) :
    def __init__(self, path, posx, posy, paddle):
        super().__init__(path, posx, posy)
        self.movementx = 7 
        self.movementy = 7
        self.scoretime = 0
        self.active = False 
        self.paddle = paddle 
    def constrain(self) :
        if self.rect.top <= 0 or self.rect.bottom >= height :
            self.movementy *= -1 
        if self.rect.left <= 0 :
            self.scoretime = pygame.time.get_ticks()
        if self.rect.right >= width :
            self.scoretime = pygame.time.get_ticks()  
    def update(self) :
        if self.active :
            self.constrain()
            self.rect.x += self.movementx
            self.rect.y += self.movementy
            self.collision()
        else :
            self.restart()
    def collision(self) :
        if pygame.sprite.spritecollide(self,self.paddle,False) :
            cpaddle = pygame.sprite.spritecollide(self,self.paddle,False)[0].rect
            if abs(self.rect.right - cpaddle.left) <10 and self.movementx >0 :
                self.movementx *= -1 
            if abs(self.rect.top - cpaddle.bottom) <10 and self.movementy <0 :
                self.movementy *= -1 
            if abs(self.rect.bottom - cpaddle.top) <10 and self.movementy >0 :
                self.movementy *= -1 
            if abs(self.rect.left - cpaddle.right) <10 and self.movementy <0 :
                self.movementx *= -1 
    def reset(self) :
        self.active = False 
        self.scoretime = pygame.time.get_ticks()
        self.rect.center = (width/2-10,height/2-10)
    def restart(self) :
        currenttime = pygame.time.get_ticks()
        count = 3 
        if currenttime - self.scoretime <= 700 :
            count = 3
        if 700 < currenttime - self.scoretime <= 1400 :
            count = 2 
        if 1400 < currenttime - self.scoretime <= 2100 :
            count = 1 
        if currenttime - self.scoretime > 2100 :
            self.active = True 
        
        timecount = gamefont.render(str(count),True,grey)
        timecountrect = timecount.get_rect(center = (width/2,height/2+50))
        screen.blit(timecount,timecountrect)

class gameManager :
    def __init__(self,ball_group,paddle_group) :
        self.player1Score = 0 
        self.player2Score = 0 
        self.ball_group = ball_group
        self.paddle_group = paddle_group
    def run(self) :
        player1_group.update()
        player1_group.draw(screen)
        ball_group.draw(screen)
        ball_group.update()
        player2group.update(ball_group)
        player2group.draw(screen)
        self.resetBall()
        self.writeScore()
    def resetBall(self) :
        if self.ball_group.sprite.rect.right >= width :
            self.player2Score += 1 
            self.ball_group.sprite.reset()
        if self.ball_group.sprite.rect.left <= 0 :
            self.ball_group.sprite.reset()
            self.player1Score += 1
    def writeScore(self) :
        player1Score = gamefont.render(str(self.player1Score),True,grey)
        player1Rect = player1Score.get_rect(center = (width /2 + 40, height/2))
        screen.blit(player1Score,player1Rect)
        player2Score = gamefont.render(str(self.player2Score),True,grey)
        player2Rect = player2Score.get_rect(center = (width /2 - 40 ,height/2))
        screen.blit(player2Score,player2Rect)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong game")

Player1 = PLAYER1(r'C:\T\.vscode\T\Paddle.png',width-20, height /2 -70)
player1_group = pygame.sprite.Group()
player1_group.add(Player1)
Player2 = PLAYER2(r'C:\T\.vscode\T\Paddle.png',10,height/2-70)
player2group = pygame.sprite.Group()
player2group.add(Player2)
cpaddle = pygame.sprite.Group()
cpaddle.add(Player1)
cpaddle.add(Player2)
Ball = BALL(r'C:\T\.vscode\T\Ball.png',width/2-10,height/2-10,cpaddle)
ball_group = pygame.sprite.GroupSingle()
ball_group.add(Ball)
gamemanager = gameManager(ball_group,cpaddle)

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit() 
            sys.exit()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_DOWN :
                Player1.movement += 7
            if event.key == pygame.K_UP :
                Player1.movement -= 7
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_DOWN :
                Player1.movement -= 7
            if event.key == pygame.K_UP :
                Player1.movement += 7
            

    screen.fill((100,100,100))

    gamemanager.run()

    pygame.draw.aaline(screen,grey,(width/2,0),(width/2,height))
    pygame.display.flip()
    clock.tick(60)
