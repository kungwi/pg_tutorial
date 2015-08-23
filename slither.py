import pygame
import time
import random

x = pygame.init()

white = (255,255,255)
black = (  0,  0,  0)
red   = (255,  0,  0)
green = (  0,155,  0)

WIDTH = 600
HEIGHT = 400

clock = pygame.time.Clock()
FPS = 100

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Slither')
icon = pygame.image.load("apple_or.png")
pygame.display.set_icon(icon)
back = pygame.image.load("Photo.png")

head_img = pygame.image.load('head.png')
apple_img = pygame.image.load('apple.png')

direction = "right"



smallfont = pygame.font.SysFont("comicsansms" , 25)
medfont = pygame.font.SysFont("comicsansms" , 50)
largefont = pygame.font.SysFont("comicsansms" , 80)

def game_intro():
	intro = True

	while intro:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					intro = False 
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
		
		
		gameDisplay.fill(white)
		gameDisplay.blit(back, (0, 0))
		message_to_screen("Welcome to Snake", green, -100 , "large")
		message_to_screen("press c to play or q to quit",black,0,"small")
		pygame.display.update()

	clock.tick(20)


def snake(block_size, snakelist):

	if direction == "right":
		head_rot = pygame.transform.rotate(head_img, 270)		
	if direction == "left":
		head_rot = pygame.transform.rotate(head_img, 90)		
	if direction == "up":
		head_rot = pygame.transform.rotate(head_img, 0)		
	if direction == "down":
		head_rot = pygame.transform.rotate(head_img, 180)		

	gameDisplay.blit(head_rot, (snakelist[-1][0], snakelist[-1][1]))

	for XnY in snakelist[:-9]:
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

def text_objects(text,color,size):
	if size == "small":
		textSurface = smallfont.render(text, True, color)
	elif size == "medium":
		textSurface = medfont.render(text, True, color)
	elif size == "large":
		textSurface = largefont.render(text, True, color)
	return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size="small"):
	textSurf, textRect = text_objects(msg,color,size)
	textRect.center = (WIDTH/2), (HEIGHT/2) + y_displace
	gameDisplay.blit(textSurf, textRect)

def gameloop():
	global direction
	direction = "right"	
	block_size = 10
	lead_x = WIDTH/2
	lead_y = HEIGHT/2
	lead_x_change = 1
	lead_y_change = 0

	gameExit = False
	gameOver = False

	snakeList = []
	snakeLength = 1
	

	randAppleX = random.randrange(1,WIDTH - block_size - 1)
	randAppleY = random.randrange(1,HEIGHT - block_size - 1)
	

	while not gameExit:

		while gameOver:
			gameDisplay.fill(white)
			message_to_screen("GAME OVER", red, y_displace=-50, size="large")
			message_to_screen("Press C to play again or Q to quit", 
									 black, 
								 y_displace=50,
								  size="small",)
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
					direction = "left"
					lead_x_change = -1
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					direction = "right"
					lead_x_change = 1
					lead_y_change = 0
				elif event.key == pygame.K_UP:
					direction = "up"
					lead_x_change = 0
					lead_y_change = -1
				elif event.key == pygame.K_DOWN:
					direction = "down"
					lead_x_change = 0
					lead_y_change = 1
	

		lead_y += lead_y_change
		lead_x += lead_x_change

		if lead_x >= WIDTH-block_size or lead_x < 0 or lead_y < 0 or lead_y >= HEIGHT-block_size:		
			gameOver = True
		for eachSegment in snakeList[:-20]:
			if rectangle_colision(lead_x,lead_y,eachSegment[0],eachSegment[1],block_size):
				gameOver = True


		gameDisplay.fill(white)
		gameDisplay.blit(apple_img, (randAppleX,randAppleY))

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

game_intro()
gameloop()
