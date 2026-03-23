import pygame
import configuraciones #Si desea cambiar alguna configuración solo ve a este archivo
from libro import Libro

class TheColorCode:
    pygame.init()
    def __init__(self):

        self.ventana = pygame.display.set_mode((configuraciones.width_pestana, configuraciones.height_pestana))

        self.libro_image=[]
        for i in range(9):
            img=pygame.image.load(f"Game/media//elementos//libros//libro{i+1}.png")
            self.libro_image.append(img)

        self.running = True
        self.objetos=[]
        for i in range(9):
            self.objetos.append(Libro(100 + i*60, 300, self.libro_image[i]))

        #Para que se quede abierta hasta que se cierre
        #Lo usaré para controlar la velocidad del movimiento
        self.reloj=pygame.time.Clock()

        self.fondo= pygame.image.load("Game/media//fondos//fondoRepisa.png").convert()

        #Seleccionar el objeto con el mouse (arrastrarlo)
        self.seleccionado=None

     #Para que cuando lo toque con el mouse no se vaya lejos
        self.offset_x = 0
        self.offset_y = 0 #son posiciones relativas

    def run(self):
        mover_derecha = False
        mover_izquierda = False
        mover_arriba = False
        mover_abajo = False

        while self.run:                 
            #Controlar los fps
            self.reloj.tick(configuraciones.fps)

            #Fondo
            self.ventana.blit(self.fondo, (0,0))

            #Actualizar la posición del mouse
            #Obtener la posición del mouse
            mouse_pos=pygame.mouse.get_pos()
            x=mouse_pos[0]
            y=mouse_pos[1]

            #Para calcular el movimiento del objeto
            delta_x=0
            delta_y=0

            if (mover_derecha):
                delta_x=configuraciones.velocidad
            if (mover_izquierda):
                delta_x=-configuraciones.velocidad
            if (mover_arriba):
                delta_y=-configuraciones.velocidad
            if (mover_abajo):
                delta_y=configuraciones.velocidad

            #Dibujar los libros
            for obj in self.objetos:
                obj.draw(self.ventana)

            #Movimiento del circulo del puntero
            pygame.draw.circle(self.ventana, configuraciones.color_puntero,(x,y),20, 2)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run=False
                    
                    #Para cuando se presiona la tecla
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_a:
                        mover_izquierda=True
                    if event.key==pygame.K_d:
                        mover_derecha=True
                    if event.key==pygame.K_w:
                        mover_arriba=True
                    if event.key==pygame.K_s:
                        mover_abajo=True

                #Para cuando se suelta la tecla
                if event.type == pygame.KEYUP:
                    if event.key==pygame.K_a:
                        mover_izquierda=False
                    if event.key==pygame.K_d:
                        mover_derecha=False
                    if event.key==pygame.K_w:
                        mover_arriba=False
                    if event.key==pygame.K_s:
                        mover_abajo=False
                        
                #Seleccionar el objeto con el mouse (arrastrarlo)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for obj in self.objetos:
                            if obj.shape.collidepoint(event.pos):
                                self.seleccionado = obj
                                self.offset_x = obj.shape.x - event.pos[0]
                                self.offset_y = obj.shape.y - event.pos[1]
                                obj.agrandarLaEscala(1.1)
                                self.objetos.remove(obj)
                                self.objetos.append(obj)
                                break

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if self.seleccionado:
                            self.seleccionado.agrandarLaEscala(1)
                        self.seleccionado = None

            if self.seleccionado: #este sirve para q no se mueva al arrastrarlo tampoco
                self.seleccionado.shape.x = x + self.offset_x
                self.seleccionado.shape.y = y + self.offset_y

        pygame.quit()