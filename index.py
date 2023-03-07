# Frogger project
import pygame
import random

# General bools
gameRunning = True
codeRunning = True

rightKeyDown = False
leftKeyDown = False
upKeyDown = False

pygame.init()

width = 400
height = 500

mainWindow = pygame.display.set_mode((width, height))

gameData = {
"Images": {
	"MainBackground": pygame.transform.scale(pygame.image.load("Images//UnfinishedBack.png"), (400, 500)),
	"PlayerImage": pygame.transform.scale(pygame.image.load("Images//froggerwoutback.png"), (30, 30)),
	"Car": pygame.transform.scale(pygame.image.load("Images//racecar.png"), (50, 37))
	},
	
"PositionData": {
	"PlayerPosition": [200,485]

	},
	
"Obstructions": [],
"RiverObjects": []
}

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


def leftKeyEnabled():
	if gameData["PositionData"]["PlayerPosition"][0] > 15 and rightKeyDown == False:
		gameData["PositionData"]["PlayerPosition"][0] -= 2
		
def rightKeyEnabled():
	if gameData["PositionData"]["PlayerPosition"][0] < 385 and leftKeyDown == False:
		gameData["PositionData"]["PlayerPosition"][0] += 2
		
def upKeyEnabled():
	if gameData["PositionData"]["PlayerPosition"][1] > 15:
		gameData["PositionData"]["PlayerPosition"][1] -= 2
	
def spawnRoadObject():
	# Find available road
	availableData = ["NIL", "NIL"]
	objectFound = False
	# check for empty roads
	rowFreeArray = [0, 1, 2, 3]
	rowFreeFinal = None
	for obstructionArray in gameData["Obstructions"]:
		if obstructionArray["RoadNumber"] == 0:
			rowFreeArray[0] == "USED"
		elif obstructionArray["RoadNumber"] == 1:
			rowFreeArray[1] == "USED"
		elif obstructionArray["RoadNumber"] == 2:
			rowFreeArray[2] == "USED"
		elif obstructionArray["RoadNumber"] == 3:
			rowFreeArray[3] == "USED"
			
	for rowNum in rowFreeArray:
		if rowNum != "USED":
			rowFreeFinal = rowNum
	
	for objectValue in gameData["Obstructions"]:
		objectFound = True
		if objectValue["Direction"] == "RIGHT":
			if objectValue["Position"][0] > 75:
				availableData[0] = "RIGHT"
				availableData[1] = objectValue["RoadNumber"]
		elif objectValue["Direction"] == "LEFT":
			if objectValue["Position"][1] < 325:
				availableData[0] = "LEFT"
				availableData[1] = objectValue["RoadNumber"]
	
	if objectFound == False:
		availableData[0] = "RIGHT"
		availableData[1] = 0
	
	if rowFreeFinal:
		availableData[0] = "RIGHT"
		availableData[1] = rowFreeFinal
	
	if availableData[0] != "NIL":
		randomisedIndex = random.randint(0, 2)
		initialX = 0
		initialY = rowFreeFinal or availableData[1]
		targetObject = "Car"
		if randomisedIndex == 0:
			targetObject = "Car"
		elif randomisedIndex == 1:
			targetObject = "Van"
		elif randomisedIndex == 2:
			targetObject = "Bike"
			
		if availableData[0] == "LEFT":
			initialX = 410
		elif availableData[1] == "RIGHT":
			initialX = -10
			
		if availableData[1] == 0:
			initialY = 325
		elif availableData[1] == 1:
			initialY = 364
		elif availableData[1] == 2:
			initialY = 403
		elif availableData[1] == 3:
			initialY = 442
		
		arrayData = {
			"Object": randomisedIndex,
			"Direction": availableData[0],
			"RoadNumber": availableData[1],
			"Position": [initialX, initialY]
		}
		
		gameData["Obstructions"].append(arrayData)
		
		return "Complete"
	else:
		return "NOTAVAILABLE"		
		
	
def handleObjectTick():
	currentRoadObjectsLen = len(gameData["Obstructions"])
	if currentRoadObjectsLen < 7:
		spawnRoadObject()
	
	for objectValue in gameData["Obstructions"]:
		#mainWindow.blit()
		print("Vals")
		
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
		elif eventValue.type == pygame.KEYUP:
			if eventValue.key == pygame.K_LEFT:
				uponLeftKeyUp()
			elif eventValue.key == pygame.K_RIGHT:
				uponRightKeyUp()
			elif eventValue.key == pygame.K_UP:
				uponUpKeyUp()
	
		
	if upKeyDown:
		upKeyEnabled()
	if rightKeyDown:
		rightKeyEnabled()
	if leftKeyDown:
		leftKeyEnabled()
	
	# ZIndex 1
	
	mainWindow.fill((0,0,0))
	
	# ZIndex 2
	
	mainWindow.blit(gameData["Images"]["MainBackground"], (0,0))
	mainWindow.blit(gameData["Images"]["PlayerImage"], (centreToCornerPos(gameData["PositionData"]["PlayerPosition"][0], gameData["PositionData"]["PlayerPosition"][1], 30, 30)))
	
	handleObjectTick()
	print(gameData["Obstructions"])
	
	pygame.display.flip()
	pygame.time.Clock().tick(60)
	
