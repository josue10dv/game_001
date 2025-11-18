import pygame
from ..game import Game

class EventHandler:
    """Gestor centralizado de eventos del juego."""
    
    def __init__(self, game: Game):
        """
        Inicializa el gestor de eventos.
        
        Args:
            game: Referencia a la instancia del juego
        """
        self.game = game
    
    def handle_events(self):
        """Procesa todos los eventos del juego."""
        events = pygame.event.get()
        
        # Procesar eventos discretos
        for event in events:
            self._handle_discrete_events(event)
        
        # Procesar input continuo (teclas mantenidas presionadas)
        self._handle_continuous_input()
    
    def _handle_discrete_events(self, event):
        """
        Maneja eventos discretos (un solo disparo).
        
        Args:
            event: Evento de pygame
        """
        if event.type == pygame.QUIT:
            self.game.running = False
        
        # Eventos de teclado
        if event.type == pygame.KEYDOWN:
            self._handle_keydown(event)
    
    def _handle_keydown(self, event):
        """
        Maneja eventos de tecla presionada.
        
        Args:
            event: Evento de pygame con información de la tecla
        """
        # Salir con ESC
        if event.key == pygame.K_ESCAPE:
            self.game.running = False
    
    def _handle_continuous_input(self):
        """Maneja input continuo como el movimiento del jugador."""
        keys = pygame.key.get_pressed()
        
        # Delegar el manejo de input al jugador
        if hasattr(self.game, 'player'):
            self.game.player.handle_input(keys)
