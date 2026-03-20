import pygame
import configuraciones #Si desea cambiar alguna configuración solo ve a este archivo
from libro import Libro

pygame.init()

#Cargar imagenes
libro_image=[]
for i in range(9):
    img=pygame.image.load(f"media//elementos//libros//libro{i+1}.png")
    libro_image.append(img)

#Tamaño para la pantalla
ventana= pygame.display.set_mode((configuraciones.width_pestana, configuraciones.height_pestana))

#Crear objetos
objetos=[]
for i in range(9):
    objetos.append(Libro(100 + i*60, 300, libro_image[i]))

#Nombre de la pestaña
pygame.display.set_caption("The color code")

#Variables de movimiento con teclas a,s,d,w
mover_arriba=False
mover_abajo=False
mover_derecha=False
mover_izquierda=False

#Para que se quede abierta hasta que se cierre
run= True

#Lo usaré para controlar la velocidad del movimiento
reloj=pygame.time.Clock()

fondo= pygame.image.load("media//fondos//fondoRepisa.png").convert()

#Seleccionar el objeto con el mouse (arrastrarlo)
seleccionado=None

#Para que cuando lo toque con el mouse no se vaya lejos
offset_x = 0
offset_y = 0 #son posiciones relativas

while run:
    
    #Controlar los fps
    reloj.tick(configuraciones.fps)

    #Fondo
    ventana.blit(fondo, (0,0))

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
    for obj in objetos:
        obj.draw(ventana)

    #Movimiento del circulo del puntero
    pygame.draw.circle(ventana, configuraciones.color_puntero,(x,y),20, 2)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            
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
                for obj in objetos:
                    if obj.shape.collidepoint(event.pos):
                        seleccionado = obj
                        offset_x = obj.shape.x - event.pos[0]
                        offset_y = obj.shape.y - event.pos[1]
                        obj.agrandarLaEscala(1.1)
                        objetos.remove(obj)
                        objetos.append(obj)
                        break

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if seleccionado:
                    seleccionado.agrandarLaEscala(1)
                seleccionado = None

    if seleccionado: #este sirve para q no se mueva al arrastrarlo tampoco
        seleccionado.shape.x = x + offset_x
        seleccionado.shape.y = y + offset_y

pygame.quit()