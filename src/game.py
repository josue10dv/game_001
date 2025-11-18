import pygame
from .core.game_window import GameWindow
from .settings import Settings as ST
from .entities.player import Player
from .system.event_handler import EventHandler

class Game:
    running: bool
    window: GameWindow
    clock: pygame.time.Clock

    def __init__(self):
        self.window = GameWindow(
            ST.SCREEN_WIDTH,
            ST.SCREEN_HEIGHT
        )
        self.window.set_title(ST.TITLE)
        self.window.set_background_color(ST.BACKGROUND_COLOR)
        self.running = True
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.fps = ST.FPS
        
        # Inicializar el jugador (usa valores de Settings por defecto)
        self.player = Player(
            ST.PLAYER_START_X,
            ST.PLAYER_START_Y,
            ST.PLAYER_WIDTH,
            ST.PLAYER_HEIGHT,
            ST.PLAYER_COLOR,
            ST.PLAYER_SPEED
        )
        
        # Inicializar el gestor de eventos
        self.event_handler = EventHandler(self)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)

        self.cleanup()
            

    def handle_events(self):
        """Maneja todos los eventos de entrada usando el EventHandler."""
        self.event_handler.handle_events()
    
    def update(self):
        """Actualiza la lógica del juego."""
        self.player.update(ST.SCREEN_WIDTH, ST.SCREEN_HEIGHT)
    
    def draw(self):
        """Dibuja todos los elementos en la pantalla."""
        self.window.screen.fill(self.window.background_color)
        self.player.draw(self.window.screen)
        self.window.update()

    def cleanup(self):
        """Limpia los recursos y cierra pygame."""
        print("Cerrando juego...")
        pygame.quit()
            
            
        
