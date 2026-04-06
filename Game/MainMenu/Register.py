
from pathlib import Path

from .Button import Button as b
import pygame

class Register:
    def __init__(self):
        self.font = pygame.font.Font(None, 24)

        self.username_text = ""
        self.password_text = ""
        self.confirm_password_text = ""

        self.active_user = False
        self.active_pass = False
        self.active_confirmpass = False

        # Posiciones para escribir
        self.user_rect = pygame.Rect(0, 0, 200, 24)
        self.pass_rect = pygame.Rect(0, 0, 200, 24)
        self.confirmpass_rect = pygame.Rect(0, 0, 200, 24)

        self.BK = pygame.image.load("Game/MainMenu/img/PopUp Register.png")

        self.RegisterButton = b("Game/MainMenu/img/RegisterButton.png", "Register", 0, 0, 0 )
        self.LogInButton = b("Game/MainMenu/img/¿Ya tienes cuenta_ Inicia Sesión aqui Button.png", "LogIn", 0, 0, 0)
        self.BackButton = b("Game/MainMenu/img/BackButton.png", "Back", 0, 0, 0)
        self.Bk2 = pygame.image.load("Game/MainMenu/img/UsuarioContraseñaConfirmarContra.png")
    
    def scale(self, x, y, w, h):
        return (x * w / 1512, y * h / 982)

    def draw(self, interfaz):
        w, h = interfaz.get_size()

        self.BackButton.x = interfaz.get_width() // 2 - self.BK.get_width() // 2 + 10
        self.BackButton.y = interfaz.get_height() // 4 - self.BackButton.height+10

        self.RegisterButton.x = interfaz.get_width() // 2 - self.BK.get_width() // 2 + 10+24+12
        self.RegisterButton.y = interfaz.get_height() // 4 + self.BK.get_height() - self.RegisterButton.height - 10-12-32

        self.LogInButton.x = interfaz.get_width() // 2 - self.BK.get_width() // 2 + 10+24+12
        self.LogInButton.y = interfaz.get_height() // 4 + self.BK.get_height() - self.LogInButton.height - 10-12-32-62
       
        interfaz.blit(self.BK, (interfaz.get_width() // 2 - self.BK.get_width() // 2, interfaz.get_height() // 4))
        interfaz.blit(self.Bk2, (interfaz.get_width() // 2 - self.BK.get_width() // 2 + 10+24+12, interfaz.get_height() // 4 + 10+12+32))
       
        base_x = interfaz.get_width() // 2 - self.BK.get_width() // 2 + 10+32+12
        base_y = interfaz.get_height() // 4 + 108+64+16

        # Usuario
        user_surface = self.font.render(self.username_text, True, (0,0,0))
        interfaz.blit(user_surface, (self.user_rect.x + 5, self.user_rect.y + 5))

        # Contraseña (oculta con *)
        hidden_pass = "*" * len(self.password_text)
        pass_surface = self.font.render(hidden_pass, True, (0,0,0))
        interfaz.blit(pass_surface, (self.pass_rect.x + 5, self.pass_rect.y + 5))

        # Confirmar Contraseña (Oculta con *)
        hidden_confpass = "*" * len(self.confirm_password_text)
        confirmpass_surface = self.font.render(hidden_confpass, True, (0,0,0))
        interfaz.blit(confirmpass_surface, (self.confirmpass_rect.x+5, self.confirmpass_rect.y+5))

        # Ajusta estos números a donde están los campos en tu imagen
        self.user_rect.topleft = (base_x + 20, base_y + 20)
        self.pass_rect.topleft = (base_x + 20, base_y + 70+30)
        self.confirmpass_rect.topleft = (base_x + 20, base_y + 70+20+70+20)

       # pygame.draw.rect(interfaz, (255,0,0), self.user_rect, 2)
        #pygame.draw.rect(interfaz, (0,255,0), self.pass_rect, 2)
       # pygame.draw.rect(interfaz, (0,0, 255), self.confirmpass_rect, 2)

        interfaz.blit(self.LogInButton.img, (self.LogInButton.x, self.LogInButton.y))
        interfaz.blit(self.RegisterButton.img, (self.RegisterButton.x, self.RegisterButton.y))

        interfaz.blit(self.BackButton.img, (self.BackButton.x, self.BackButton.y))

    def exit(self):
        return "exit"
    
    def Opciones(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if self.RegisterButton.is_clicked(mouse_pos):
                    if (self.confirm_password_text == self.password_text) and not self.user_exists(self.username_text):
                        self.Register()
                        return "exit"
                elif self.LogInButton.is_clicked(mouse_pos):
                    return "LogIn"
                elif self.BackButton.is_clicked(mouse_pos):
                    return "exit"
                
                if self.user_rect.collidepoint(event.pos):
                    self.active_user = True
                    self.active_pass = False
                    self.active_confirmpass = False
                elif self.pass_rect.collidepoint(event.pos):
                    self.active_pass = True
                    self.active_user = False
                    self.active_confirmpass = False
                elif self.confirmpass_rect.collidepoint(event.pos):
                    self.active_confirmpass = True
                    self.active_pass = False
                    self.active_user = False
                else:
                    self.active_user = False
                    self.active_pass = False
                    self.active_confirmpass = False
                
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
                if self.active_confirmpass:
                    if event.key == pygame.K_BACKSPACE:
                        self.confirm_password_text = self.confirm_password_text[:-1]
                    else:
                        self.confirm_password_text += event.unicode
                
    def Register(self):

        Path("Repositories").mkdir(exist_ok=True)

        archivo = "Repositories/Usuarios.csv"

        # Si el archivo no existe, crear con encabezado
        if not Path(archivo).exists():
            with open(archivo, "w", encoding="utf-8") as f:
                f.write("username,password\n")

        with open(archivo, "a", encoding="utf-8") as f:
            f.write(f"{self.username_text},{self.password_text}\n")
    
    def user_exists(self, username):
        try:
            with open("Repositories/Usuarios.csv", "r", encoding="utf-8") as f:
                for line in f.readlines()[1:]:
                    if line.split(",")[0] == username:
                        return True
        except FileNotFoundError:
            return False
        return False