import pygame
from MainMenu.Chapters import Chapters
from MainMenu.LoggedMenu import LoggedMenu
from MainMenu.LoggedMenu import PopUpLogOut
from MainMenu.Register import Register
from TheColorCode import TheColorCode
import configuraciones #Si desea cambiar alguna configuración solo ve a este archivo
from libro import Libro
from MainMenu.Menu import Menu
from MainMenu.LoginIn import LoginInterface as Login

pygame.init()

info = pygame.display.Info()
width_pestana = info.current_w
height_pestana = info.current_h

login_interface = None
register_interface = None
MenuLogged = None
LogOut = None
Capitulos = None
ColorCode = None

ventana = pygame.display.set_mode((width_pestana, height_pestana))
pygame.display.set_caption("Dentro del Espectro")
opcion = 0

menu = Menu()

run = True
reloj = pygame.time.Clock()

login = False

while run:
    reloj.tick(60)

    for event in pygame.event.get():
        opcion = 0
        
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not login:
                opcion = menu.Option(event)
            else:
                opcion = MenuLogged.Option(event)

            if opcion == 1:
                login_interface = Login()
            elif opcion==2:
                register_interface = Register()
            elif opcion==3:
                pass
            elif opcion==4:
                pass
            elif opcion=="logout":
                LogOut = PopUpLogOut()
            elif opcion==6:
                Capitulos = Chapters()

        if LogOut:
            result = LogOut.Option(event)
            if result == "Yes":
                LogOut = None
                login = False
                MenuLogged = None
            elif result == "No":
                LogOut = None

        if login_interface:
            result = login_interface.Opciones(event)
            if result == "exit":
                login_interface = None
            elif result == "LoggedIn":
                login = True
                login_interface = None
                MenuLogged = LoggedMenu()
            elif result == "Register":
                register_interface = Register()
                login_interface = None

        if register_interface:
            result = register_interface.Opciones(event)
            if result == "exit":
                register_interface = None
            elif result == "LogIn":
                login_interface = Login()
                register_interface = None
            elif result == "Register":
                register_interface.Register()
                register_interface = None
        
        if Capitulos:
            result = Capitulos.Option(event)
            if result == "exit":
                Capitulos = None
            elif result == "ColorCode":
                Capitulos = None
                ColorCode = TheColorCode()
            elif result == "Chapter2":
                pass
            elif result == "Chapter3":
                pass

    if not login:
        menu.draw(ventana)
    else:
        MenuLogged.draw(ventana)
    if login_interface:
        login_interface.draw(ventana)
    if register_interface:
        register_interface.draw(ventana)
    if LogOut:
        LogOut.draw(ventana)
    if ColorCode:
        ColorCode.run()
    if Capitulos:
        Capitulos.draw(ventana)
    pygame.display.flip()