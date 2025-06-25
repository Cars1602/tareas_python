import pygame
import sys
import tkinter as tk
from tkinter import messagebox
import math
import random

# Inicialización de Pygame
pygame.init()

# Configuración de Tkinter para la pantalla de inicio
def start_screen():
    root = tk.Tk()
    root.title("Pacman - Menú de Inicio")
    root.geometry("300x200")
    
    def start_game():
        root.destroy()
        main_game()
    
    def show_controls():
        messagebox.showinfo("Controles", "Usa las flechas del teclado para mover a Pacman\n\nObjetivo: Come todos los puntos\n\nEvita a los fantasmas!")
    
    tk.Label(root, text="PACMAN", font=("Arial", 24), fg="yellow").pack(pady=10)
    tk.Button(root, text="Iniciar Juego", command=start_game, width=20, bg="yellow").pack(pady=5)
    tk.Button(root, text="Controles", command=show_controls, width=20, bg="cyan").pack(pady=5)
    tk.Button(root, text="Salir", command=root.destroy, width=20, bg="red").pack(pady=5)
    
    root.mainloop()

# Tamaño de los bloques (ahora es global)
BLOCK_SIZE = 40

# Función para verificar colisiones con las paredes (ahora es global)
def check_collision(x, y, maze_data, is_ghost=False):
    # Convertir posición a coordenadas del laberinto
    grid_x = x // BLOCK_SIZE
    grid_y = y // BLOCK_SIZE
    
    # Fantasmas pueden pasar por espacios vacíos y puntos
    if is_ghost:
        for dx, dy in [(0, 0), (15, 0), (-15, 0), (0, 15), (0, -15)]:
            check_x = (x + dx) // BLOCK_SIZE
            check_y = (y + dy) // BLOCK_SIZE
            
            if 0 <= check_x < len(maze_data[0]) and 0 <= check_y < len(maze_data):
                if maze_data[check_y][check_x] == 1:
                    return True
        return False
    else:
        # Pacman solo choca con paredes
        for dx, dy in [(0, 0), (15, 0), (-15, 0), (0, 15), (0, -15)]:
            check_x = (x + dx) // BLOCK_SIZE
            check_y = (y + dy) // BLOCK_SIZE
            
            if 0 <= check_x < len(maze_data[0]) and 0 <= check_y < len(maze_data):
                if maze_data[check_y][check_x] == 1:
                    return True
        return False

# Clase para los fantasmas
class Ghost:
    def __init__(self, x, y, color, speed):
        self.x = x * BLOCK_SIZE + BLOCK_SIZE // 2
        self.y = y * BLOCK_SIZE + BLOCK_SIZE // 2
        self.color = color
        self.speed = speed
        self.direction = random.randint(0, 3)
        self.target_x = 0
        self.target_y = 0
        self.frightened = False
        self.frightened_timer = 0
    
    def move(self, maze):
        # Cambio de dirección ocasional
        if random.random() < 0.02:
            self.direction = random.randint(0, 3)
        
        # Movimiento básico
        new_x, new_y = self.x, self.y
        
        if self.direction == 0:  # Derecha
            new_x += self.speed
        elif self.direction == 1:  # Arriba
            new_y -= self.speed
        elif self.direction == 2:  # Izquierda
            new_x -= self.speed
        elif self.direction == 3:  # Abajo
            new_y += self.speed
        
        # Verificar colisión con paredes
        if not check_collision(new_x, new_y, maze, is_ghost=True):
            self.x, self.y = new_x, new_y
        else:
            self.direction = random.randint(0, 3)
    
    def draw(self, screen):
        if self.frightened:
            color = (0, 0, 255)  # Azul cuando está asustado
        else:
            color = self.color
        
        # Cuerpo del fantasma
        pygame.draw.rect(screen, color, (self.x - 15, self.y - 15, 30, 30))
        pygame.draw.circle(screen, color, (int(self.x), int(self.y - 8)), 15)
        
        # Ojos
        eye_color = (255, 255, 255) if not self.frightened else (255, 255, 255)
        pygame.draw.circle(screen, eye_color, (int(self.x - 6), int(self.y - 5)), 5)
        pygame.draw.circle(screen, eye_color, (int(self.x + 6), int(self.y - 5)), 5)
        
        # Pupilas
        pupil_color = (0, 0, 0)
        pygame.draw.circle(screen, pupil_color, (int(self.x - 6), int(self.y - 5)), 2)
        pygame.draw.circle(screen, pupil_color, (int(self.x + 6), int(self.y - 5)), 2)
        
        # Patas
        for i in range(3):
            pygame.draw.rect(screen, color, (self.x - 15 + i*10, self.y + 10, 10, 5))

