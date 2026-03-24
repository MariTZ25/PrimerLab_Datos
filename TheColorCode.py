import pygame
from libro import Libro
import random

class TheColorCode:
   
    def __init__(self):
        pygame.init()
        
        self.base_w = 1512
        self.base_h = 982
        
        #adaptarse a la pantalla
        info = pygame.display.Info()
        self.width = info.current_w
        self.height = info.current_h
        self.ventana = pygame.display.set_mode((self.width, self.height))

        self.libro_image=[]
        for i in range(9):
            img=pygame.image.load(f"Game/media//elementos//libros//libro{i+1}.png")
            self.libro_image.append(img)
            
            #Le asigno un color a cada libro
        self.nombres_libros = [
            "Rojo", "Naranja", "Rosa", "Amarillo",
            "Verde", "Celeste", "Azul", "Azul oscuro", "Morado"
        ]
        
        self.crearCondicion()
            
        self.running = True
        self.objetos=[]
        for i in range(9):
            x, y = self.scale(510 + i*60, 400)
            libro = Libro(x, y, self.libro_image[i])
            libro.nombre = self.nombres_libros[i]
            self.objetos.append(libro)

        #Para que se quede abierta hasta que se cierre
        #Lo usaré para controlar la velocidad del movimiento
        self.reloj=pygame.time.Clock()

        self.fondo= pygame.image.load("Game/media//fondos//fondoRepisa.png").convert()
        
        self.fondoGanar= pygame.image.load("Game/media//fondos//ganaste.png").convert()
        
        self.fondoPerder= pygame.image.load("Game/media//fondos//perdiste.png").convert()
        
        #Acá meto el botón de salir y un cuadrito detrás para saber si lo toqué o no
        self.finish= pygame.image.load("Game/media//elementos//Botones//finish.png").convert()
        size = self.scale(220, 90) 
        self.finish = pygame.transform.scale(self.finish, (int(size[0]), int(size[1])))
        x, y = self.scale(10, 10)
        self.finish_shape = self.finish.get_rect(topleft=(int(x), int(y)))
        #Para q el shape sea más chiquito que el botón
        self.finish_shape.inflate_ip(-30, -30)
        #Lo centra pq estaba achicando desde la esquina 
        self.finish_shape.center = self.finish.get_rect(topleft=(int(x), int(y))).center

        #Botón salir
        size_exit = self.scale(120, 50)
        x_exit = 30
        y_exit = self.height - int(size_exit[1]) - 20
        self.exit_shape = pygame.Rect(x_exit, y_exit, int(size_exit[0]), int(size_exit[1]))

        #Fuente de la letra
        self.font = pygame.font.SysFont("arial", 30)
        self.font_exit = pygame.font.SysFont("arial", 30)

        self.textos = []
        self.textos_info = []  

        #Le pongo un color diferente a cada palabra y le asigno el objeto asociado
        for nombre in self.default:
            color = (random.randint(50,255), random.randint(50,255), random.randint(50,255))
            texto = self.font.render(nombre, True, color)
            self.textos.append(texto)
            self.textos_info.append(nombre)  

        #Seleccionar el objeto con el mouse (arrastrarlo)
        self.seleccionado=None
        #Para que cuando lo toque con el mouse no se vaya lejos
        self.offset_x = 0
        self.offset_y = 0 #son posiciones relativas

        self.terminado = False
        self.Ganar = False

        self.tiempo_inicio = pygame.time.get_ticks()  # timer
        self.duracion = 30000  # timer

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

            fondo_scaled = pygame.transform.smoothscale(self.fondo, (w, h))
            self.ventana.blit(fondo_scaled, (0,0))

            self.ventana.blit(self.finish, (self.finish_shape.x, self.finish_shape.y))

            pygame.draw.rect(self.ventana, ((224, 186, 224)), self.exit_shape)
            texto_exit = self.font_exit.render("Salir", True, (255,255,255))
            self.ventana.blit(texto_exit, (self.exit_shape.x + 14, self.exit_shape.y + 4))

            segundos = max(0, tiempo_restante // 1000)
            texto_timer = self.font.render(f"Tiempo: {segundos}", True, (232, 21, 232))
            self.ventana.blit(texto_timer, (50, 100))

            margen = 300
            espacio = 20
            y_texto = self.scale(0, 50)[1]

            x_actual = margen
            for texto in self.textos:
                if x_actual + texto.get_width() > self.width - margen:
                    x_actual = margen
                    y_texto += texto.get_height() + 10

                self.ventana.blit(texto, (x_actual, y_texto))
                x_actual += texto.get_width() + espacio

            mouse_pos=pygame.mouse.get_pos()
            x=mouse_pos[0]
            y=mouse_pos[1]

            for obj in self.objetos:
                obj.draw(self.ventana)

            pygame.draw.circle(
                self.ventana,
                (255,255,255),
                (x,y),
                int(20 * w / self.base_w),
                2
            )

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running=False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:

                        if self.finish_shape.collidepoint(event.pos):
                            self.terminado = True

                        if self.exit_shape.collidepoint(event.pos):
                            self.running = False

                        for obj in self.objetos:
                            if obj.shape.collidepoint(event.pos):
                                self.seleccionado = obj
                                self.offset_x = obj.shape.x - event.pos[0]
                                self.offset_y = obj.shape.y - event.pos[1]
                                obj.agrandarLaEscala(1.1)
                                self.objetos.remove(obj)
                                self.objetos.append(obj)
                                break
                        movidos = [self.seleccionado]
                        cambio = True
                        while cambio:
                            cambio = False
                            for obj in self.objetos:
                             for otro in self.objetos:
                              if obj != otro and obj.shape.colliderect(otro.shape):
                                if obj not in movidos:
                                    otro.shape.x = obj.shape.right + 0.2
                                    movidos.append(obj)
                                    cambio = True

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if self.seleccionado:
                            self.seleccionado.agrandarLaEscala(1)
                        self.seleccionado = None

            if self.seleccionado:
                self.seleccionado.shape.x = x + self.offset_x
                self.seleccionado.shape.y = y + self.offset_y

               

               
            
            if self.terminado:
               self.verificarCondiciones()
               if self.Ganar:
                   print("Felicidades, ganaste")
                   self.result=True
               else:
                   print("Perdiste bobo")
                   self.result=False

               from pantalla_final import PantallaFinal
               pantalla = PantallaFinal(self.result, self.width, self.height, self.base_w, self.base_h)
               pantalla.run()

               self.running = False
               self.terminado = False
                   
    def crearCondicion(self):
     self.default = self.nombres_libros[:]
     random.shuffle(self.default)
     return(self.default)
         
    def verificarCondiciones(self):
     self.definirPosicionesReales()
     if self.default == self.listaPosicionesReales:
         self.Ganar=True
     else:
         self.Ganar=False
            
    def definirPosicionesReales(self):
        ordenados = sorted(self.objetos, key=lambda obj: obj.shape.x)
        self.listaPosicionesReales = []
        for obj in ordenados:
            self.listaPosicionesReales.append(obj.nombre)
        return self.listaPosicionesReales
