
from .Button import Button as b
import pygame
from pathlib import Path

class LoginInterface:
    def __init__(self):

        #Efectos de sonido
        pygame.mixer.music.load("Music/menuMusica.mp3")
        pygame.mixer.music.play(-1)

        self.sonido_clickEspecial= pygame.mixer.Sound("Music/botonElegido.mp3")
        self.sonido_señalar= pygame.mixer.Sound("Music/señalar.mp3")
        self.font = pygame.font.Font(None, 24)

        self.username_text = ""
        self.password_text = ""

        self.active_user = False
        self.active_pass = False

        # Posiciones para escribir
        self.user_rect = pygame.Rect(0, 0, 200, 24)
        self.pass_rect = pygame.Rect(0, 0, 200, 24)

        self.BK = pygame.image.load("Game/MainMenu/img/PopUp Login.png")

        self.LogInButton = b("Game/MainMenu/img/LoginButton.png", "LogIn", 0, 0, 0 )
        self.RegisterButton = b("Game/MainMenu/img/¿nO TIENES CUENTA_ rEGISTRATE AQUI Button.png", "Register", 0, 0, 0)
        self.BackButton = b("Game/MainMenu/img/BackButton.png", "Back", 0, 0, 0)
        self.Bk2 = pygame.image.load("Game/MainMenu/img/UsuarioContraseña.png")

        self.username_entry = None
        self.password_entry = None
    
    def scale(self, x, y, w, h):
        return (x * w / 1512, y * h / 982)

    def draw(self, interfaz):
        self.BackButton.x = interfaz.get_width() // 2 - self.BK.get_width() // 2 + 10
        self.BackButton.y = interfaz.get_height() // 4 - self.BackButton.height+10

        self.LogInButton.x = interfaz.get_width() // 2 - self.BK.get_width() // 2 + 10+32+12
        self.LogInButton.y = interfaz.get_height() // 4 + self.BK.get_height() - self.LogInButton.height - 10-12-32

        self.RegisterButton.x = interfaz.get_width() // 2 - self.BK.get_width() // 2 + 10+32+12
        self.RegisterButton.y = interfaz.get_height() // 4 + self.BK.get_height() - self.RegisterButton.height - 10-12-32-42-62
       
        interfaz.blit(self.BK, (interfaz.get_width() // 2 - self.BK.get_width() // 2, interfaz.get_height() // 4))
        interfaz.blit(self.Bk2, (interfaz.get_width() // 2 - self.BK.get_width() // 2 + 10+32+12, interfaz.get_height() // 4 + 10+12+32))

        base_x = interfaz.get_width() // 2 - self.BK.get_width() // 2 + 10+32+12
        base_y = interfaz.get_height() // 4 + 10+12+32+108

        # Usuario
        user_surface = self.font.render(self.username_text, True, (0,0,0))
        interfaz.blit(user_surface, (self.user_rect.x + 5, self.user_rect.y + 5))

        # Contraseña (oculta con *)
        hidden_pass = "*" * len(self.password_text)
        pass_surface = self.font.render(hidden_pass, True, (0,0,0))
        interfaz.blit(pass_surface, (self.pass_rect.x + 5, self.pass_rect.y + 5))


        self.user_rect.topleft = (base_x + 20, base_y + 20)
        self.pass_rect.topleft = (base_x + 20, base_y + 70+28)

      #  pygame.draw.rect(interfaz, (255,0,0), self.user_rect, 2)
      #  pygame.draw.rect(interfaz, (0,255,0), self.pass_rect, 2)

        interfaz.blit(self.LogInButton.img, (self.LogInButton.x, self.LogInButton.y))
        interfaz.blit(self.RegisterButton.img, (self.RegisterButton.x, self.RegisterButton.y))

        interfaz.blit(self.BackButton.img, (self.BackButton.x, self.BackButton.y))

    def exit(self):
        return "exit"
    
    def Opciones(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if self.LogInButton.is_clicked(mouse_pos):
                    if self.login(self.username_text, self.password_text) == True:
                        self.sonido_clickEspecial.play()
                        return "LoggedIn"
                elif self.RegisterButton.is_clicked(mouse_pos):
                    self.sonido_clickEspecial.play()
                    return "Register"
                elif self.BackButton.is_clicked(mouse_pos):
                    self.sonido_clickEspecial.play()
                    return "exit"
                
                if self.user_rect.collidepoint(event.pos):
                    self.active_user = True
                    self.active_pass = False
                elif self.pass_rect.collidepoint(event.pos):
                    self.active_pass = True
                    self.active_user = False
                else:
                    self.active_user = False
                    self.active_pass = False

            if event.type == pygame.KEYDOWN:
                if self.active_user:
                    if event.key == pygame.K_BACKSPACE:
                        self.username_text = self.username_text[:-1]
                    else:
                        self.username_text += event.unicode

                if self.active_pass:
                    if event.key == pygame.K_BACKSPACE:
                        self.password_text = self.password_text[:-1]
                    else:
                        self.password_text += event.unicode

    def login(self, name, contra):

        Path("Repositories").mkdir(exist_ok=True)

        try:
            with open("Repositories/Usuarios.csv", "r", encoding="utf-8") as f:
                for linea in f:
                    username = linea.split(",")[0]
                    contraseña = linea.split(",")[1].strip()
                    if (username == name and contraseña == contra):
                        return True
                return False
        except FileNotFoundError:
            return False
        return False


            