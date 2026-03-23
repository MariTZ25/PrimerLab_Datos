import pygame

class Button:
    def __init__(self, img, name, x, y, height=None, width=None):
        self.img = pygame.image.load(img)
        self.name = name
        self.x = x
        self.y = y
        self.base_x = x
        self.base_y = y

        self.width = width if width and width > 0 else self.img.get_width()
        self.height = height if height and height > 0 else self.img.get_height()
    
    def is_clicked(self, pos):
        if self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height:
            return True
        return False
    
    def is_hovered(self, pos):
        if self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height:
            return True
        return False