# Función principal del juego
def main_game():
    # Configuración de la pantalla
    WIDTH, HEIGHT = 600, 650
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pacman")
    
    # Colores
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    PINK = (255, 184, 255)
    CYAN = (0, 255, 255)
    ORANGE = (255, 184, 82)
    GREEN = (0, 255, 0)
    PURPLE = (128, 0, 128)
    
    # Laberinto (1 = pared, 0 = punto, 2 = espacio vacío, 3 = punto especial)
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 2, 0, 0, 0, 3, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 3, 0, 0, 0, 2, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 3, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    
    # Radio de Pacman
    PACMAN_RADIUS = 15
    
    # Posición inicial de Pacman
    pacman_x, pacman_y = 7 * BLOCK_SIZE + BLOCK_SIZE // 2, 13 * BLOCK_SIZE + BLOCK_SIZE // 2
    pacman_direction = 0  # 0: derecha, 1: arriba, 2: izquierda, 3: abajo
    pacman_speed = 5
    mouth_angle = 0
    mouth_open = True
    
    # Puntuación y vidas
    score = 0
    lives = 3
    total_dots = sum(row.count(0) for row in maze) + sum(row.count(3) for row in maze)
    font = pygame.font.SysFont(None, 36)
    
    # Crear fantasmas
    ghosts = [
        Ghost(7, 5, RED, 3),    # Rojo - Blinky
        Ghost(7, 7, PINK, 2),   # Rosa - Pinky
        Ghost(6, 7, CYAN, 2),   # Cian - Inky
        Ghost(8, 7, ORANGE, 2)  # Naranja - Clyde
    ]
    
    # Tiempo para puntos especiales
    power_time = 0
    
    # Reloj para controlar la velocidad del juego
    clock = pygame.time.Clock()
    
    # Función para dibujar el laberinto
    def draw_maze():
        for y in range(len(maze)):
            for x in range(len(maze[y])):
                rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                if maze[y][x] == 1:  # Pared
                    pygame.draw.rect(screen, BLUE, rect)
                    # Detalles en las paredes
                    pygame.draw.rect(screen, (0, 0, 150), rect, 2)
                elif maze[y][x] == 0:  # Punto
                    pygame.draw.circle(screen, WHITE, 
                                     (x * BLOCK_SIZE + BLOCK_SIZE // 2, 
                                      y * BLOCK_SIZE + BLOCK_SIZE // 2), 
                                      4)
                elif maze[y][x] == 3:  # Punto especial
                    pygame.draw.circle(screen, GREEN, 
                                     (x * BLOCK_SIZE + BLOCK_SIZE // 2, 
                                      y * BLOCK_SIZE + BLOCK_SIZE // 2), 
                                      8)
    
    # Función para comer puntos
    def eat_dots(x, y):
        nonlocal score, power_time
        grid_x = x // BLOCK_SIZE
        grid_y = y // BLOCK_SIZE
        
        if 0 <= grid_x < len(maze[0]) and 0 <= grid_y < len(maze):
            if maze[grid_y][grid_x] == 0:  # Punto normal
                maze[grid_y][grid_x] = 2
                score += 10
                return True
            elif maze[grid_y][grid_x] == 3:  # Punto especial
                maze[grid_y][grid_x] = 2
                score += 50
                power_time = 500  # 10 segundos de poder
                # Asustar a los fantasmas
                for ghost in ghosts:
                    ghost.frightened = True
                    ghost.frightened_timer = 500
                return True
        return False
    
    # Función para verificar colisión con fantasmas
    def check_ghost_collision():
        nonlocal lives, pacman_x, pacman_y, score
        for ghost in ghosts:
            distance = math.sqrt((ghost.x - pacman_x)**2 + (ghost.y - pacman_y)**2)
            if distance < PACMAN_RADIUS + 15:  # Radio de colisión
                if ghost.frightened:
                    # Comer fantasma
                    ghost.x = 7 * BLOCK_SIZE + BLOCK_SIZE // 2
                    ghost.y = 5 * BLOCK_SIZE + BLOCK_SIZE // 2
                    ghost.frightened = False
                    score += 200
                else:
                    # Perder vida
                    lives -= 1
                    if lives <= 0:
                        return True  # Game over
                    else:
                        # Resetear posición
                        pacman_x, pacman_y = 7 * BLOCK_SIZE + BLOCK_SIZE // 2, 13 * BLOCK_SIZE + BLOCK_SIZE // 2
                        # Dar breve invencibilidad
                        pygame.time.delay(1000)
        return False
    
    # Bucle principal del juego
    running = True
    game_over = False
    win = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        if not game_over:
            # Movimiento de Pacman
            keys = pygame.key.get_pressed()
            new_x, new_y = pacman_x, pacman_y
            
            if keys[pygame.K_RIGHT]:
                new_x += pacman_speed
                pacman_direction = 0
            elif keys[pygame.K_LEFT]:
                new_x -= pacman_speed
                pacman_direction = 2
            elif keys[pygame.K_UP]:
                new_y -= pacman_speed
                pacman_direction = 1
            elif keys[pygame.K_DOWN]:
                new_y += pacman_speed
                pacman_direction = 3
            
            # Verificar colisión antes de actualizar la posición
            if not check_collision(new_x, new_y, maze):
                pacman_x, pacman_y = new_x, new_y
            
            # Comer puntos
            eat_dots(pacman_x, pacman_y)
            
            # Mover fantasmas
            for ghost in ghosts:
                ghost.move(maze)
            
            # Verificar colisión con fantasmas
            if check_ghost_collision():
                game_over = True
                win = False
            
            # Actualizar tiempo de poder
            if power_time > 0:
                power_time -= 1
                if power_time == 0:
                    for ghost in ghosts:
                        ghost.frightened = False
            
            # Verificar si ganó
            if score >= total_dots * 10:
                game_over = True
                win = True
            
            # Animación de la boca de Pacman
            mouth_angle += 0.1
            if mouth_angle >= 2:
                mouth_angle = 0
                mouth_open = not mouth_open
        
        # Dibujar todo
        screen.fill(BLACK)
        draw_maze()
        
        # Dibujar fantasmas
        for ghost in ghosts:
            ghost.draw(screen)
        
        # Dibujar Pacman
        if mouth_open:
            start_angle = pacman_direction * (math.pi / 2) + math.pi / 4
            end_angle = pacman_direction * (math.pi / 2) - math.pi / 4
            pygame.draw.arc(screen, YELLOW, 
                          (pacman_x - PACMAN_RADIUS, pacman_y - PACMAN_RADIUS, 
                           PACMAN_RADIUS * 2, PACMAN_RADIUS * 2),
                          start_angle, end_angle, PACMAN_RADIUS)
            # Rellenar el arco para que parezca un Pacman
            pygame.draw.line(screen, YELLOW, (pacman_x, pacman_y),
                           (pacman_x + math.cos(start_angle) * PACMAN_RADIUS, 
                            pacman_y + math.sin(start_angle) * PACMAN_RADIUS), 2)
            pygame.draw.line(screen, YELLOW, (pacman_x, pacman_y),
                           (pacman_x + math.cos(end_angle) * PACMAN_RADIUS, 
                            pacman_y + math.sin(end_angle) * PACMAN_RADIUS), 2)
        else:
            pygame.draw.circle(screen, YELLOW, (int(pacman_x), int(pacman_y)), PACMAN_RADIUS)
        
        # Dibujar puntuación y vidas
        score_text = font.render(f"Puntuación: {score}", True, WHITE)
        screen.blit(score_text, (10, HEIGHT - 40))
        
        lives_text = font.render(f"Vidas: {lives}", True, WHITE)
        screen.blit(lives_text, (WIDTH - 120, HEIGHT - 40))
        
        # Dibujar iconos de vidas
        for i in range(lives):
            pygame.draw.circle(screen, YELLOW, (20 + i * 30, HEIGHT - 20), 10)
            # Boca de Pacman para iconos de vida
            start_angle = math.pi / 4
            end_angle = -math.pi / 4
            pygame.draw.arc(screen, BLACK, 
                          (10 + i * 30, HEIGHT - 30, 20, 20),
                          start_angle, end_angle, 2)
        
        # Mostrar mensaje de fin de juego
        if game_over:
            if win:
                message = "¡Ganaste!"
                color = GREEN
            else:
                message = "¡Juego Terminado!"
                color = RED
            
            game_over_text = font.render(message, True, color)
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, 
                                         HEIGHT // 2 - game_over_text.get_height() // 2))
            
            restart_text = font.render("Presiona R para reiniciar", True, WHITE)
            screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, 
                                      HEIGHT // 2 + 40))
            
            # Reiniciar juego
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                main_game()
                return
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()
    sys.exit()

# Iniciar el juego mostrando primero la pantalla de inicio
start_screen()