import pygame
from MainMenu.Button import Button as b
from MainMenu.LoginIn import LoginInterface

class Chapters:
    
    def __init__(self):
        self.BK = pygame.image.load("Game/MainMenu/img/Iniciar Sesion.png")
        self.title = pygame.image.load("Game/MainMenu/img/Title.png")
        self.tileMenu = pygame.image.load("Game/MainMenu/img/Capítulos.png")

        self.buttons = []

        self.ColorCodeButton = b("Game/MainMenu/img/ColorCodeButton.png", "ColorCode", 219, 393+48, 0)
        self.ColorCodeButton.img = pygame.transform.scale(self.ColorCodeButton.img, (314, 312))
        self.ColorCodeButton.width = self.ColorCodeButton.img.get_width()
        self.ColorCodeButton.height = self.ColorCodeButton.img.get_height()

        self.Chapter2Button = b("Game/MainMenu/img/Frame 4.png", "Chapter2", self.ColorCodeButton.x+self.ColorCodeButton.width+64, 393+48, 0)
        self.Chapter2Button.img = pygame.transform.scale(self.Chapter2Button.img, (314, 312))
        self.Chapter2Button.width = self.ColorCodeButton.img.get_width()
        self.Chapter2Button.height = self.ColorCodeButton.img.get_height()

        self.Chapter3Button = b("Game/MainMenu/img/Frame 5.png", "Chapter3", self.Chapter2Button.x+self.ColorCodeButton.width+64, 393+48, 0)
        self.Chapter3Button.img = pygame.transform.scale(self.Chapter3Button.img, (314, 312))
        self.Chapter3Button.width = self.ColorCodeButton.img.get_width()
        self.Chapter3Button.height = self.ColorCodeButton.img.get_height()

        self.BackButton = b("Game/MainMenu/img/BackButton.png", "Back", 219, self.ColorCodeButton.y-51+16, 0)

        self.buttons.append(self.BackButton)
        self.buttons.append(self.ColorCodeButton)
        self.buttons.append(self.Chapter2Button)
        self.buttons.append(self.Chapter3Button)

        self.selected = None
        self.posX = 0
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

        CapitulosTitle = pygame.transform.scale(self.tileMenu, (138, 52))
        interfaz.blit(CapitulosTitle, self.scale(301, self.BackButton.base_y-CapitulosTitle.get_height()//2, w, h))

        mouse_pos = pygame.mouse.get_pos()

        hover_found = False  

        for button in self.buttons:
            button.x, button.y = self.scale(button.base_x, button.base_y, w, h)

            size = self.scale(button.width, button.height, w, h)
            img_scaled = pygame.transform.scale(button.img, (int(size[0]), int(size[1])))

            if button.is_hovered(mouse_pos) and button.name != "Back":
                hover_found = True

                size_hover = self.scale(button.width * 1.1, button.height * 1.1, w, h)
                img_scaled = pygame.transform.scale(button.img, (int(size_hover[0]), int(size_hover[1])))

                draw_x = button.x - (size_hover[0] - size[0]) / 2
                draw_y = button.y - (size_hover[1] - size[1]) / 2

                self.posX = draw_x
                self.posY = draw_y
                self.sizeH = size_hover

                interfaz.blit(img_scaled, (draw_x, draw_y))

            else:
                interfaz.blit(img_scaled, (button.x, button.y))


        if hover_found:
            hover_surface = pygame.Surface((int(self.sizeH[0]), int(self.sizeH[1])), pygame.SRCALPHA)
            hover_surface.fill((217, 217, 217, 25))
            interfaz.blit(hover_surface, (self.posX, self.posY))

    
    def Option(self, event):
        pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button.is_clicked(pos):
                    print(button.name)

                    if button.name == "Back":
                        return "Back"
                    if button.name == "ColorCode":
                        return "ColorCode"
