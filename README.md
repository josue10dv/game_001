# Game 001 - Juego con Pygame

Proyecto de juego desarrollado con Python y Pygame que implementa un sistema básico de movimiento de jugador con una arquitectura modular y escalable.

## 📋 Descripción

Este es un juego 2D simple que demuestra los fundamentos de desarrollo de videojuegos con Pygame. El jugador controla un cuadrado verde que puede moverse libremente por la pantalla usando las teclas de dirección.

## 🎮 Características

- Control de jugador con teclas de dirección (↑ ↓ ← →)
- Sistema de colisión con los bordes de la pantalla
- Arquitectura modular y organizada
- Gestión centralizada de eventos
- Configuración centralizada de parámetros del juego
- Patrón Singleton para la ventana del juego

## 🏗️ Arquitectura del Proyecto

El proyecto sigue una estructura modular que separa las responsabilidades en diferentes componentes:

```
game_001/
│
├── main.py                 # Punto de entrada del juego
├── requirements.txt        # Dependencias del proyecto
│
└── src/                    # Código fuente principal
    ├── __init__.py
    ├── game.py            # Clase principal del juego (Game Loop)
    ├── settings.py        # Configuración global del juego
    │
    ├── core/              # Componentes centrales
    │   ├── __init__.py
    │   └── game_window.py # Gestión de la ventana (Singleton)
    │
    ├── entities/          # Entidades del juego
    │   └── player.py      # Clase del jugador
    │
    └── system/            # Sistemas del juego
        ├── __init__.py
        └── event_handler.py # Gestor de eventos
```

### Componentes Principales

#### 1. **main.py**
Punto de entrada de la aplicación. Instancia y ejecuta el juego.

#### 2. **src/game.py** - Clase `Game`
Núcleo del juego que implementa el Game Loop clásico:
- **Inicialización**: Configura la ventana, el jugador y los sistemas
- **Game Loop**: Ciclo principal con tres fases:
  - `handle_events()`: Procesa eventos de entrada
  - `update()`: Actualiza la lógica del juego
  - `draw()`: Renderiza los elementos en pantalla
- **Cleanup**: Libera recursos al cerrar

#### 3. **src/settings.py** - Clase `Settings`
Configuración centralizada de todos los parámetros del juego:
- Dimensiones de la ventana (600x600)
- FPS objetivo (30)
- Propiedades del jugador (tamaño, color, velocidad)
- Colores y título

#### 4. **src/core/game_window.py** - Clase `GameWindow`
Implementa el patrón Singleton para gestionar la ventana de Pygame:
- Garantiza una única instancia de la ventana
- Inicializa Pygame y la pantalla
- Proporciona métodos para configurar título y color de fondo

#### 5. **src/entities/player.py** - Clase `Player`
Representa al jugador con las siguientes capacidades:
- Movimiento en 4 direcciones
- Colisión con los bordes de la pantalla
- Renderizado del sprite (rectángulo coloreado)
- Manejo de input del teclado

#### 6. **src/system/event_handler.py** - Clase `EventHandler`
Gestor centralizado de eventos que maneja:
- Eventos discretos (cerrar ventana, tecla ESC)
- Input continuo (teclas mantenidas presionadas)
- Delegación del input al jugador

## 🎯 Funcionamiento

### Flujo de Ejecución

1. **Inicio**: `main.py` crea una instancia de `Game` y llama a `run()`

2. **Game Loop** (se repite mientras `running = True`):
   ```
   ┌─────────────────────────────────────┐
   │  1. handle_events()                 │
   │     - Procesa eventos de Pygame     │
   │     - Detecta input del jugador     │
   ├─────────────────────────────────────┤
   │  2. update()                        │
   │     - Actualiza posición del jugador│
   │     - Aplica colisiones             │
   ├─────────────────────────────────────┤
   │  3. draw()                          │
   │     - Limpia la pantalla            │
   │     - Dibuja el jugador             │
   │     - Actualiza el display          │
   ├─────────────────────────────────────┤
   │  4. clock.tick(FPS)                 │
   │     - Mantiene el framerate         │
   └─────────────────────────────────────┘
   ```

3. **Finalización**: Se ejecuta `cleanup()` para cerrar Pygame limpiamente

### Controles

- **Flechas direccionales (↑ ↓ ← →)**: Mover al jugador
- **ESC**: Salir del juego
- **Cerrar ventana (X)**: Salir del juego

### Sistema de Movimiento

El jugador se mueve con una velocidad constante definida en `Settings.PLAYER_SPEED`:
- La velocidad se aplica a los ejes X e Y independientemente
- El movimiento está limitado por los bordes de la pantalla
- Las velocidades se resetean cada frame y se recalculan según el input

## 🚀 Instalación y Ejecución

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**

2. **Navegar al directorio del proyecto**
   ```powershell
   cd c:\Users\Skinny69\Desktop\ET\UTE\game_001
   ```

3. **Instalar las dependencias**
   ```powershell
   pip install -r requirements.txt
   ```

### Ejecutar el Juego

```powershell
python main.py
```

## 🔧 Configuración

Puedes modificar los parámetros del juego editando el archivo `src/settings.py`:

```python
# Cambiar tamaño de ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Modificar propiedades del jugador
PLAYER_WIDTH = 75
PLAYER_HEIGHT = 75
PLAYER_COLOR = (255, 0, 0)  # Cambiar a rojo
PLAYER_SPEED = 10           # Aumentar velocidad

# Ajustar FPS
FPS = 60
```

## 🛠️ Tecnologías Utilizadas

- **Python 3**: Lenguaje de programación
- **Pygame 2.6.1**: Biblioteca para desarrollo de videojuegos

## 📦 Dependencias

Las dependencias están especificadas en `requirements.txt`:
- pygame==2.6.1

## 🔮 Posibles Mejoras

Este proyecto sirve como base para implementar:

- [ ] Enemigos y sistemas de combate
- [ ] Sistema de puntuación
- [ ] Múltiples niveles
- [ ] Sonidos y música
- [ ] Animaciones del jugador
- [ ] Diferentes tipos de movimiento (aceleración, salto)
- [ ] Sistema de colisiones más avanzado
- [ ] Power-ups y objetos coleccionables
- [ ] Menú principal y pantalla de game over
- [ ] Sistema de guardado

## 📝 Notas de Desarrollo

- El proyecto usa type hints para mejor documentación del código
- La arquitectura permite fácil extensión para nuevas entidades y sistemas
- El patrón Singleton en `GameWindow` previene múltiples ventanas
- El `EventHandler` centraliza toda la lógica de input, facilitando su modificación

## 👨‍💻 Autor

Proyecto educativo desarrollado como base para aprendizaje de desarrollo de videojuegos con Pygame.

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.
