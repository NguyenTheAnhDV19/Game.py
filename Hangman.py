import pygame 
import math

pygame.init()
WIDTH,HIGH= 800,500 
win =pygame.display.set_mode((WIDTH,HIGH))
pygame.display.set_caption("Hang man game")

FPS = 60 
clock = pygame.time.Clock()


images = []
image0 = pygame.image.load(r'C:\T\bmages\bangman0.png')
images.append(image0)
image1 = pygame.image.load(r'C:\T\bmages\bangman1.png')
images.append(image1)
image2 = pygame.image.load(r'C:\T\bmages\bangman2.png')
images.append(image2)
image3 = pygame.image.load(r'C:\T\bmages\bangman3.png')
images.append(image3)
image4 = pygame.image.load(r'C:\T\bmages\bangman4.png')
images.append(image4)
image5 = pygame.image.load(r'C:\T\bmages\bangman5.png')
images.append(image5)
image6 = pygame.image.load(r'C:\T\bmages\bangman6.png')
images.append(image6)

hangman_status = 0

radius = 20 
gap = 15 

start_x = round((WIDTH - ((radius*2 + gap) * 13))/2 )
start_y = 400

A=65

letters = []
for i in range(26) :
    x = start_x + gap*2 + ((radius*2 + gap) * (i %13))
    y = start_y + ((i//13) * (gap + radius*2))
    letters.append([x,y,chr(A+i),True])

font_letter = pygame.font.SysFont('comicsans',40)

word = "INCREASING"
guessed = []

def draw() :
    win.fill((255,255,255))
    show_up = ""

    for letter in word :
        if letter in guessed :
            show_up += letter +" "
        else :
            show_up += "_ "

    for letter in letters :
        x,y, ltr,visible = letter 
        if visible :
            pygame.draw.circle(win,(41,41,41),(x,y), radius,3)
            text = font_letter.render(ltr,1,(41,41,41))
            win.blit(text,(x - text.get_width()/2,y - text.get_height()/2))
    


    win.blit(images[hangman_status],(150,100))
    show = font_letter.render(show_up,1,(41,41,41))
    win.blit(show,(400,200))
    pygame.display.update()

def display_message(message) :
    win.fill((255,255,255))
    text = font_letter.render(message,1,(41,41,41))
    win.blit(text, (WIDTH/2 - text.get_width()/2, HIGH/2 - text.get_height()/2))
    pygame.display.update()

run = True 
while run :
    clock.tick(FPS)
    draw()

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False 
        if event.type == pygame.MOUSEBUTTONDOWN :
            m_x,m_y= pygame.mouse.get_pos()
            for letter in letters :
                x,y,ltr,visible = letter
                if visible :
                    dis = math.sqrt((x - m_x)**2 + (y-m_y)**2)
                    if dis < radius :
                        guessed.append(ltr)
                        letter[3] = False
                        if ltr not in word :hangman_status += 1

    won = True 
    for letter in word :
        if letter not in guessed :
            won = False 
            break

    if won :
        display_message("U won")

    if hangman_status == 6 :
        display_message("U lost")

pygame.quit() 


