import pygame

class Player:
    """Clase que representa al jugador principal."""

    def __init__(
            self, 
            x: int ,
            y: int ,
            width: int ,
            height: int ,
            color: tuple ,
            speed: int 
        ):
        """
        Inicializa el jugador.
        
        Args:
            x: Posición inicial en el eje X
            y: Posición inicial en el eje Y
            width: Ancho del jugador
            height: Alto del jugador
            color: Color del jugador en formato RGB
            speed: Velocidad de movimiento
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        
        # Velocidades actuales en cada eje
        self.vel_x = 0
        self.vel_y = 0
        
        # Crear el rectángulo del jugador
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def move_up(self):
        """Mueve al jugador hacia arriba."""
        self.vel_y = -self.speed
    
    def move_down(self):
        """Mueve al jugador hacia abajo."""
        self.vel_y = self.speed
    
    def move_left(self):
        """Mueve al jugador hacia la izquierda."""
        self.vel_x = -self.speed
    
    def move_right(self):
        """Mueve al jugador hacia la derecha."""
        self.vel_x = self.speed
    
    def update(self, screen_width: int, screen_height: int):
        """
        Actualiza la posición del jugador.
        
        Args:
            screen_width: Ancho de la pantalla para limitar el movimiento
            screen_height: Alto de la pantalla para limitar el movimiento
        """
        # Actualizar posición
        self.x += self.vel_x
        self.y += self.vel_y
        
        # Limitar el movimiento dentro de la pantalla
        if self.x < 0:
            self.x = 0
        elif self.x + self.width > screen_width:
            self.x = screen_width - self.width
        
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > screen_height:
            self.y = screen_height - self.height
        
        # Actualizar rectángulo
        self.rect.x = self.x
        self.rect.y = self.y
    
    def draw(self, screen: pygame.Surface):
        """
        Dibuja al jugador en la pantalla.
        
        Args:
            screen: Superficie de pygame donde dibujar
        """
        pygame.draw.rect(screen, self.color, self.rect)
    
    def handle_input(self, keys):
        """
        Maneja la entrada del teclado para el movimiento.
        
        Args:
            keys: Estado de las teclas obtenido de pygame.key.get_pressed()
        """
        # Resetear velocidades
        self.vel_x = 0
        self.vel_y = 0
        
        # Movimiento con teclas de dirección
        if keys[pygame.K_UP]:
            self.move_up()
        if keys[pygame.K_DOWN]:
            self.move_down()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()
