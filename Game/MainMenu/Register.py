
from .Button import Button as b
import pygame

class Register:
    def __init__(self):
       self.BK = pygame.image.load("Game/MainMenu/img/PopUp Register.png")

       self.RegisterButton = b("Game/MainMenu/img/RegisterButton.png", "Register", 0, 0, 0 )
       self.LogInButton = b("Game/MainMenu/img/¿Ya tienes cuenta_ Inicia Sesión aqui Button.png", "LogIn", 0, 0, 0)
       self.BackButton = b("Game/MainMenu/img/BackButton.png", "Back", 0, 0, 0)
       self.Bk2 = pygame.image.load("Game/MainMenu/img/UsuarioContraseñaConfirmarContra.png")

       self.username_entry = None
       self.password_entry = None
       self.confirmpassword_entry = None
    
    def scale(self, x, y, w, h):
        return (x * w / 1512, y * h / 982)

    def draw(self, interfaz):
        self.BackButton.x = interfaz.get_width() // 2 - self.BK.get_width() // 2 + 10
        self.BackButton.y = interfaz.get_height() // 4 - self.BackButton.height+10

        self.RegisterButton.x = interfaz.get_width() // 2 - self.BK.get_width() // 2 + 10+24+12
        self.RegisterButton.y = interfaz.get_height() // 4 + self.BK.get_height() - self.RegisterButton.height - 10-12-32

        self.LogInButton.x = interfaz.get_width() // 2 - self.BK.get_width() // 2 + 10+24+12
        self.LogInButton.y = interfaz.get_height() // 4 + self.BK.get_height() - self.LogInButton.height - 10-12-32-62
       
        interfaz.blit(self.BK, (interfaz.get_width() // 2 - self.BK.get_width() // 2, interfaz.get_height() // 4))
        interfaz.blit(self.Bk2, (interfaz.get_width() // 2 - self.BK.get_width() // 2 + 10+24+12, interfaz.get_height() // 4 + 10+12+32))

        interfaz.blit(self.LogInButton.img, (self.LogInButton.x, self.LogInButton.y))
        interfaz.blit(self.RegisterButton.img, (self.RegisterButton.x, self.RegisterButton.y))

        interfaz.blit(self.BackButton.img, (self.BackButton.x, self.BackButton.y))

    def exit(self):
        return "exit"
    
    def Opciones(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if self.RegisterButton.is_clicked(mouse_pos):
                    self.Register()
                    return "Register"
                elif self.LogInButton.is_clicked(mouse_pos):
                    return "LogIn"
                elif self.BackButton.is_clicked(mouse_pos):
                    return "exit"
    def Register(self):
        pass