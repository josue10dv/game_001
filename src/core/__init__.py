"""
Paquete core del juego.
Contiene componentes fundamentales y singleton patterns.

Módulos incluidos:
- game_window: Clase Singleton para manejar la ventana del juego.
"""

from .game_window import GameWindow

__all__ = [
    GameWindow
]
