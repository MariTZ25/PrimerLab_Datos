import pygame

pygame.init()


class Libro():
    
    def __init__(self, x, y, image):
        self.image_original = image
        self.image = image
        self.shape = self.image.get_rect()
        self.shape.center = (x, y)
        self.scale = 1
        
        
    def movimiento(self, delta_x, delta_y):
        self.shape.x= self.shape.x + delta_x
        self.shape.y= self.shape.y + delta_y
        
    def agrandarLaEscala(self, scale):
        self.scale = scale
        width = int(self.image_original.get_width() * scale)
        height = int(self.image_original.get_height() * scale)
        
        center = self.shape.center
        
        self.image = pygame.transform.scale(self.image_original, (width, height))
        self.shape = self.image.get_rect()
        self.shape.center = center
        
    def draw(self, interfaz):
        interfaz.blit(self.image, self.shape)
        #pygame.draw.rect(interfaz,((230, 106, 230)), self.shape)