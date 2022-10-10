from copy import deepcopy
import pygame,sys, random,time
pygame.init()
clock= pygame.time.Clock()  

width, height = 1280,800 
screen = pygame.display.set_mode((width,height))

class snake :
    def __init__(self,snake_body,move_x,move_y) -> None:
        self.move_x,self.move_y = move_x,move_y
        self.snake_body = pygame.image.load(snake_body)
        self.snake = [self.snake_body.get_rect(center = (40,40))]
        self.collide = False
        self.player_score = 0 
    def move_snake(self) :
        snake_copy = deepcopy(self.snake)
        for i in range(len(self.snake)-1,0,-1) :
            self.snake[i].x = snake_copy[i-1].x
            self.snake[i].y = snake_copy[i-1].y
        self.snake[0].x += self.move_x 
        self.snake[0].y += self.move_y 
        if self.snake[0].bottom >= height+40 :self.snake[0].top = 0 
        elif self.snake[0].top <=-40 : self.snake[0].bottom = height 
        if self.snake[0].right >= width+40 : self.snake[0].left = 0 
        elif self.snake[0].left <= -40 : self.snake[0].right = width
    def reset_move(self) :
        self.move_x,self.move_y = 0,0
    def add_snake(self) :
        if pygame.Rect.colliderect(self.snake[0], Apple.rect) :
            self.snake.append(self.snake_body.get_rect(center = (-40,-40)))
            self.player_score += 1
    def display_snake(self) :
        for i in range(len(self.snake)) :screen.blit(self.snake_body,self.snake[i])
    def Collide(self) :
        for i in range(1,len(self.snake)) :
            if pygame.Rect.colliderect(self.snake[0],self.snake[i]) :self.collide = True 
    def update(self) :
        self.move_snake()
        self.add_snake()
        self.display_snake()
        self.Collide()

Snake = snake(r'C:\T\block.jpg',0,0)

class apple :
    def __init__(self,apple_image,posx,posy) -> None:
        self.apple_image = pygame.image.load(apple_image)
        self.posx = posx
        self.posy = posy 
        self.rect = self.apple_image.get_rect(center = (self.posx,self.posy))
    def display_apple(self) :
        screen.blit(self.apple_image,self.rect)
    def spawn_apple(self) :
        for i in range(len(Snake.snake)) :
            if pygame.Rect.colliderect(self.rect,Snake.snake[i]) :
                list_x,list_y = [],[]
                for y in range(100,height-100) :
                    if y% 40 == 0 : list_y.append(y)
                for x in range(100,width-100) :
                    if x % 40 == 0 : list_x.append(x)
                self.rect.x = random.choice(list_x) 
                self.rect.y = random.choice(list_y) 
    def update(self) :
        self.spawn_apple()
        self.display_apple()
Apple = apple(r'C:\T\bapples.jpg',100,50)

class game_manager :
    def __init__(self,font) :
        self.font = pygame.font.Font(font,32)
        self.color = (0,0,0)
        self.player_highest_score = 0 
    def run(self) :
        Snake.update()
        Apple.update()
        self.restart_game()
        self.display_score()
        self.highest_score()
    def display_score(self) :
        score = self.font.render("YOUR SCORE: " + str(Snake.player_score),True,self.color)
        score_rect = score.get_rect(center = (400,20))
        screen.blit(score,score_rect)
    def restart_game(self) :
        if Snake.collide :
            Snake.move_x,Snake.move_y = 0,0 
            Snake.snake= [Snake.snake_body.get_rect(center = (40,40))]
            if self.player_highest_score<= Snake.player_score :self.player_highest_score = Snake.player_score
            Snake.player_score = 0 
            Snake.collide = False    
    def display_lose(self) :
        pass 
    def highest_score(self) :
        highest_score = self.font.render("YOUR HIGHEST SCORE: " + str(self.player_highest_score),True,self.color)
        heighst_score_rect = highest_score.get_rect(center = (800,20))
        screen.blit(highest_score,heighst_score_rect)
    def pause(self) :
        pass
    def countinue(self) :
        pass 
Game_manager = game_manager("freesansbold.ttf")

while True : 
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_DOWN and Snake.move_y >= 0:
                Snake.reset_move()
                Snake.move_y = 40
            if event.key == pygame.K_UP and Snake.move_y <= 0 :
                Snake.reset_move()
                Snake.move_y = -40
            if event.key == pygame.K_LEFT and Snake.move_x <= 0:
                Snake.reset_move()
                Snake.move_x = -40
            if event.key == pygame.K_RIGHT and Snake.move_x >= 0 :
                Snake.reset_move()
                Snake.move_x = 40 
    screen.fill((100,100,100))
    Game_manager.run()
    time.sleep(0.05)
    pygame.display.flip()
    clock.tick(60)