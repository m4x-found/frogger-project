# Frogger project
import pygame
import random

# General bools
gameRunning = True
codeRunning = True

rightKeyDown = False
leftKeyDown = False
upKeyDown = False
downKeyDown = False

pygame.init()

width = 400
height = 500

mainWindow = pygame.display.set_mode((width, height))

gameData = {
"Images": {
	"MainBackground": pygame.transform.scale(pygame.image.load("Images//UnfinishedBack.png"), (400, 500)),
	"PlayerImage": pygame.transform.scale(pygame.image.load("Images//froggerwoutback.png"), (30, 30)),
	"Car": pygame.transform.scale(pygame.image.load("Images//racecar.png"), (50, 37)),
	"Log": pygame.transform.scale(pygame.image.load("Images//log.png"), (120, 51))
	},
	
"PositionData": {
	"PlayerPosition": [200,485]

	},
	
"Obstructions": {
"RoadOne": [["Car", 0, 310, 1], ["Car", 170, 310, 1]],
"RoadTwo": [["Car", 0, 349, 4], ["Car", 200, 349, 4], ["Car", 400, 349, 4]],
"RoadThree": [["Car", 0, 388, 3]],
"RoadFour": [["Car", 0, 427, 2]]
},
"RiverObjects": {	
"RowOne": [["Log1", 0, 63, 1, False]],
"RowTwo": [["Log2", 0, 113, -3, False]],
"RowThree": [["Log3", 0, 163, 4, False]],
"RowOnFour": [["Log4", 0, 213, -1, False]]
}
}

def checkCollisions(objectPosX, objectPosY, objectSizeX, objectSizeY):
	playerPositionX = gameData["PositionData"]["PlayerPosition"][0]
	playerPositionY = gameData["PositionData"]["PlayerPosition"][1]
	if (objectPosX) < playerPositionX < (objectPosX+objectSizeX): # Use smaller than whole size to allow player head room
		if (objectPosY) < playerPositionY < (objectPosY+objectSizeY):
			return True 

def centreToCornerPos(targetPosX, targetPosY, targetSizeX, targetSizeY):
	return [targetPosX-(targetSizeX/2), targetPosY-(targetSizeY/2)]

def uponLeftKey():
	global leftKeyDown
	leftKeyDown = True

def uponLeftKeyUp():
	global leftKeyDown
	leftKeyDown = False

def uponRightKey():
	global rightKeyDown
	rightKeyDown = True
	
def uponRightKeyUp():
	global rightKeyDown
	rightKeyDown = False
		
def uponUpKey():
	global upKeyDown
	upKeyDown = True
	
def uponUpKeyUp():
	global upKeyDown
	upKeyDown = False

def uponDownKey():
	global downKeyDown
	downKeyDown = True

def uponDownKeyUp():
	global downKeyDown
	downKeyDown = False

def leftKeyEnabled():
	if gameData["PositionData"]["PlayerPosition"][0] > 15 and rightKeyDown == False:
		gameData["PositionData"]["PlayerPosition"][0] -= 2
		
def rightKeyEnabled():
	if gameData["PositionData"]["PlayerPosition"][0] < 385 and leftKeyDown == False:
		gameData["PositionData"]["PlayerPosition"][0] += 2
		
def upKeyEnabled():
	if gameData["PositionData"]["PlayerPosition"][1] > 15:
		gameData["PositionData"]["PlayerPosition"][1] -= 2
	
def downKeyEnabled():
	if gameData["PositionData"]["PlayerPosition"][1] < 485:
		gameData["PositionData"]["PlayerPosition"][1] += 2

def handleObjectTick():
	for objectValue in gameData["Obstructions"]:
		for objectArr in gameData["Obstructions"][objectValue]:
			mainWindow.blit(gameData["Images"]["Car"], (objectArr[1], objectArr[2]))
			if checkCollisions(objectArr[1], objectArr[2], 50, 37):
				return "Dead"
			if objectArr[1] >= 400:
				objectArr[1] = 0
			else:
				objectArr[1] += objectArr[3]

	for objectValue in gameData["RiverObjects"]:
		for objectArr in gameData["RiverObjects"][objectValue]:
			mainWindow.blit(gameData["Images"]["Log"], (objectArr[1], objectArr[2]))
			if checkCollisions(objectArr[1], objectArr[2], 120, 51):
				gameData["PositionData"]["PlayerPosition"][0] += objectArr[3]
			if objectArr[3] >= 1:
				if objectArr[1] >= 400:
					objectArr[1] = -120
			elif objectArr[3] <= -1:
				if objectArr[1] <= -120:
					objectArr[1] = 400
			objectArr[1] += objectArr[3]
		
#str var1 << "";
#std::cin >> var1;
#std::cout << "\n";
#std::cout << var1;

while codeRunning:
	for eventValue in pygame.event.get():
		if eventValue.type == pygame.KEYDOWN:
			if eventValue.key == pygame.K_LEFT:
				uponLeftKey()
			elif eventValue.key == pygame.K_RIGHT:
				uponRightKey()
			elif eventValue.key == pygame.K_UP:
				uponUpKey()
			elif eventValue.key == pygame.K_DOWN:
				uponDownKey()
		elif eventValue.type == pygame.KEYUP:
			if eventValue.key == pygame.K_LEFT:
				uponLeftKeyUp()
			elif eventValue.key == pygame.K_RIGHT:
				uponRightKeyUp()
			elif eventValue.key == pygame.K_UP:
				uponUpKeyUp()
			elif eventValue.key == pygame.K_DOWN:
				uponDownKeyUp()
		elif eventValue.type == pygame.QUIT:
			exit()
	
		
	if upKeyDown:
		upKeyEnabled()
	if rightKeyDown:
		rightKeyEnabled()
	if leftKeyDown:
		leftKeyEnabled()
	if downKeyDown:
		downKeyEnabled()
	
	# ZIndex 1
	
	mainWindow.fill((0,0,0))
	
	# ZIndex 2
	
	mainWindow.blit(gameData["Images"]["MainBackground"], (0,0))
	pygame.draw.rect(mainWindow, (0,80,255), pygame.Rect(0, 63, 400, 204))
	
	# ZIndex 3
	'''
	mainWindow.blit(gameData["Images"]["Log"], (0, 73))
	mainWindow.blit(gameData["Images"]["Log"], (0, 123))
	mainWindow.blit(gameData["Images"]["Log"], (0, 173))
	mainWindow.blit(gameData["Images"]["Log"], (0, 223))
	'''

	handleObjectTick()
	
	mainWindow.blit(gameData["Images"]["PlayerImage"], (centreToCornerPos(gameData["PositionData"]["PlayerPosition"][0], gameData["PositionData"]["PlayerPosition"][1], 30, 30)))

	pygame.display.flip()
	pygame.time.Clock().tick(60)
	
