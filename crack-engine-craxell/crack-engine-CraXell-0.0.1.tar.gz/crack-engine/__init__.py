import pygame

def drawImage(surface, imagePath, x, y): # Pass in the surface, the path, and the coordinates
    image = pygame.image.load(imagePath) # We load the image
    surface.blit(image, (x, y)) # Then we print it on to the screen
	
def collisionBox():
    pass # Added a function for future updates

