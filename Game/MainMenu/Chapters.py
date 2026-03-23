import pygame
from MainMenu.Button import Button as b
from MainMenu.LoginIn import LoginInterface

class Chapters:
    
    def __init__(self):
        self.BK = pygame.image.load("Game/MainMenu/img/Iniciar Sesion.png")
        self.title = pygame.image.load("Game/MainMenu/img/Title.png")

        self.buttons = []

        self.BackButton = b("Game/MainMenu/img/BackButton.png", "Back", 219, 341, 0)
        self.ColorCodeButton = b("Game/MainMenu/img/ColorCodeButton.png", "ColorCode", 219, 393, 0)
        self.ColorCodeButton.img = pygame.transform.scale(self.ColorCodeButton.img, (314, 312))

        self.buttons.append(self.BackButton)
        self.buttons.append(self.ColorCodeButton)

        self.selected = None
        self.posY = 0
        self.sizeH = 0.0

        self.login_interface = None

    def scale(self, x, y, w, h):
        return (x * w / 1512, y * h / 982)
    
    def draw(self, interfaz):
        w, h = interfaz.get_size()

        BK = pygame.transform.scale(self.BK, (w, h))
        interfaz.blit(BK, (0, 0))
        size = self.scale(922, 242, w, h)
        title = pygame.transform.scale(self.title, (int(size[0]), int(size[1])))
        interfaz.blit(title, self.scale(219, 169, w, h))
        
        mouse_pos = pygame.mouse.get_pos()

        for button in self.buttons:
            button.x, button.y = self.scale(button.base_x, button.base_y, w, h)

            if button.name == "ColorCode":
                size = self.scale(313.67, 312, w, h)
            else:
                size = self.scale(button.width, button.height, w, h)

            img_scaled = pygame.transform.scale(button.img, (int(size[0]), int(size[1])))

            if button.is_hovered(mouse_pos):
                size = self.scale(button.width * 1.1, button.height * 1.1, w, h)
                img_scaled = pygame.transform.scale(button.img, (int(size[0]), int(size[1])))

                interfaz.blit(img_scaled, (button.x - (size[0] - button.width) / 2, button.y - (size[1] - button.height) / 2))
                rect = pygame.Rect(button.x, button.y, int(size[0]), int(size[1]))
                if rect.collidepoint(mouse_pos):
                    self.posY = button.y-6
                    self.sizeH = self.scale(329, 42, w, h)[0]*1.1, self.scale(392, 42, w, h)[1]*1.1
            else:
               interfaz.blit(img_scaled, (button.x, button.y))

        if self.posY != 0:
            hover_surface = pygame.Surface((self.sizeH[0], self.sizeH[1]), pygame.SRCALPHA)
            hover_surface.fill((217, 217, 217, 25))  # rgba
            interfaz.blit(hover_surface, (self.scale(206, 400, w, h)[0], self.posY))

    
    def Option(self, event):
        pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons):

            if button.is_clicked(pos):
                print(button.name)

                if button.name == "Back":
                    return "Back"
                if button.name == "ColorCode":
                    return "ColorCode"
