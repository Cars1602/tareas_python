import tkinter as tk
from tkinter import messagebox
import copy

class ChessGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ajedrez")
        self.root.geometry("900x1200")
        self.root.resizable(False, False)
        
        # Colores del tablero
        self.light_color = "#F0D9B5"
        self.dark_color = "#B58863"
        self.highlight_color = "#FFD700"
        self.check_color = "#FF6B6B"
        
        # Estado del juego
        self.board = self.create_initial_board()
        self.current_player = "white"
        self.selected_piece = None
        self.selected_pos = None
        self.possible_moves = []
        self.game_over = False
        
        # Símbolos de las piezas
        self.piece_symbols = {
            'white': {'king': '♔', 'queen': '♕', 'rook': '♖', 'bishop': '♗', 'knight': '♘', 'pawn': '♙'},
            'black': {'king': '♚', 'queen': '♛', 'rook': '♜', 'bishop': '♝', 'knight': '♞', 'pawn': '♟'}
        }
        
        self.create_widgets()
        self.draw_board()
        
    def create_initial_board(self):
        # Crear el tablero inicial
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Piezas blancas
        board[7] = [
            {'type': 'rook', 'color': 'white'}, {'type': 'knight', 'color': 'white'},
            {'type': 'bishop', 'color': 'white'}, {'type': 'queen', 'color': 'white'},
            {'type': 'king', 'color': 'white'}, {'type': 'bishop', 'color': 'white'},
            {'type': 'knight', 'color': 'white'}, {'type': 'rook', 'color': 'white'}
        ]
        board[6] = [{'type': 'pawn', 'color': 'white'} for _ in range(8)]
        
        # Piezas negras
        board[0] = [
            {'type': 'rook', 'color': 'black'}, {'type': 'knight', 'color': 'black'},
            {'type': 'bishop', 'color': 'black'}, {'type': 'queen', 'color': 'black'},
            {'type': 'king', 'color': 'black'}, {'type': 'bishop', 'color': 'black'},
            {'type': 'knight', 'color': 'black'}, {'type': 'rook', 'color': 'black'}
        ]
        board[1] = [{'type': 'pawn', 'color': 'black'} for _ in range(8)]
        
        return board
    
    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg="white")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Información del juego
        self.info_label = tk.Label(main_frame, text="Turno: Blancas", font=("Arial", 14), bg="white")
        self.info_label.pack(pady=10)
        
        # Canvas para el tablero
        self.canvas = tk.Canvas(main_frame, width=640, height=640, bg="white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_square_click)
        
        # Botón para reiniciar
        reset_btn = tk.Button(main_frame, text="Nuevo Juego", command=self.reset_game, 
                             font=("Arial", 12), bg="#4CAF50", fg="white")
        reset_btn.pack(pady=10)
    
    def draw_board(self):
        self.canvas.delete("all")
        
        square_size = 80
        
        # Dibujar las casillas
        for row in range(8):
            for col in range(8):
                x1 = col * square_size
                y1 = row * square_size
                x2 = x1 + square_size
                y2 = y1 + square_size
                
                # Color de la casilla
                if (row + col) % 2 == 0:
                    color = self.light_color
                else:
                    color = self.dark_color
                
                # Resaltar casilla seleccionada
                if self.selected_pos and self.selected_pos == (row, col):
                    color = self.highlight_color
                
                # Resaltar posibles movimientos
                if (row, col) in self.possible_moves:
                    color = "#90EE90"
                
                # Resaltar rey en jaque
                piece = self.board[row][col]
                if piece and piece['type'] == 'king' and self.is_in_check(piece['color']):
                    color = self.check_color
                
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
                
                # Dibujar pieza
                if piece:
                    symbol = self.piece_symbols[piece['color']][piece['type']]
                    self.canvas.create_text(x1 + square_size//2, y1 + square_size//2,
                                          text=symbol, font=("Arial", 40), fill="black")
    
    def on_square_click(self, event):
        if self.game_over:
            return
        
        col = event.x // 80
        row = event.y // 80
        
        if 0 <= row < 8 and 0 <= col < 8:
            if self.selected_piece is None:
                # Seleccionar pieza
                piece = self.board[row][col]
                if piece and piece['color'] == self.current_player:
                    self.selected_piece = piece
                    self.selected_pos = (row, col)
                    self.possible_moves = self.get_possible_moves(row, col)
                    self.draw_board()
            else:
                # Mover pieza
                if (row, col) in self.possible_moves:
                    self.make_move(self.selected_pos, (row, col))
                    self.selected_piece = None
                    self.selected_pos = None
                    self.possible_moves = []
                    self.switch_player()
                    self.draw_board()
                    self.check_game_status()
                else:
                    # Deseleccionar o seleccionar nueva pieza
                    piece = self.board[row][col]
                    if piece and piece['color'] == self.current_player:
                        self.selected_piece = piece
                        self.selected_pos = (row, col)
                        self.possible_moves = self.get_possible_moves(row, col)
                        self.draw_board()
                    else:
                        self.selected_piece = None
                        self.selected_pos = None
                        self.possible_moves = []
                        self.draw_board()
    
    def get_possible_moves(self, row, col):
        piece = self.board[row][col]
        if not piece:
            return []
        
        moves = []
        piece_type = piece['type']
        
        if piece_type == 'pawn':
            moves = self.get_pawn_moves(row, col, piece['color'])
        elif piece_type == 'rook':
            moves = self.get_rook_moves(row, col, piece['color'])
        elif piece_type == 'knight':
            moves = self.get_knight_moves(row, col, piece['color'])
        elif piece_type == 'bishop':
            moves = self.get_bishop_moves(row, col, piece['color'])
        elif piece_type == 'queen':
            moves = self.get_queen_moves(row, col, piece['color'])
        elif piece_type == 'king':
            moves = self.get_king_moves(row, col, piece['color'])
        
        # Filtrar movimientos que pondrían al rey en jaque
        valid_moves = []
        for move in moves:
            if self.is_move_safe(row, col, move[0], move[1]):
                valid_moves.append(move)
        
        return valid_moves
    
    def get_pawn_moves(self, row, col, color):
        moves = []
        direction = -1 if color == 'white' else 1
        start_row = 6 if color == 'white' else 1
        
        # Movimiento hacia adelante
        new_row = row + direction
        if 0 <= new_row < 8 and self.board[new_row][col] is None:
            moves.append((new_row, col))
            
            # Movimiento doble desde posición inicial
            if row == start_row:
                new_row = row + 2 * direction
                if 0 <= new_row < 8 and self.board[new_row][col] is None:
                    moves.append((new_row, col))
        
        # Captura diagonal
        for dc in [-1, 1]:
            new_row, new_col = row + direction, col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target = self.board[new_row][new_col]
                if target and target['color'] != color:
                    moves.append((new_row, new_col))
        
        return moves
    
    def get_rook_moves(self, row, col, color):
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            for i in range(1, 8):
                new_row, new_col = row + i * dr, col + i * dc
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    target = self.board[new_row][new_col]
                    if target is None:
                        moves.append((new_row, new_col))
                    elif target['color'] != color:
                        moves.append((new_row, new_col))
                        break
                    else:
                        break
                else:
                    break
        
        return moves
    
    def get_knight_moves(self, row, col, color):
        moves = []
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), 
                       (1, -2), (1, 2), (2, -1), (2, 1)]
        
        for dr, dc in knight_moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target = self.board[new_row][new_col]
                if target is None or target['color'] != color:
                    moves.append((new_row, new_col))
        
        return moves
    
    def get_bishop_moves(self, row, col, color):
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for dr, dc in directions:
            for i in range(1, 8):
                new_row, new_col = row + i * dr, col + i * dc
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    target = self.board[new_row][new_col]
                    if target is None:
                        moves.append((new_row, new_col))
                    elif target['color'] != color:
                        moves.append((new_row, new_col))
                        break
                    else:
                        break
                else:
                    break
        
        return moves
    
    def get_queen_moves(self, row, col, color):
        return self.get_rook_moves(row, col, color) + self.get_bishop_moves(row, col, color)
    
    def get_king_moves(self, row, col, color):
        moves = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), 
                     (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target = self.board[new_row][new_col]
                if target is None or target['color'] != color:
                    moves.append((new_row, new_col))
        
        return moves
    
    def make_move(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        
        # Mover la pieza
        self.board[to_row][to_col] = self.board[from_row][from_col]
        self.board[from_row][from_col] = None
    
    def is_move_safe(self, from_row, from_col, to_row, to_col):
        # Simular el movimiento
        board_copy = copy.deepcopy(self.board)
        piece = board_copy[from_row][from_col]
        board_copy[to_row][to_col] = piece
        board_copy[from_row][from_col] = None
        
        # Verificar si el rey está en jaque después del movimiento
        return not self.is_in_check_on_board(piece['color'], board_copy)
    
    def is_in_check(self, color):
        return self.is_in_check_on_board(color, self.board)
    
    def is_in_check_on_board(self, color, board):
        # Encontrar el rey
        king_pos = None
        for row in range(8):
            for col in range(8):
                piece = board[row][col]
                if piece and piece['type'] == 'king' and piece['color'] == color:
                    king_pos = (row, col)
                    break
            if king_pos:
                break
        
        if not king_pos:
            return False
        
        # Verificar si alguna pieza enemiga puede atacar al rey
        enemy_color = 'black' if color == 'white' else 'white'
        for row in range(8):
            for col in range(8):
                piece = board[row][col]
                if piece and piece['color'] == enemy_color:
                    if self.can_attack_position(row, col, king_pos[0], king_pos[1], board):
                        return True
        
        return False
    
    def can_attack_position(self, from_row, from_col, to_row, to_col, board):
        piece = board[from_row][from_col]
        if not piece:
            return False
        
        piece_type = piece['type']
        color = piece['color']
        
        if piece_type == 'pawn':
            direction = -1 if color == 'white' else 1
            if from_row + direction == to_row and abs(from_col - to_col) == 1:
                return True
        elif piece_type == 'rook':
            if from_row == to_row or from_col == to_col:
                return self.is_path_clear(from_row, from_col, to_row, to_col, board)
        elif piece_type == 'knight':
            dr, dc = abs(from_row - to_row), abs(from_col - to_col)
            if (dr == 2 and dc == 1) or (dr == 1 and dc == 2):
                return True
        elif piece_type == 'bishop':
            if abs(from_row - to_row) == abs(from_col - to_col):
                return self.is_path_clear(from_row, from_col, to_row, to_col, board)
        elif piece_type == 'queen':
            if (from_row == to_row or from_col == to_col or 
                abs(from_row - to_row) == abs(from_col - to_col)):
                return self.is_path_clear(from_row, from_col, to_row, to_col, board)
        elif piece_type == 'king':
            if abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1:
                return True
        
        return False
    
    def is_path_clear(self, from_row, from_col, to_row, to_col, board):
        dr = 0 if from_row == to_row else (1 if to_row > from_row else -1)
        dc = 0 if from_col == to_col else (1 if to_col > from_col else -1)
        
        current_row, current_col = from_row + dr, from_col + dc
        
        while (current_row, current_col) != (to_row, to_col):
            if board[current_row][current_col] is not None:
                return False
            current_row += dr
            current_col += dc
        
        return True
    
    def switch_player(self):
        self.current_player = 'black' if self.current_player == 'white' else 'white'
        player_name = 'Negras' if self.current_player == 'black' else 'Blancas'
        self.info_label.config(text=f"Turno: {player_name}")
    
    def check_game_status(self):
        if self.is_checkmate(self.current_player):
            winner = 'Negras' if self.current_player == 'white' else 'Blancas'
            messagebox.showinfo("Jaque Mate", f"¡{winner} ganan!")
            self.game_over = True
        elif self.is_stalemate(self.current_player):
            messagebox.showinfo("Empate", "¡Empate por ahogado!")
            self.game_over = True
        elif self.is_in_check(self.current_player):
            player_name = 'Negras' if self.current_player == 'black' else 'Blancas'
            self.info_label.config(text=f"Turno: {player_name} - ¡JAQUE!")
    
    def is_checkmate(self, color):
        if not self.is_in_check(color):
            return False
        
        return self.has_no_legal_moves(color)
    
    def is_stalemate(self, color):
        if self.is_in_check(color):
            return False
        
        return self.has_no_legal_moves(color)
    
    def has_no_legal_moves(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece['color'] == color:
                    moves = self.get_possible_moves(row, col)
                    if moves:
                        return False
        return True
    
    def reset_game(self):
        self.board = self.create_initial_board()
        self.current_player = "white"
        self.selected_piece = None
        self.selected_pos = None
        self.possible_moves = []
        self.game_over = False
        self.info_label.config(text="Turno: Blancas")
        self.draw_board()
    
    def run(self):
        self.root.mainloop()

# Ejecutar el juego
if __name__ == "__main__":
    game = ChessGame()
    game.run()