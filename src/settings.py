class Settings:
    """Configuración global del juego."""
    
    # Ventana
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    FPS = 30
    TITLE = "Juego"
    BACKGROUND_COLOR = (0, 0, 0)
    
    # Jugador
    PLAYER_WIDTH = 50
    PLAYER_HEIGHT = 50
    PLAYER_COLOR = (0, 255, 0)
    PLAYER_SPEED = 5
    PLAYER_START_X = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2
    PLAYER_START_Y = SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2