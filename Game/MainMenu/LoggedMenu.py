import pygame
from MainMenu.Button import Button as b
from MainMenu.LoginIn import LoginInterface

class LoggedMenu:
    
    def __init__(self):
        self.BK = pygame.image.load("Game/MainMenu/img/Iniciar Sesion.png")
        self.title = pygame.image.load("Game/MainMenu/img/Title.png")

        self.PopUpLogOut = None

        self.buttons = []

        self.ContinueButton = b("Game/MainMenu/img/TextMenu/_ Continuar.png", "Continue", 225, 425, 34 )
        self.NuevaRondaButton = b("Game/MainMenu/img/TextMenu/_ Nueva Partida.png", "NewRound", 225, 483, 34)
        self.ConfigButton = b("Game/MainMenu/img/TextMenu/_ ConfiguraciónText.png", "config", 225, 541, 34)
        self.creditsButton = b("Game/MainMenu/img/TextMenu/_ Créditostext.png", "credits", 225, 599, 34)
        self.LogOutButton = b("Game/MainMenu/img/TextMenu/_ Cerrar Sesión.png", "logout", 225, 657, 34)
        self.ExitButton = b("Game/MainMenu/img/TextMenu/_ SaLirText.png", "exit", 225, 715, 34)

        self.buttons.append(self.ContinueButton)
        self.buttons.append(self.NuevaRondaButton)
        self.buttons.append(self.ConfigButton)
        self.buttons.append(self.creditsButton)
        self.buttons.append(self.LogOutButton)
        self.buttons.append(self.ExitButton)

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

                if button.name == "exit":
                    pygame.quit()
                    return None
                if button.name == "logout":
                    return "logout"
                if button.name == "Continue":                    
                    return 5
                if button.name == "NewRound":                    
                    return 6


                return i + 1

class PopUpLogOut:
    def __init__(self):
        self.BK = pygame.image.load("Game/MainMenu/img/PopUp LogOut.png")

        self.YesButton = b("Game/MainMenu/img/Frame 9.png", "Yes", 0, 0, 0 )
        self.NoButton = b("Game/MainMenu/img/Frame 11.png", "No", 0, 0, 0)

    def scale(self, x, y, w, h):
        return (x * w / 1512, y * h / 982)

    def draw(self, interfaz):
        w, h = interfaz.get_size()

        BK = pygame.transform.scale(self.BK, (492, 251))
        interfaz.blit(BK, (w//2-BK.get_width()//2, h//2-BK.get_height()//2))
        
        mouse_pos = pygame.mouse.get_pos()

        size_button = self.scale(204, 33, w, h)
        self.YesButton.img = pygame.transform.scale(self.YesButton.img, (int(size_button[0]), int(size_button[1])))
        self.NoButton.img = pygame.transform.scale(self.NoButton.img, (int(size_button[0]), int(size_button[1])))

        self.YesButton.width = int(size_button[0])
        self.YesButton.height = int(size_button[1])
        self.NoButton.width = int(size_button[0])
        self.NoButton.height = int(size_button[1])

        self.NoButton.x = w//2-BK.get_width()//2 + self.scale(24+12, 150, w, h)[0]
        self.NoButton.y = h//2-BK.get_height()//2 + self.scale(100, 150+107-40, w, h)[1]

        self.YesButton.x = w//2-BK.get_width()//2 + self.scale(24+204+24, 150, w, h)[0]
        self.YesButton.y = h//2-BK.get_height()//2 + self.scale(100, 107+150-40, w, h)[1]

        for button in [self.YesButton, self.NoButton]:
           
            if button.is_hovered(mouse_pos):
                size = self.scale(button.width*1.1, button.height*1.1, w, h)
                img_scaled = pygame.transform.scale(button.img, (int(size[0]), int(size[1])))
                interfaz.blit(img_scaled, (button.x - (size[0] - button.width) / 2, button.y - (size[1] - button.height) / 2))
            else:
               interfaz.blit(button.img, (button.x, button.y))
        
    def Option(self, event):
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.YesButton.is_clicked(pos):
                return "Yes"
            if self.NoButton.is_clicked(pos):
                return "No"
            
class PopUpNewRound:
    def __init__(self):
        self.BK = pygame.image.load("Game/MainMenu/img/PopUp NuevaPartida.png")

        self.YesButton = b("Game/MainMenu/img/Crear.png", "Yes", 0, 0, 0 )
        self.NoButton = b("Game/MainMenu/img/Cancelar.png", "No", 0, 0, 0)

    def scale(self, x, y, w, h):
        return (x * w / 1512, y * h / 982)

    def draw(self, interfaz):
        w, h = interfaz.get_size()

        BK = pygame.transform.scale(self.BK, (492, 251))
        interfaz.blit(BK, (w//2-BK.get_width()//2, h//2-BK.get_height()//2))
        
        mouse_pos = pygame.mouse.get_pos()

        size_button = self.scale(204, 33, w, h)
        self.YesButton.img = pygame.transform.scale(self.YesButton.img, (int(size_button[0]), int(size_button[1])))
        self.NoButton.img = pygame.transform.scale(self.NoButton.img, (int(size_button[0]), int(size_button[1])))

        self.YesButton.width = int(size_button[0])
        self.YesButton.height = int(size_button[1])
        self.NoButton.width = int(size_button[0])
        self.NoButton.height = int(size_button[1])

        self.NoButton.x = w//2-BK.get_width()//2 + self.scale(24+12, 150, w, h)[0]
        self.NoButton.y = h//2-BK.get_height()//2 + self.scale(100, 150+107-40, w, h)[1]

        self.YesButton.x = w//2-BK.get_width()//2 + self.scale(24+204+24, 150, w, h)[0]
        self.YesButton.y = h//2-BK.get_height()//2 + self.scale(100, 107+150-40, w, h)[1]

        for button in [self.YesButton, self.NoButton]:
           
            if button.is_hovered(mouse_pos):
                size = self.scale(button.width*1.1, button.height*1.1, w, h)
                img_scaled = pygame.transform.scale(button.img, (int(size[0]), int(size[1])))
                interfaz.blit(img_scaled, (button.x - (size[0] - button.width) / 2, button.y - (size[1] - button.height) / 2))
            else:
               interfaz.blit(button.img, (button.x, button.y))
        
    def Option(self, event):
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.YesButton.is_clicked(pos):
                return "Yes"
            if self.NoButton.is_clicked(pos):
                return "No"