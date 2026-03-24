from pathlib import Path

import pygame
from MainMenu.Button import Button as b
from MainMenu.LoginIn import LoginInterface

class Config:
    
    def __init__(self):
        self.BK = pygame.image.load("Game/MainMenu/img/Bk.png")
        self.title = pygame.image.load("Game/MainMenu/img/Title.png")
        self.tileMenu = pygame.image.load("Game/MainMenu/img/Configuración.png")
        self.Bk2 = pygame.image.load("Game/MainMenu/img/Bk2.png")

        self.buttons = []
        
        self.VolButton = b("Game/MainMenu/img/Volumen.png", "Volumen", 264, 425, 0)
        self.BrilloButton = b("Game/MainMenu/img/Brillo.png", "Brillo", 264, self.VolButton.y+self.VolButton.height//4+20, 0)
        self.SensibilidadButton = b("Game/MainMenu/img/Sensibilidad.png", "Sensibilidad", 264, self.BrilloButton.y+self.BrilloButton.height//4+20, 0)
        self.ControlesButton = b("Game/MainMenu/img/Controles.png", "Control", 264, self.SensibilidadButton.y+self.SensibilidadButton.height//4+20, 0)
        self.IdiomaButton = b("Game/MainMenu/img/Idioma.png", "Idioma", 264, self.ControlesButton.y+self.ControlesButton.height//4+20, 0)

        self.BackButton = b("Game/MainMenu/img/BackButton.png", "Back", 219, 383-52+16, 0)

        self.opciones =  None
        self.music = 0.5
        self.ambience = 0.5
        self.sensibildad=0.5
        self.keyboard = 1

        self.brillo=1

        # posición de la barra (AJUSTA ESTO A TU DISEÑO)
        self.slider_x = 0
        self.slider_y = 0
        self.slider_width = 0

        self.slider2_x=0
        self.slider2_y=0
        self.slider2_width=0

        self.dragging = False
        self.dragging2 = False

        self.current_option=None

        self.buttons.append(self.BackButton)
        self.buttons.append(self.VolButton)
        self.buttons.append(self.BrilloButton)
        self.buttons.append(self.SensibilidadButton)
        self.buttons.append(self.ControlesButton)
        self.buttons.append(self.IdiomaButton)

        self.hover_found = False
        self.posX = 0
        self.posY = 0
        self.sizeH = 0.0

        self.Option_interface = None

        self.Cargar()
        self.arrow_rect = pygame.Rect(0, 0, 185, 162)
        self.wasd_rect= pygame.Rect(0, 0, 185, 162)

        self.keyboardArrow = b("game/MainMenu/img/ArrowButton.png", "Flecha", 0, 0 ,0)
        self.keyboardWASD= b("game/MainMenu/img/WASDOption.png", "WASD", 0, 0 ,0)



    def scale(self, x, y, w, h):
        return (x * w / 1512, y * h / 982)
    
    def draw(self, interfaz):
        w, h = interfaz.get_size()

        BK = pygame.transform.scale(self.BK, (w, h))
        interfaz.blit(BK, (0, 0))

        size = self.scale(922, 242, w, h)
        title = pygame.transform.scale(self.title, (int(size[0]), int(size[1])))
        interfaz.blit(title, self.scale(219, 144, w, h))

        size = self.scale(1074, 428, w, h)
        BK2 = pygame.transform.scale(self.Bk2, (int(size[0]), int(size[1])))
        interfaz.blit(BK2, self.scale(219, 383, w, h))

        ConfiguracionTitle = pygame.transform.scale(self.tileMenu, (991, 52))
        interfaz.blit(ConfiguracionTitle, self.scale(301, self.BackButton.base_y-ConfiguracionTitle.get_height()//2, w, h))

        mouse_pos = pygame.mouse.get_pos()
        

        for button in self.buttons:
            button.x, button.y = self.scale(button.base_x, button.base_y, w, h)
            size = self.scale(button.width, button.height, w, h)
            
            if button.name != "Back":
                button.rect = pygame.Rect(button.x, button.y, int(size[0]//4),int(size[1])//4)
                img_scaled = pygame.transform.scale(button.img, (int(size[0]//4), int(size[1])//4))
            else:
                button.rect = pygame.Rect(button.x, button.y, int(size[0]),int(size[1]))
                img_scaled = pygame.transform.scale(button.img, (int(size[0]), int(size[1])))

            if button.is_hovered2(mouse_pos) and button.name != "Back":
                self.hover_found = True

                size_hover = self.scale(button.width * 1.1//4, button.height * 1.1//4, w, h)
                img_scaled = pygame.transform.scale(button.img, (int(size_hover[0]), int(size_hover[1])))

                draw_x = button.x - (size_hover[0] - size[0]//4) / 2
                draw_y = button.y - (size_hover[1] - size[1]//4) / 2

                self.posX = draw_x
                self.posY = draw_y
                self.sizeH = size_hover

                interfaz.blit(img_scaled, (draw_x, draw_y))

            else:
                interfaz.blit(img_scaled, (button.x, button.y))
        


        if self.hover_found:
            hover_surface = pygame.Surface((int(self.sizeH[0]), int(self.sizeH[1])), pygame.SRCALPHA)
            hover_surface.fill((217, 217, 217, 25))
            interfaz.blit(hover_surface, (self.posX, self.posY))

        if self.current_option == "Volumen":
            size = self.scale(778, 380, w, h)
            
            Vol = pygame.transform.scale(self.opciones, (int(size[0]), int(size[1])))
            interfaz.blit(Vol, self.scale(500, 420, w, h))

            self.slider_x = self.scale(708, 0, w, h)[0]
            self.slider_y = self.scale(0, 595, w, h)[1]
            self.slider_width = self.scale(444,0, w, h)[0]

            self.slider2_x = self.scale(708, 0, w, h)[0]
            self.slider2_y = self.scale(0, 595+32, w, h)[1]
            self.slider2_width = self.scale(444,0, w, h)[0]

            #sinterfaz.blit(self.opciones, (self.slider_x - 50, self.slider_y - 50))

            # bolita
            circle2_x = self.slider2_x+int(self.ambience*self.slider2_width)
            circle2_y = self.slider2_y

            circle_x = self.slider_x + int(self.music * self.slider_width)
            circle_y = self.slider_y

            pygame.draw.circle(interfaz, (255,255,255), (circle_x, circle_y), 8)
            pygame.draw.circle(interfaz, (255,255,255), (circle2_x, circle2_y), 8)

        if self.current_option == "Brillo":
            size = self.scale(778, 380, w, h)
            
            Brillo = pygame.transform.scale(self.opciones, (int(size[0]), int(size[1])))
            interfaz.blit(Brillo, self.scale(500, 420, w, h))

            self.slider_x = self.scale(708, 0, w, h)[0]
            self.slider_y = self.scale(0, 595+16, w, h)[1]
            self.slider_width = self.scale(444,0, w, h)[0]

            #sinterfaz.blit(self.opciones, (self.slider_x - 50, self.slider_y - 50))
            circle_x = self.slider_x + int(self.brillo * self.slider_width)
            circle_y = self.slider_y

            pygame.draw.circle(interfaz, (255,255,255), (circle_x, circle_y), 8)
        
        if self.current_option == "Sensibilidad":
            size = self.scale(778, 380, w, h)
            
            Sensibilidad = pygame.transform.scale(self.opciones, (int(size[0]), int(size[1])))
            interfaz.blit(Sensibilidad, self.scale(500, 420, w, h))

            self.slider_x = self.scale(708, 0, w, h)[0]
            self.slider_y = self.scale(0, 595+16, w, h)[1]
            self.slider_width = self.scale(444,0, w, h)[0]

            #sinterfaz.blit(self.opciones, (self.slider_x - 50, self.slider_y - 50))
            circle_x = self.slider_x + int(self.sensibildad * self.slider_width)
            circle_y = self.slider_y

            pygame.draw.circle(interfaz, (255,255,255), (circle_x, circle_y), 8)

        if self.current_option == "Control":
            pos_arrow = self.scale(660, 500, w, h)
            pos_wasd = self.scale(905, 500, w, h)
            size = self.scale(778, 380, w, h)
            
            Control = pygame.transform.scale(self.opciones, (int(size[0]), int(size[1])))
            interfaz.blit(Control, self.scale(500, 420, w, h))

            if self.keyboard==1:
                arrow_img = pygame.image.load("game/MainMenu/img/ArrowButton.png")
                wasd_img = pygame.image.load("game/MainMenu/img/WASDOption.png")
            else:
                arrow_img = pygame.image.load("Game/MainMenu/img/ArrowOption2.png")
                wasd_img = pygame.image.load("Game/MainMenu/img/WASDOption2.png")
            
            arrow_img = pygame.transform.scale(arrow_img, (185, 162))
            wasd_img = pygame.transform.scale(wasd_img, (185, 162))

            self.arrow_rect = pygame.Rect(pos_arrow[0], pos_arrow[1], 185, 162)
            self.wasd_rect = pygame.Rect(pos_wasd[0], pos_wasd[1], 185, 162)


            interfaz.blit(arrow_img, pos_arrow)
            interfaz.blit(wasd_img, pos_wasd)



        if self.current_option == "Idioma":
            size = self.scale(778, 380, w, h)

            Idioma = pygame.transform.scale(self.opciones, (int(size[0]), int(size[1])))
            interfaz.blit(Idioma, self.scale(500, 420, w, h))

    
    def Option(self, event):

        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in self.buttons:
                if button.rect.collidepoint(pos):
                    if button.name == "Back":
                        return "Back"
                    if button.name == "Volumen":
                        self.opciones=pygame.image.load("Game/MainMenu/img/VolOpciones.png")
                        self.current_option = "Volumen"
                    if button.name == "Brillo":
                        self.opciones = pygame.image.load("Game/MainMenu/img/BrilloOpciones.png")
                        self.current_option = "Brillo"
                    if button.name == "Sensibilidad":
                        self.opciones = pygame.image.load("Game/MainMenu/img/SensibilidadOpciones.png")
                        self.current_option = "Sensibilidad"
                    if button.name == "Control":
                        self.opciones = pygame.image.load("Game/MainMenu/img/ControlesOpciones.png")
                        self.current_option = "Control"
                    if button.name == "Idioma":
                        self.opciones = pygame.image.load("Game/MainMenu/img/IdiomaOpciones.png")
                        self.current_option = "Idioma"

        if self.current_option == "Volumen":
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                slider_rect = pygame.Rect(self.slider_x, self.slider_y - 10, self.slider_width, 20)
                slider2_rect = pygame.Rect(self.slider2_x, self.slider2_y - 10, self.slider2_width, 20)

                if slider_rect.collidepoint(event.pos):
                    self.dragging = True
                    self.dragging2 = False
                
                if slider2_rect.collidepoint(event.pos):
                    self.dragging2 = True
                    self.dragging = False

            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
                self.dragging2 = False
                self.Guardar()

            elif event.type == pygame.MOUSEMOTION and self.dragging:
                mouse_x = event.pos[0]
                self.music = (mouse_x - self.slider_x) / self.slider_width
                self.music = max(0, min(1, self.music))
            
            elif event.type == pygame.MOUSEMOTION and self.dragging2:
                mouse_x = event.pos[0]
                self.ambience=(mouse_x - self.slider2_x)/self.slider2_width
                self.ambience=max(0, min(1, self.ambience))
        
        if self.current_option == "Brillo":
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                slider_rect = pygame.Rect(self.slider_x, self.slider_y - 10, self.slider_width, 20)

                if slider_rect.collidepoint(event.pos):
                    self.dragging = True

            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
                self.Guardar()

            elif event.type == pygame.MOUSEMOTION and self.dragging:
                mouse_x = event.pos[0]
                self.brillo = (mouse_x - self.slider_x) / self.slider_width
                self.brillo = max(0, min(1, self.brillo))
        
        if self.current_option == "Sensibilidad":
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                slider_rect = pygame.Rect(self.slider_x, self.slider_y - 10, self.slider_width, 20)

                if slider_rect.collidepoint(event.pos):
                    self.dragging = True

            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
                self.Guardar()

            elif event.type == pygame.MOUSEMOTION and self.dragging:
                mouse_x = event.pos[0]
                self.sensibildad = (mouse_x - self.slider_x) / self.slider_width
                self.sensibildad = max(0, min(1, self.sensibildad))
            
        if self.current_option == "Control":

             if event.type == pygame.MOUSEBUTTONDOWN:

                if self.arrow_rect.collidepoint(event.pos):
                    self.keyboard = 0
                    self.Guardar()

                elif self.wasd_rect.collidepoint(event.pos):
                    self.keyboard = 1
                    self.Guardar()

            
    
    def Guardar(self):
        Path("Repositories").mkdir(exist_ok=True)
        lineas = []
        if Path("Repositories/Configuracion.csv").exists():
            with open("Repositories/Configuracion.csv", "r", encoding="utf-8") as f:
                lineas = f.readlines()
        if len(lineas)<2:
            lineas = ["Musica,Ambiente,Brillo,Sensibilidad,teclado\n",
            f"{self.music},{self.ambience},{self.brillo},{self.sensibildad},{self.keyboard}\n"]
        else:
            lineas[1] = f"{self.music},{self.ambience},{self.brillo},{self.sensibildad},{self.keyboard}\n"

        with open("Repositories/Configuracion.csv", "w", encoding="utf-8") as f:
            f.writelines(lineas)
    
    def Cargar(self):
        with open("Repositories/Configuracion.csv", "r", encoding="utf-8") as f:
            lineas = f.readlines()

            if len(lineas)>1:
                datos = lineas[1].strip().split(",")

                self.music = float(datos[0])
                self.ambience = float(datos[1])
                self.brillo = float(datos[2])
                self.sensibildad = float(datos[3])
                self.keyboard = int(datos[4])


        
