import random
# Pawn (Peón) - P
# Rook (Torre) - R
# Knight (Caballo) - N
# Bishop (Alfil) - B
# Queen (Reina) - Q
# King (Rey) - K
symbols_white = ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♖', '♖', '♘', '♘', '♗', '♗', '♕', '♔']
symbols_black = ['♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♜', '♜', '♞', '♞', '♝', '♝', '♛', '♚']

crow_symbols_white = ['♖', '♘', '♗', '♕']
crow_symbols_black = ['♜', '♞', '♝', '♛']
position_bishop_white = []
position_bishop_black = []

def generate_piece(color):
  if color == 'B':
    copy = symbols_black.copy()
  else:
    copy = symbols_white.copy()
    
  list = []
  for _ in range(5):
    pop = copy.pop(random.randint(0, len(copy) - 1))
    if color == 'B':
      list.append(pop.lower())
    else:
      list.append(pop.upper())

  return list 
      
      
      
def is_not_valid_position_bishop(row, col, piece):
  if piece == '♗':        
      if len(position_bishop_white) == 0:
              position_bishop_white.append(get_color(row, col))        
      else:            
          return position_bishop_white.count(get_color(row, col)) == 0    
      
  if piece == '♝':       
    if len(position_bishop_black) == 0:
          position_bishop_black.append(get_color(row, col))
    else:            
      return position_bishop_black.count(get_color(row, col)) == 0    
  return True

def is_valid_position(board, row, col, piece):    
    print(f'Piece: {piece} ({row},{col})')   
     # Verificar si la posición está vacía    
    if board[row][col] not in ('B', 'W'):       
        return False    
    if (piece == '♟︎' and row == 0) or (piece == '♙' and row == 7):        
      return False;    
    if piece in ('♗', '♝'):        
        return is_not_valid_position_bishop(row, col, piece)   
     # Verificar que no haya más de 2 alfiles del mismo color en casillas del mismo color   
     # Verificar si la casilla es de color blanco (fila par y columna par) o de color negro (fila impar y columna impar)  
      # Verificar que los peones no estén en la fila 1 para el blanco o fila 6 para el negro  
      # Verificar que el rey no pueda estar en jaque   
     # ...    
    return True

def place_piece(board, piece):  
    for _ in range(5):    
          p = piece.pop()     
          while True:          
              row = random.randint(0, 7)        
              col = random.randint(0, 7)            
              if is_valid_position(board, row, col, p):     
                  if (p == '♟︎' and row == 7) or (p == '♙' and row == 0):    
                      if p == '♟︎':                
                        p = crow_symbols_black[random.randint(0, len(crow_symbols_black) - 1)]          
                      else:                      
                        p = crow_symbols_white[random.randint(0, len(crow_symbols_white) - 1)]   
                  board[row][col] = p             
                  break
              
              
def get_color(row, column):    
   if (row % 2 == 0 and column % 2 != 0) or (row % 2 != 0 and column % 2 == 0):   
         return 'B'  
   return 'W'

def generate_board():   
  board = []    
  for f in range(8):     
       row = []       
       for c in range(8):    
          row.append(get_color(f, c)) 
       board.append(row)     
  return board

def print_board(board):   
    for row in board:  
      for col in row:    
        print(col, end='\t')     
      print('')
      
      
      
def get_possibles_moves(board):
  for row in range(8):
    for col in range(8):
      if board[row][col] not in ('B', 'W'):
        piece = board[row][col]
        if piece == '♟︎' or piece == '♙':
          print(get_pawn_moves(board, row, col))
        elif piece == '♖' or piece == '♜':
          print(get_rook_moves(board, row, col))
        elif piece == '♗' or piece == '♝':
          print(get_bishop_moves(board, row, col))
        elif piece == '♘' or piece == '♞':
          print(get_knight_moves(board, row, col))
        elif piece == '♕' or piece == '♛':
          print(get_queen_moves(board, row, col))
        
def get_pawn_moves(board, row, col):
  if board[row][col] == '♟︎':
    if row == 1:
      if (is_valid_position2(board, row + 1, col)):
        return [(row + 1, col), (row + 2, col)]
    else:
      return [(row + 1, col)]
  elif board[row][col] == '♙':
    if row == 6:
      return [(row - 1, col), (row - 2, col)]
    else:
      return [(row - 1, col)]
    
def get_rook_moves(board, row, col):
  moves = []
  for i in range(1, 8):
    if row + i < 8:
      moves.append((row + i, col))
    if row - i >= 0:
      moves.append((row - i, col))
    if col + i < 8:
      moves.append((row, col + i))
    if col - i >= 0:
      moves.append((row, col - i))
  return moves

def get_bishop_moves(board, row, col):
  moves = []
  for i in range(1, 8):
    if row + i < 8 and col + i < 8:
      moves.append((row + i, col + i))
    if row - i >= 0 and col - i >= 0:
      moves.append((row - i, col - i))
    if row + i < 8 and col - i >= 0:
      moves.append((row + i, col - i))
    if row - i >= 0 and col + i < 8:
      moves.append((row - i, col + i))
  return moves

def get_knight_moves(board, row, col):
  moves = []
  if row + 2 < 8 and col + 1 < 8:
    moves.append((row + 2, col + 1))
  if row + 2 < 8 and col - 1 >= 0:
    moves.append((row + 2, col - 1))
  if row - 2 >= 0 and col + 1 < 8:
    moves.append((row - 2, col + 1))
  if row - 2 >= 0 and col - 1 >= 0:
    moves.append((row - 2, col - 1))
  if row + 1 < 8 and col + 2 < 8:
    moves.append((row + 1, col + 2))
  if row + 1 < 8 and col - 2 >= 0:
    moves.append((row + 1, col - 2))
  if row - 1 >= 0 and col + 2 < 8:
    moves.append((row - 1, col + 2))
  if row - 1 >= 0 and col - 2 >= 0:
    moves.append((row - 1, col - 2))
  return moves

def get_queen_moves(board, row, col):
  moves = []
  moves += get_rook_moves(board, row, col)
  moves += get_bishop_moves(board, row, col)
  return moves

def get_king_moves(board, row, col):
  moves = []
  if row + 1 < 8:
    moves.append((row + 1, col))
  if row - 1 >= 0:
    moves.append((row - 1, col))
  if col + 1 < 8:
    moves.append((row, col + 1))
  if col - 1 >= 0:
    moves.append((row, col - 1))
  if row + 1 < 8 and col + 1 < 8:
    moves.append((row + 1, col + 1))
  if row - 1 >= 0 and col - 1 >= 0:
    moves.append((row - 1, col - 1))
  if row + 1 < 8 and col - 1 >= 0:
    moves.append((row + 1, col - 1))
  if row - 1 >= 0 and col + 1 < 8:
    moves.append((row - 1, col + 1))
  return moves


def is_valid_position2(board, row, col):
    if board[row][col] not in ('B', 'W'):
      return False
    return True


board = generate_board()
white_piece = generate_piece('B')
black_piece = generate_piece('W')
place_piece(board, white_piece)
place_piece(board, black_piece)
print_board(board)
get_possibles_moves(board)

