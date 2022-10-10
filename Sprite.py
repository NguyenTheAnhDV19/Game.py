import pygame,sys, random
pygame.init()
clock= pygame.time.Clock()  

width, height = 1280,800 

screen = pygame.display.set_mode((width,height))

class Crosshair(pygame.sprite.Sprite) :
    def __init__(self, picture):
        super().__init__()
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect()
    def shoot(self) :
        pygame.sprite.spritecollide(crosshair,target_group,True)
    def update(self) :
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite) : 
    def __init__(self, picture, posx, posy):
        super().__init__()
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect()
        self.rect.center = [posx, posy]

crosshair = Crosshair(r'C:\T\.vscode\T\shot_yellow_large.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

target_group = pygame.sprite.Group()
for target in range(20) :
    new = Target(r'C:\T\.vscode\T\duck_back.png', random.randrange(0, width), random.randrange(0, height))
    target_group.add(new)

pygame.mouse.set_visible(False)

while True : 
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN :
        crosshair.shoot()

    screen.fill((100,100,100))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    pygame.display.flip()
    clock.tick(60)