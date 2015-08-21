import pygame
import time

x = pygame.init()

white = (255,255,255)
black = (  0,  0,  0)
red   = (255,  0,  0)

WIDTH = 800
HEIGHT = 600

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Slither')

pygame.display.update()

gameExit = False

block_size = 10
lead_x = WIDTH/2
lead_y = HEIGHT/2
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()
FPS = 100

font = pygame.font.SysFont(None , 25)

def message_to_screen(msg , color):
	screen_text = font.render(msg, True , color)
	gameDisplay.blit(screen_text,(WIDTH/2,HEIGHT/2))

while not gameExit:
	for event in pygame.event.get():
		# print(event)
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				lead_x_change = -1
				lead_y_change = 0
			elif event.key == pygame.K_RIGHT:
				lead_x_change = 1
				lead_y_change = 0
			elif event.key == pygame.K_UP:
				lead_x_change = 0
				lead_y_change = -1
			elif event.key == pygame.K_DOWN:
				lead_x_change = 0
				lead_y_change = 1
	
	#	if event.type == pygame.KEYUP:
	#		if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
	#			lead_x_change = 0
	#		if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
	#			lead_y_change = 0

	lead_y += lead_y_change
	lead_x += lead_x_change

	if lead_x >= WIDTH-block_size or lead_x < 0 or lead_y < 0 or lead_y >= HEIGHT-block_size:		
		gameExit = True

	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay,black,(lead_x,lead_y,block_size,block_size))
	pygame.display.update()

	clock.tick(FPS)

message_to_screen("You lose",red)
pygame.display.update()
time.sleep(5)
pygame.quit()
quit()
