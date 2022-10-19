'''
Create the ping_pong game that restart everytime the ball hit the ring. 
'''

import pygame, sys , random
from pygame import mixer 
pygame.init()
mixer.init()
clock = pygame.time.Clock()

width,height = 800, 576   

red = (202,0,0)

screen = pygame.display.set_mode((width, height))

class BLOCK(pygame.sprite.Sprite) :
    def __init__(self, path, posx, posy):
        super().__init__()
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(midbottom = (posx,posy))

class BIRD(BLOCK) :
    def __init__(self, path, posx, posy,pipe):
        super().__init__(path, posx, posy)
        self.pipe = pipe 
        self.move = 0.25
        self.run = True
        self.Playerscore = 0 
    def moveBird(self) :
        self.move += 0.25
        self.rect.y += self.move
    def collision(self) :
        for pipe in self.pipe.list : 
            if pygame.Rect.colliderect(pipe,self.rect) :
                pygame.mixer.music.load(r'C:\T\.vscode\T\die.wav')
                pygame.mixer.music.play()
                self.run = False 
    def score(self) :            
        for pipe in self.pipe.list :
            if self.rect.centerx == pipe.right or self.rect.centerx == pipe.right + 1:
                self.Playerscore += 0.5
                pygame.mixer.music.load(r'C:\T\.vscode\T\point.wav')      
                pygame.mixer.music.play()
    def restrain(self) :
        if self.rect.y >= height or self.rect.y <= 0 :
            pygame.mixer.music.load(r'C:\T\.vscode\T\die.wav')
            pygame.mixer.music.play()
            self.run = False
    def update(self) :
        if self.run :
            self.moveBird() 
            self.collision()
            self.score()
            self.restrain()  

class Pipe :
    def __init__(self,image) :
        self.position = 576
        self.list = []
        self.image = image
        self.image = pygame.transform.scale2x(self.image)
    def getRect(self) :
        bottomPipe = [1100,1150,1200]
        pipeBottom = self.image.get_rect(midbottom = (self.position,random.choice(bottomPipe)))
        topPipe = [-450,-500,-550]
        pipeTop = self.image.get_rect(midtop = (self.position,random.choice(topPipe)))
        return pipeBottom, pipeTop 
    def movePipe(self) :
        for pipe in self.list :pipe.x -= 1 
        return self.list 
    def spawnPipe(self) :
        for pipe in self.list :
            if pipe.bottom < 1000 :
                image = pygame.transform.flip(self.image,False,True)
                screen.blit(image,pipe)
            else :screen.blit(self.image,pipe)
    def remove(self) :
        for pipe in self.list :
            if pipe.right <= 0 :self.list.remove(pipe)
    def update(self) :
        self.movePipe()
        self.list = self.movePipe()
        self.spawnPipe()
        self.remove()

class SCREEN :
    def __init__(self,image,pos1,pos2) :
        self.pos1 = pos1 
        self.pos2 = pos2 
        self.image = image 
        self.image = pygame.transform.scale2x(self.image)
    def display(self) :
        screen.blit(self.image,(self.pos1,0))
        screen.blit(self.image,(self.pos2,0))
    def move(self) :
        self.pos1 -=1 
        self.pos2 -= 1
        if self.pos1 <= -576 :
            self.pos1 = 0 
            self.pos2 = 576 
    def update(self) :
        self.move()
        self.display()

class gameManager() : 
    def __init__(self,font,color,pause,countinue,pipe,loss):
        self.pipe = pipe 
        self.x,self.y = 0 ,0
        self.font = font
        self.color = color 
        self.pause = pygame.image.load(pause)
        self.Countinue = pygame.image.load(countinue)
        self.loss = pygame.image.load(loss)
        self.gamefont= pygame.font.Font(self.font,32)
        self.score = 0 
        self.displayScore = False
        self.stop = False
    def run(self) :
        if bird.run == False :
            self.displayScore = True 
            pipe.list.clear() 
            Screen.update()
            self.showlost()
            bird.rect.y = height/2
            if self.displayScore :
                self.bestScore()
                self.displayScore = False
                bird.move = 0 
        if bird.run :
            if self.stop : 
                self.drawCountinue()
                self.countinue()
            else :
                self.Pause() 
                Screen.update()
                pipe.update()
                birdGroup.draw(screen)
                birdGroup.update()
                self.drawPause()
                self.showscore()
        self.showhighestScore()
    def showlost(self) :
        lostrect = self.loss.get_rect(center = (width/2,height/2))
        screen.blit(self.loss,lostrect)
    def showscore(self) :
        playerscore = self.gamefont.render(str(int(bird.Playerscore)),True,self.color)
        playerscorerect = playerscore.get_rect(center = (width - 26,height/2 -50))
        screen.blit(playerscore,playerscorerect)
    def showhighestScore(self) :
        highscore = self.gamefont.render(str("highest score :" + str(int(self.score))),True,self.color)
        highscorerect = highscore.get_rect(center = (width/2,height/4))
        screen.blit(highscore,highscorerect)
    def bestScore(self) :
        if bird.Playerscore > self.score :self.score = bird.Playerscore
    def Pause(self) :
        if width - 75 <self.x < width -25 and height - 725 > self.y > height -775  :
            self.stop = True
            self.x,self.y = 0,0 
    def countinue(self)  :
        if width - 75 <self.x < width -25 and height - 725 > self.y > height -775  :
            self.stop = False 
            self.x, self.y = 0,0 
    def drawPause(self) :
        Pause = self.pause.get_rect(center = (width - 50, height - 750))
        screen.blit(self.pause,Pause)
    def drawCountinue(self) :
        countinuerect =self.Countinue.get_rect(center = (width - 50, height - 750))
        screen.blit(self.Countinue,countinuerect) 

spawnColumn = pygame.USEREVENT
pygame.time.set_timer(spawnColumn,1200)

#Group 
Screen = SCREEN(pygame.image.load(r'C:\T\.vscode\T\background.png').convert(),0,576)
pipe = Pipe(pygame.image.load(r'C:\T\.vscode\T\pipe.png').convert()) 
bird = BIRD(r'C:\T\.vscode\T\yellowbirdDownflap.png',(width-126)/2,height/2,pipe)
birdGroup = pygame.sprite.GroupSingle()
birdGroup.add(bird)
gamemanager = gameManager("freesansbold.ttf",red,r'C:\T\.vscode\T\pause.png',r'C:\T\.vscode\T\countinue.png',pipe,r'C:\T\.vscode\T\lose.png')   

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                bird.move = 0 
                bird.move -= 10 
            if event.key == pygame.K_k :
                bird.run = True 
                bird.Playerscore = 0 
        if event.type == spawnColumn :
            if gamemanager.stop == False : pipe.list.extend(pipe.getRect())
        if event.type == pygame.MOUSEBUTTONDOWN :
            gamemanager.x,gamemanager.y = pygame.mouse.get_pos()
    gamemanager.run()
    pygame.display.flip()
    clock.tick(60)
