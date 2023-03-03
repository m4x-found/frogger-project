# Frogger project
import pygame

# General bools
gameRunning = True
codeRunning = True

pygame.init()

width = 400
height = 500

mainWindow = pygame.display.set_mode((width, height))

gameData = {
"Images": {
	"MainBackground": pygame.transform.scale(pygame.image.load("Images//UnfinishedBack.png"), (400, 500)),
	"PlayerImage": pygame.transform.scale(pygame.image.load("Images//froggerwoutback.png"), (30, 30))
	},
	
"PositionData": {
	"PlayerPosition": [200,485]

	}
}

def centreToCornerPos(targetPosX, targetPosY, targetSizeX, targetSizeY):
	return [targetPosX-(targetSizeX/2), targetPosY-(targetSizeY/2)]

def uponLeftKey():
	if gameData["PositionData"]["PlayerPosition"][0] > 20:
		gameData["PositionData"]["PlayerPosition"][0] -= 30

def uponRightKey():
	if gameData["PositionData"]["PlayerPosition"][0] < 380:
		gameData["PositionData"]["PlayerPosition"][0] += 30
		
def uponUpKey():
	if gameData["PositionData"]["PlayerPosition"][1] > 20:
		gameData["PositionData"]["PlayerPosition"][1] -= 40

while codeRunning:
	for eventValue in pygame.event.get():
		if eventValue.type == pygame.KEYDOWN:
			if eventValue.key == pygame.K_LEFT:
				uponLeftKey()
			elif eventValue.key == pygame.K_RIGHT:
				uponRightKey()
			elif eventValue.key == pygame.K_UP:
				uponUpKey()
	
	# ZIndex 1
	
	mainWindow.fill((0,0,0))
	
	# ZIndex 2
	
	mainWindow.blit(gameData["Images"]["MainBackground"], (0,0))
	mainWindow.blit(gameData["Images"]["PlayerImage"], (centreToCornerPos(gameData["PositionData"]["PlayerPosition"][0], gameData["PositionData"]["PlayerPosition"][1], 30, 30)))
	
	pygame.display.flip()
	pygame.time.Clock().tick(60)
	
