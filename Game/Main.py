import pygame
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

pygame.init()
pygame.init()

pygame.mixer.init()

info = pygame.display.Info()
width_pestana = info.current_w
height_pestana = info.current_h

login_interface = None
register_interface = None
MenuLogged = None
NewRound = None
LogOut = None
configuracion=None
Capitulos = None
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
            if not login and not configuracion:
                opcion = menu.Option(event)
            elif opcion==6:
                opcion = Capitulos.Option(event)
            elif login and not configuracion:
                opcion = MenuLogged.Option(event)
              
            if opcion == 1:
                login_interface = Login()
            elif opcion==2:
                register_interface = Register()
            elif opcion==3:
                configuracion = Config()
            elif opcion==4:
                pass
            elif opcion=="logout":
                LogOut = PopUpLogOut()
            elif opcion==5:
                game = TheColorCode()
                if game.cargar_partida():
                    game.run()
                else:
                    print("No hay partida guardada")
                                
            elif opcion==6:
                NewRound=PopUpNewRound()
                
        if configuracion:
            result = configuracion.Option(event)
            if result =="Back":
                configuracion = None
            
        if NewRound:
            result = NewRound.Option(event)
            if result=="Yes":
                NewRound = None
                Capitulos = Chapters()
            elif result=="No":
                NewRound=None

        if Capitulos:
            result = Capitulos.Option(event)
            if result == "Back":
                Capitulos = None
            elif result == "ColorCode":
                Capitulos = None
                ColorCode = TheColorCode()
            elif result == "MusicalCode":
                Capitulos = None
                MusicalC = musicalCode()
            elif result == "Chapter3":
                pass
            else:
                pass
            
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
                
        

    if not login and not Capitulos:
        menu.draw(ventana)
    elif login and not Capitulos:
        MenuLogged.draw(ventana)
    elif login and Capitulos:
        Capitulos.draw(ventana)
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

    if Capitulos:
        Capitulos.draw(ventana)
    if ColorCode:
        ColorCode.run()
    if MusicalC:
        MusicalC.run()

    
    overlay = pygame.Surface((width_pestana, height_pestana))
    overlay.fill((0, 0, 0))

    alpha = int((1 - brillo) * 200)  # puedes ajustar 200
    overlay.set_alpha(alpha)

    ventana.blit(overlay, (0, 0))
    
    pygame.display.flip()