import time

import pygame
import sys
from MainMenu.Chapters import Chapters
from MainMenu.LoggedMenu import LoggedMenu
from MainMenu.LoggedMenu import PopUpLogOut, PopUpNewRound
from MainMenu.Register import Register
from TheColorCode import TheColorCode
from MainMenu.Config import Config
import configuraciones #Si desea cambiar alguna configuración solo ve a este archivo
from libro import Libro
from MainMenu.Menu import Menu
from MainMenu.LoginIn import LoginInterface as Login
from MusicalCode import musicalCode

sys.path.append("Persistence")
from HashTable import HashTable

pygame.init()

pygame.mixer.init()

info = pygame.display.Info()
width_pestana = info.current_w
height_pestana = info.current_h

PopUp = False
continuar = False


login_interface = None
register_interface = None
MenuLogged = None
NewRound = None
LogOut = None
configuracion=None
Capitulos = None
game = None
ColorCode = None
MusicalC= None



config = Config()

music = config.music
ambience = config.ambience
sensibildad=config.sensibildad
keyboard = config.keyboard
brillo=config.brillo

ventana = pygame.display.set_mode((width_pestana, height_pestana))
pygame.display.set_caption("Dentro del Espectro")
opcion = 0

global usuarios
usuarios = HashTable()
usuarios.csv_to_hashtable("Repositories/Usuarios.csv")

menu = Menu()
run = True
reloj = pygame.time.Clock()

login = False

while run:
    reloj.tick(60)
    clicked = False

    for event in pygame.event.get():
        opcion = 0
        
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not clicked:
            if not login and not configuracion and not Capitulos:
                opcion = menu.Option(event)
            elif login and not configuracion and not Capitulos:
                opcion = MenuLogged.Option(event)
              
            if opcion == 1:
                login_interface = Login(usuarios)
            elif opcion==2:
                register_interface = Register(usuarios)
            elif opcion==3:
                configuracion = Config()
            elif opcion==4:
                pass
            elif opcion=="logout":
                LogOut = PopUpLogOut()
            elif opcion==5:
                continuar = True
                Capitulos = Chapters()
            elif opcion==6:
                NewRound=PopUpNewRound()
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            clicked = False
                
        if configuracion:
            result = configuracion.Option(event)
            if result =="Back":
                configuracion = None
            
        if NewRound:
            continuar = False
            PopUp = True
            result = NewRound.Option(event)
            if result=="Yes":
                NewRound = None
                Capitulos = Chapters()
                PopUp = False
            elif result=="No":
                NewRound=None
                PopUp = False

        if Capitulos and not NewRound and not PopUp:
            result = Capitulos.Option(event)
            if result == "Back":
                Capitulos = None
                continuar = False
            elif result == "ColorCode":
                Capitulos = None
                if not continuar:
                    ColorCode = TheColorCode()
                else:
                    game = TheColorCode()
            elif result == "MusicalCode":
                Capitulos = None
                if not continuar:
                    MusicalC = musicalCode()
                else:
                    game = musicalCode()
            elif result == "Chapter3":
                pass
            if result is not None:
                NewRound = None
            else:
                pass
            
        if LogOut:
            PopUp = True
            result = LogOut.Option(event)
            if result == "Yes":
                LogOut = None
                login = False
                MenuLogged = None
                PopUp = False
            elif result == "No":
                LogOut = None
                PopUp = False

        if login_interface:
            PopUp = True
            result = login_interface.Opciones(event)
            if result == "exit":
                login_interface = None
                PopUp = False
            elif result == "LoggedIn":
                login = True
                login_interface = None
                MenuLogged = LoggedMenu()
                PopUp = False
            elif result == "Register":
                register_interface = Register(usuarios)
                login_interface = None
                PopUp = False
                    
        if register_interface:
            PopUp = True
            result = register_interface.Opciones(event)
            if result == "exit":
                register_interface = None
                PopUp = False
            elif result == "LogIn":
                login_interface = Login(usuarios)
                register_interface = None
                PopUp = False
            elif result == "Register":
                register_interface.Register()
                register_interface = None
                PopUp = False
                
                
        

    if not login and not Capitulos:
        menu.draw(ventana)
    elif login and not Capitulos:
        MenuLogged.draw(ventana)
    if NewRound:
        NewRound.draw(ventana)
    if login_interface:
        login_interface.draw(ventana)
    if register_interface:
        register_interface.draw(ventana)
    if LogOut:
        LogOut.draw(ventana)
    if configuracion:
        configuracion.draw(ventana)
        music = configuracion.music
        brillo = configuracion.brillo
        sensibildad = configuracion.sensibildad
        keyboard = configuracion.keyboard
        ambience = configuracion.ambience

    if Capitulos and not NewRound and not PopUp:
        Capitulos.draw(ventana)

    if ColorCode:
        ColorCode.run()
    if MusicalC:
        MusicalC.run()
    if continuar and game:
        game.cargar_partida()
        game.run()
    

    
    overlay = pygame.Surface((width_pestana, height_pestana))
    overlay.fill((0, 0, 0))

    alpha = int((1 - brillo) * 200)  # puedes ajustar 200
    overlay.set_alpha(alpha)

    ventana.blit(overlay, (0, 0))
    
    pygame.display.flip()