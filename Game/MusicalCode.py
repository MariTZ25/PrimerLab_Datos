import pygame
from HashTable import HashTable
import random
from MainMenu.Config import Config

tabla_partida = HashTable()

class musicalCode:
   def __init__(self):
  #Musica y efectos sonoros
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("Music/bulla.mp3")
        self.primero= pygame.mixer.Sound("Music/beep1.mp3")
        self.segundo= pygame.mixer.Sound("Music/beep2.mp3")
        self.tercero= pygame.mixer.Sound("Music/beep3.mp3")
        self.cuarto= pygame.mixer.Sound("Music/beep4.mp3")
        self.quinto= pygame.mixer.Sound("Music/beep5.mp3")
        self.sexto= pygame.mixer.Sound("Music/beep6.mp3")
        pygame.mixer.music.play(-1)
        self.config = Config()
        
        
        self.base_w = 1512
        self.base_h = 982
        
        #adaptarse a la pantalla
        info = pygame.display.Info()
        self.width = info.current_w
        self.height = info.current_h
        self.ventana = pygame.display.set_mode((self.width, self.height))
        
        #Fondo
        self.fondo= pygame.image.load("Game/media/fondos/fondoPuzzle2.png").convert_alpha()
        self.img_correcto = pygame.image.load("Game/media/elementos/Botones/correcto.png").convert_alpha()
        self.img_error = pygame.image.load("Game/media/elementos/Botones/error.png").convert_alpha()
        
        
        #objetos (beets) 
        self.running = True
        self.objetos=[]
        self.reloj=pygame.time.Clock()
     
        #Botón salir
        size_exit = self.scale(120, 50)
        x_exit = 30
        y_exit = self.height - int(size_exit[1]) - 20
        self.exit_shape = pygame.Rect(x_exit, y_exit, int(size_exit[0]), int(size_exit[1]))

        size_repeat = self.scale(120, 50)
        x_repeat = self.width - int(size_repeat[0]) - 30
        y_repeat = self.height - int(size_repeat[1]) - 20
        self.repeat_shape = pygame.Rect(x_repeat, y_repeat, int(size_repeat[0]), int(size_repeat[1]))

        #Fuente de la letra
        self.font = pygame.font.SysFont("arial", 30)
        self.font_exit = pygame.font.SysFont("arial", 30)
        
        
        self.terminado = False
        self.Ganar = False

        self.tiempo_inicio = pygame.time.get_ticks()  # timer
        self.duracion = 120000  # timer
        
        self.sonidos = {
            1: self.primero,
            2: self.segundo,
            3: self.tercero,
            4: self.cuarto,
            5: self.quinto,
            6: self.sexto
        }

        self.secuencia = [random.randint(1,6) for _ in range(6)]
        self.silencios = random.sample(range(len(self.secuencia)), 2)

        self.input_usuario = []
        self.mostrar = []

        self.visual = ""

   def tocar(self, x_pos, y_pos):
    if 250 < x_pos < 650 and 50 < y_pos < 250:
        self.rect_actual = pygame.Rect(250,50,400,200)
        self.caso=1
        return self.caso

    elif 250 < x_pos < 650 and 250 <= y_pos < 470:
        self.rect_actual = pygame.Rect(250,250,400,220)
        self.caso=2
        return self.caso

    elif 250 < x_pos < 650 and 470 <= y_pos < 690:
        self.rect_actual = pygame.Rect(250,470,400,220)
        self.caso=3
        return self.caso
    elif 650 <= x_pos < 1050 and 50 < y_pos < 250:
        self.rect_actual = pygame.Rect(650,50,400,200)
        self.caso=4
        return self.caso
    elif 650 < x_pos < 1050 and 250 <= y_pos < 470:
        self.rect_actual = pygame.Rect(650,250,400,220)
        self.caso=5
        return self.caso
    elif 650 < x_pos < 1050 and 470 <= y_pos < 690:
        self.rect_actual = pygame.Rect(650,470,400,220)
        self.caso=6
        return self.caso
    return None

   def reproducir_secuencia(self):
        self.visual = ""
        for i, valor in enumerate(self.secuencia):
            if i in self.silencios:
                self.visual += "_"
                pygame.mixer.music.set_volume(1.0)
                pygame.time.delay(1000)
            else:
                self.visual += "*"
                pygame.mixer.music.set_volume(0.0)
                self.sonidos[valor].play()
                pygame.time.delay(1000)
        pygame.mixer.music.set_volume(1.0)

   def cambiar_silencios(self):
        self.silencios = random.sample(range(len(self.secuencia)), 2)
            
   def scale(self, x, y):
        return (x * self.width / self.base_w, y * self.height / self.base_h)

   def run(self):

        while self.running:                 
            self.reloj.tick(60)
            w, h = self.ventana.get_size()

            tiempo_actual = pygame.time.get_ticks()
            tiempo_restante = self.duracion - (tiempo_actual - self.tiempo_inicio)
            if tiempo_restante <= 0:
                print("Se acabó el tiempo")
                self.result=False
                from pantalla_final import PantallaFinal
                pantalla = PantallaFinal(False, self.width, self.height, self.base_w, self.base_h)
                pantalla.run()
                self.running = False
                
            #dibujar el fondo
            fondo_scaled = pygame.transform.scale(self.fondo, (w, h))
            self.ventana.blit(fondo_scaled, (0,0))
            
            #para salir
            pygame.draw.rect(self.ventana, ((224, 186, 224)), self.exit_shape)
            texto_exit = self.font_exit.render("Salir", True, (255,255,255))
            self.ventana.blit(texto_exit, (self.exit_shape.x + 16, self.exit_shape.y + 4))

            pygame.draw.rect(self.ventana, (186, 224, 186), self.repeat_shape)
            texto_repeat = self.font_exit.render("Play", True, (255,255,255))
            self.ventana.blit(texto_repeat, (self.repeat_shape.x + 10, self.repeat_shape.y + 4))
            
            #dibujar el timer
            segundos = max(0, tiempo_restante // 1000)
            texto_timer = self.font.render(f"Tiempo: {segundos}", True, (255,255,255))
            self.ventana.blit(texto_timer, (55, 160))

            if self.visual:
                texto_visual = self.font.render(self.visual, True, (255,255,255))
                self.ventana.blit(texto_visual, (self.width - 200, 100))

            ahora = pygame.time.get_ticks()
            nuevas = []
            for img, rect, t in self.mostrar:
                if ahora - t < 1000:
                    img_scaled = pygame.transform.scale(img, (rect.width, rect.height))
                    self.ventana.blit(img_scaled, rect)
                    nuevas.append((img, rect, t))
            self.mostrar = nuevas
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running=False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:

                        if self.repeat_shape.collidepoint(event.pos):
                            self.input_usuario = []
                            self.cambiar_silencios()
                            self.reproducir_secuencia()
                            continue

                        if self.exit_shape.collidepoint(event.pos):
                            self.guardar_partida()
                            self.running = False
                            continue

                        caso = self.tocar(event.pos[0], event.pos[1])

                        if caso:

                            match caso:
                                case 1:
                                    self.primero.play()
                                case 2:
                                    self.segundo.play()
                                case 3:
                                    self.tercero.play()
                                case 4:
                                    self.cuarto.play()
                                case 5:
                                    self.quinto.play()
                                case 6:
                                    self.sexto.play()
                                case _:
                                    print("fuera de sitio")

                            index = len(self.input_usuario)

                            if index < len(self.secuencia):
                                esperado = self.secuencia[index]

                                if caso == esperado:
                                    self.mostrar.append((self.img_correcto, self.rect_actual, pygame.time.get_ticks()))
                                    self.input_usuario.append(caso)

                                    if len(self.input_usuario) == len(self.secuencia):
                                        self.Ganar = True
                                        from pantalla_final import PantallaFinal
                                        pantalla = PantallaFinal(True, self.width, self.height, self.base_w, self.base_h)
                                        pantalla.run()
                                        self.running = False

                                else:
                                    self.mostrar.append((self.img_error, self.rect_actual, pygame.time.get_ticks()))
                                    self.input_usuario = []