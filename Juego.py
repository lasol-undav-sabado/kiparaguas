import pygame
import Personaje

from pygame.locals import *
from Personaje import *

class juego:
    def __init__(self):
        self.running = False
        self.display_surf = None
        self.size = 640, 400
        
 
    def initialize(self):
        if(not self.running):
            pygame.init()
            self.display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
            self.display_surf.fill((255,255,255))
            pygame.display.set_caption("Paraguas")
            self.kiper = personaje(self.display_surf)
            self.objeto = objeto("assets/kiper.jpg", 1000, 1)
            self.running = True

    def onEvent(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            self.kiper.move(event.key)
            
    def onLoop(self):
        pass
    
    def onRender(self):
        self.kiper.render(self.display_surf)
        self.objeto.render(self.display_surf)

    def cleanup(self):
        pygame.quit()

    def run(self):
        self.initialize()
        while( self.running ):
            for event in pygame.event.get():
                self.onEvent(event)
            self.onLoop()
            self.onRender()
            pygame.time.delay(50)
            pygame.display.flip()
    
        self.cleanup()
    


if(__name__ == "__main__"):
    paraguas = juego()
    paraguas.run()
