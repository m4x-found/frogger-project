# Frogger project
import pygame
import random

# General bools
gameRunning = True
codeRunning = True
gameWon = False

rightKeyDown = False
leftKeyDown = False
upKeyDown = False
downKeyDown = False

pygame.init()
pygame.font.init()
defaultFont = pygame.font.SysFont("Comic Sans MS", 30)


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

"SlotFilled": {
	"One": False,
	"Two": False,
	"Three": False
	},
	
"Obstructions": {
	"RoadOne": [["Car", 0, 310, 1], ["Car", 170, 310, 1]],
	"RoadTwo": [["Car", 0, 349, 4], ["Car", 200, 349, 4], ["Car", 400, 349, 4]],
	"RoadThree": [["Car", 0, 388, 3]],
	"RoadFour": [["Car", 0, 427, 2]]
	},

"RiverObjects": {	
	"RowOne": [["Log1", 0, 63, 1, False]],
	"RowTwo": [["Log2", 0, 113, -2, False]],
	"RowThree": [["Log3", 0, 163, 3, False]],
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
	if gameData["PositionData"]["PlayerPosition"][1] > 70:
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
	
	if gameData["PositionData"]["PlayerPosition"][1] <= 70:
		print("Handle end game")
		if 125 > gameData["PositionData"]["PlayerPosition"][0] > 75:
			if gameData["SlotFilled"]["One"] == False:
				gameData["PositionData"]["PlayerPosition"] = [200, 485]
				gameData["SlotFilled"]["One"] = True
		elif 225 > gameData["PositionData"]["PlayerPosition"][0] > 175:
			if gameData["SlotFilled"]["Two"] == False:
				gameData["PositionData"]["PlayerPosition"] = [200, 485]
				gameData["SlotFilled"]["Two"] = True
		elif 325 > gameData["PositionData"]["PlayerPosition"][0] > 275:
			if gameData["SlotFilled"]["Three"] == False:
				gameData["PositionData"]["PlayerPosition"] = [200, 485]
				gameData["SlotFilled"]["Three"] = True

	if gameData["SlotFilled"]["One"]:
		mainWindow.blit(gameData["Images"]["PlayerImage"], centreToCornerPos(93, 40, 30, 30))
	if gameData["SlotFilled"]["Two"]:
		mainWindow.blit(gameData["Images"]["PlayerImage"], centreToCornerPos(200, 40, 30, 30))
	if gameData["SlotFilled"]["Three"]:
		mainWindow.blit(gameData["Images"]["PlayerImage"], centreToCornerPos(307, 40, 30, 30))

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

	if gameWon != True and gameRunning == True:
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

		handleObjectTick()
		
		mainWindow.blit(gameData["Images"]["PlayerImage"], (centreToCornerPos(gameData["PositionData"]["PlayerPosition"][0], gameData["PositionData"]["PlayerPosition"][1], 30, 30)))

	elif gameWon == True and gameRunning == False:

		pygame.draw.rect(mainWindow, (0, 0, 0), pygame.Rect(0, 0, 400, 500))
		textSurface = defaultFont.render("Game Over", False, (255, 255, 255))
		mainWindow.blit(textSurface, (125, 225))

	elif gameWon == False and gameRunning == False:

		pygame.draw.rect(mainWindow, (0, 0, 0), pygame.Rect(0, 0, 400, 500))		



	# Post processes

	# Game won

	if gameData["SlotFilled"]["One"] and gameData["SlotFilled"]["Two"] and gameData["SlotFilled"]["Three"]:
		gameWon = True
		gameRunning = False

	pygame.display.flip()
	pygame.time.Clock().tick(60)