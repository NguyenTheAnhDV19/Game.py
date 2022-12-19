import pygame,sys,random

width,height = 800,700
screen_color,ball_color,stick_color,hole_color = (150,250,0),(120,40,90),(255,125,255),(0,0,0)

screen = pygame.display.set_mode((width,height))

class ball :
     def __init__(self, Hole) -> None:
          self.hole = Hole
          self.color = ball_color
          self.position = [400,500]
          self.movement = [0,0]
     def draw(self):
          pygame.draw.circle(screen,self.color,(self.position[0],self.position[1]),15)

     def reduce(self):
          while self.movement[0] >60 or self.movement[0] < -60 or self.movement[1] >60 or self.movement[1] < -60:
               self.movement[0] /= 1.2
               self.movement[1] /= 1.2
              
          self.movement[0] /= 1.1
          self.movement[1] /= 1.1

          if  0 < self.movement[0] < 0.1 or -0.1 < self.movement[0] < 0 : self.movement[0] = 0
          if  0 < self.movement[1] < 0.1 or -0.1 < self.movement[1] < 0 : self.movement[1] = 0

     def move(self):
          self.position[0] += self.movement[0]
          self.position[1] += self.movement[1]

     def bounce(self) :
          if self.position[0] <= 0 or self.position[0] >= width : self.movement[0] *= -1 
          if self.position[1] <= 0 or self.position[1] >= height : self.movement[1] *= -1 

     def fall(self) :
          if self.hole.position[0] - 10 <= self.position[0] <= self.hole.position[0] + 10 :
               if self.hole.position[1] - 10 <= self.position[1] <= self.hole.position[1] + 10 :
                    return True 
          return False 

     def reappear(self):
          if self.fall() :
               self.position[0] = random.randrange(15,width-15)
               self.position[1] = random.randrange(15,height-15)
               self.movement = [0,0]

     def win(self):
          if self.fall() == True :
               pass 

     def update(self):
          self.draw()
          self.reduce()
          self.move()
          self.bounce()
          self.reappear()
         

class stick :
     def __init__(self) -> None:
          pass
     def draw(self):
          pass
     
class block :
     def __init__(self) -> None:
          pass
     def draw(self):
          pass 

class hole :
     def __init__(self) -> None:
          self.color = hole_color
          self.position = (400,400)

     def draw(self):
          pygame.draw.circle(screen,self.color,self.position,20)

     def update(self):
          self.draw()

class game :
     def __init__(self,Ball,Stick,Block,Hole) -> None:
          self.ball = Ball
          self.stick = Stick
          self.block = Block
          self.hole = Hole

     def run(self):
          Ball.update()
          Hole.update()

#create instance 
Stick = stick()
Block = block()
Hole = hole()
Ball = ball(Hole)
Game = game(Ball,Stick,Block,Hole)

while True :
     for event in pygame.event.get() :
          if event.type == pygame.QUIT :
               pygame.quit()
               sys.exit()
     
          if event.type == pygame.MOUSEBUTTONUP :
               x,y = pygame.mouse.get_pos()
               if x > Ball.position[0] : Ball.movement[0] = -(x - Ball.position[0])
               else :                    Ball.movement[0] = ( Ball.position[0] - x)
               if y > Ball.position[1] : Ball.movement[1] = -(y - Ball.position[1])
               else :                    Ball.movement[1] = (Ball.position[1] - y)
               
               
     screen.fill(screen_color)
     Game.run()
     pygame.display.update()
     

