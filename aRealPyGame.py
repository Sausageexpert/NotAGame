import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('finally working')
clock = pygame.time.Clock()

gameState = 'run'

bg = pygame.image.load('C:/Users/soham/Desktop/AGame/Graphics/bgimg.png').convert() # convert makes it run more smoothly
bg = pygame.transform.scale(bg, (800, 400))

mainFont = pygame.font.Font('C:/Users/soham/Desktop/AGame/Fonts/Borel-Regular.ttf', 50)
fontSurface = mainFont.render('this is text', True, 'black')
fontRect = fontSurface.get_rect(center=(400, 200))

enemySprite = pygame.image.load('C:/Users/soham/Desktop/AGame/Graphics/enemy.png').convert_alpha() # alpha gets rid of the white background behind the image
enemySprite = pygame.transform.scale(enemySprite, (50, 50))
enemyRect = enemySprite.get_rect(topleft=(150, 200))

playerSurf = pygame.image.load('Graphics/bunny0.png').convert_alpha()
playerRect = playerSurf.get_rect(topleft = (80, 200)) # midleft, midright, midbottom, leftbottom... can use any
#playerRect = pygame.Rect(left, top, width, height)

player_gravity = 0

while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gameState='end'
    if gameState=='run':        
        # putting everything on the screen
        
        player_gravity+=1
        
        screen.blit(bg, (0, 0)) # block image transfer, basically putting one surface on another, top left is at 0,0
        pygame.draw.rect(screen, 'red', fontRect, width=6, border_radius=20) # surface, color, rectangle are mandatory, rest are optional. Without the width, it's a solid rectangle
        # One idea you could use here is to draw two rectangles for the font surface: one with the width specified (acts as a border) and one without it (acts as the main rectangle)
        screen.blit(fontSurface, fontRect)
        
        pygame.draw.line(screen, 'red', (0,0), (200, 200), width=2) # if width<1, nothing will be drawn (hmmm, invisible lines)
        
        keys = pygame.key.get_pressed() # returns a dictionary of EVERY button on the keyboard and 0 or 1
        if keys[pygame.K_SPACE] and playerRect.y>300:
            player_gravity=-20
        
        if playerRect.y>300: playerRect.y=300
            
        screen.blit(enemySprite, enemyRect)
        screen.blit(playerSurf, playerRect)
        playerRect.y+=player_gravity
        playerRect.left+=3
        enemyRect.right+=1 # can use left also, doesn't really make a difference
        if enemyRect.right==400:
            del enemyRect
        if playerRect.colliderect(enemyRect):
            print("collision")
        
        mousePos = pygame.mouse.get_pos() # returns a tuple with x and y positions. You could also use if event==pygame.MOUSEMOTION but that only works if the mouse is moving. print(event.pos)
        if playerRect.collidepoint((mousePos[0], mousePos[1])): # or just specify mousePos, no need of the tuple inside the brackets
            print("collided with the point")
        # pygame.mouse.get_pressed() returns a tuple with three booleans, one for each mouse button
        pygame.display.update()
        clock.tick(60) 
    else:
        screen.fill('yellow')
    # to make sure the player is touching the ground (condition for jumping), make sure the BOTTOM of the player rectangle coincides with the top of the floor rectangle
    
    
# the while True loop should not run faster than 60 times/sec (don't run the game too fast), 60 is a ceiling value
# Telling the game not to run too slowly (floor value) is much harder because you can't tell a computer to just...be better
