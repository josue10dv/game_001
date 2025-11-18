import pygame

class GameWindow:
    """
    Clase singleton que maneja la ventana del juego usando pygame.
    """

    # Variable de clase para almacenar la instancia única
    _instance = None
    
    def __new__(cls, width=800, height=600):
        """
        Crea una nueva instancia de la clase o devuelve la instancia existente.
        """
        if cls._instance is None:
            cls._instance = super(GameWindow, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, width=800, height=600):
        """
        Inicializa pygame y crea la ventana si no ha sido inicializada.
        """
        if self._initialized:
            return
        
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.width, self.height)
        )
        self.clock = pygame.time.Clock()
        self._initialized = True

    def set_title(self, title: str):
        """Establece el título de la ventana."""
        pygame.display.set_caption(title)
    
    def set_background_color(self, color: tuple):
        """Establece el color de fondo de la ventana."""
        self.background_color = color
        self.screen.fill(self.background_color)
    
    def update(self):
        """Actualiza la pantalla y maneja el reloj."""
        pygame.display.flip()
