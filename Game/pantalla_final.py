import pygame

class PantallaFinal:

    def __init__(self, gano, width, height, base_w, base_h):
        pygame.init()
        
       


        self.width = width
        self.height = height
        self.base_w = base_w
        self.base_h = base_h

        self.ventana = pygame.display.set_mode((self.width, self.height))

        # Cargar fondos
        if gano:
         self.fondo = pygame.image.load("Game/media//fondos//ganaste.png").convert()
             #Efectos de sonido
         pygame.mixer.music.load("Music/ganar.mp3")
         pygame.mixer.music.play(-1)
        else:
         self.fondo = pygame.image.load("Game/media//fondos//perdiste.png").convert()
            #Efectos de sonido
         pygame.mixer.music.load("Music/perder.mp3")
         pygame.mixer.music.play(-1)

        # Botón salir
        size_w = int(120 * self.width / self.base_w)
        size_h = int(50 * self.height / self.base_h)

        x_exit = 30
        y_exit = self.height - size_h - 20

        self.exit_shape = pygame.Rect(x_exit, y_exit, size_w, size_h)

        self.font = pygame.font.SysFont("arial", 30)

        self.running = True
        self.reloj = pygame.time.Clock()

    def run(self):

        while self.running:
            self.reloj.tick(60)

            w, h = self.ventana.get_size()

            fondo_scaled = pygame.transform.smoothscale(self.fondo, (w, h))
            self.ventana.blit(fondo_scaled, (0,0))

            pygame.draw.rect(self.ventana, ((224, 186, 224)), self.exit_shape)
            texto_exit = self.font.render("Salir", True, (255,255,255))
            self.ventana.blit(texto_exit, (self.exit_shape.x + 14, self.exit_shape.y + 4))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.exit_shape.collidepoint(event.pos):
                            self.running = False
                            pygame.mixer.music.play()