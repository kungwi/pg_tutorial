import pygame
import random

x = pygame.init()

white = (255,255,255)
black = (  0,  0,  0)
red   = (255,  0,  0)
green = (  0,155,  0)

WIDTH = 800
HEIGHT = 600

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Slither')

pygame.display.update()

font = pygame.font.SysFont(None , 25)

def snake(block_size, snakelist):
	for XnY in snakelist:
		pygame.draw.rect(gameDisplay,green,(XnY[0],XnY[1],block_size,block_size))

def rectangle_colision(sx,sy,ax,ay,sz):
	if sx > ax + sz :
		return False
	if sy > ay + sz :
		return False
	if sx + sz < ax :
		return False
	if sy + sz < ay :
		return False

	return True

def text_objects(text,color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

def message_to_screen(msg , color):
	textSurf, textRect = text_objects(msg,color)
	textRect.center = (WIDTH/2) , (HEIGHT/2)
	gameDisplay.blit(textSurf,textRect)

def gameloop():
	block_size = 10
	lead_x = WIDTH/2
	lead_y = HEIGHT/2
	lead_x_change = 0
	lead_y_change = 0

	gameExit = False
	gameOver = False

	snakeList = []
	snakeLength = 1
	
	clock = pygame.time.Clock()
	FPS = 100

	randAppleX = random.randrange(1,WIDTH - block_size - 1)
	randAppleY = random.randrange(1,HEIGHT - block_size - 1)

	while not gameExit:

		while gameOver:
			gameDisplay.fill(white)
			message_to_screen("Press C to play again or Q to quit" , red)
			pygame.display.update()			

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:	
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key == pygame.K_c:
						gameloop()

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
			gameOver = True
		for eachSegment in snakeList[:-20]:
			if rectangle_colision(lead_x,lead_y,eachSegment[0],eachSegment[1],block_size):
				gameOver = True


		gameDisplay.fill(white)
		pygame.draw.rect(gameDisplay,red,(randAppleX,randAppleY,block_size,block_size))

		snakeHead = []
		snakeHead.append(lead_x)
		snakeHead.append(lead_y)
		snakeList.append(snakeHead)
		if len(snakeList) > snakeLength:
			del snakeList[0]

		snake(block_size,snakeList)
		pygame.display.update()

		if rectangle_colision(lead_x,lead_y,randAppleX,randAppleY,block_size) :
			randAppleX = random.randrange(1,WIDTH - block_size - 1)
			randAppleY = random.randrange(1,HEIGHT - block_size - 1)
			snakeLength += 6

		clock.tick(FPS)

	pygame.quit()
	quit()

gameloop()
