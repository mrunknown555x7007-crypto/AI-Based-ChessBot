import pygame
import chess
import random
import sys

# -- AI Logic (Minimax with Alpha-Beta Pruning...) --

PIECE_VALUES = {
    chess.PAWN: 100, chess.KNIGHT: 320, chess.BISHOP: 330,
    chess.ROOK: 500, chess.QUEEN: 900, chess.KING: 20000
}

PAWN_TABLE = [
    0,  0,  0,  0,  0,  0,  0,  0,
    5, 10, 10,-20,-20, 10, 10,  5,
    5, -5,-10,  0,  0,-10, -5,  5,
    0,  0,  0, 20, 20,  0,  0,  0,
    5,  5, 10, 25, 25, 10,  5,  5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0,  0,  0,  0,  0,  0,  0,  0
]

def evaluate_board(board):
    if board.is_checkmate():
        return -20000 if board.turn == chess.WHITE else 20000
    if board.is_stalemate() or board.is_insufficient_material():
        return 0

    score = 0
    for piece_type in PIECE_VALUES:
        score += len(board.pieces(piece_type, chess.WHITE)) * PIECE_VALUES[piece_type]
        score -= len(board.pieces(piece_type, chess.BLACK)) * PIECE_VALUES[piece_type]

    for square in board.pieces(chess.PAWN, chess.WHITE):
        score += PAWN_TABLE[square]
    for square in board.pieces(chess.PAWN, chess.BLACK):
        score -= PAWN_TABLE[chess.square_mirror(square)]
    return score

def minimax_with_alpha_beta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    legal_moves = list(board.legal_moves)
    legal_moves.sort(key=lambda move: board.is_capture(move), reverse=True)

    if maximizing_player:
        max_eval = -float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax_with_alpha_beta(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha: break
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax_with_alpha_beta(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha: break
        return min_eval

def get_best_move(board, depth):
    best_move = None
    is_white = board.turn == chess.WHITE
    best_eval = -float('inf') if is_white else float('inf')
        
    for move in board.legal_moves:
        board.push(move)
        eval = minimax_with_alpha_beta(board, depth - 1, -float('inf'), float('inf'), not is_white)
        board.pop()
        
        if is_white:
            if eval > best_eval:
                best_eval = eval
                best_move = move
            elif eval == best_eval and random.random() < 0.2: best_move = move
        else:
            if eval < best_eval:
                best_eval = eval
                best_move = move
            elif eval == best_eval and random.random() < 0.2: best_move = move
    return best_move


# --- PYGAMEs LIVE Chess Board LOGIC.. ---

WIDTH, HEIGHT = 600, 600
SQ_SIZE = WIDTH // 8
LIGHT_BLUE = (228, 240, 246)  
DARK_GRAY = (148, 162, 177)   
HIGHLIGHT = (255, 165, 0)     
DOT_COLOR = (50, 150, 50, 150) # GREEN for ALL  possible moves

UNICODE_PIECES = {
    'P': '♙', 'N': '♘', 'B': '♗', 'R': '♖', 'Q': '♕', 'K': '♔',
    'p': '♟', 'n': '♞', 'b': '♝', 'r': '♜', 'q': '♛', 'k': '♚'
}

def draw_board(screen):
    for row in range(8):
        for col in range(8):
            color = LIGHT_BLUE if (row + col) % 2 == 0 else DARK_GRAY
            pygame.draw.rect(screen, color, pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, board, font):
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            col = chess.square_file(square)
            row = 7 - chess.square_rank(square) 
            
            symbol = UNICODE_PIECES[piece.symbol()]
            color = (0, 0, 0) if piece.color == chess.BLACK else (255, 255, 255)
            
            text_surface = font.render(symbol, True, color)
            text_rect = text_surface.get_rect(center=(col * SQ_SIZE + SQ_SIZE // 2, row * SQ_SIZE + SQ_SIZE // 2))
            screen.blit(text_surface, text_rect)

def draw_legal_moves(screen, board, selected_square):
    """Draws small circles on squares where the selected piece can legally move."""
    if selected_square is not None:
        for move in board.legal_moves:
            if move.from_square == selected_square:
                col = chess.square_file(move.to_square)
                row = 7 - chess.square_rank(move.to_square)
                center_x = col * SQ_SIZE + SQ_SIZE // 2
                center_y = row * SQ_SIZE + SQ_SIZE // 2
                pygame.draw.circle(screen, DOT_COLOR, (center_x, center_y), SQ_SIZE // 6)

def draw_game_over_text(screen, board, font):
    """Overlays the result of the game when it ends."""
    if board.is_game_over():
        if board.is_checkmate():
            # If it's White's turn & they were at checkmate, WHITE LOST...
            if board.turn == chess.WHITE:
                text = "Checkmate! You Lost."
                color = (200, 0, 0) # Red
            else:
                text = "Checkmate! You Won!"
                color = (0, 150, 0) # Green
        elif board.is_stalemate():
            text = "Stalemate! It's a Draw."
            color = (100, 100, 100) # Gray
        else:
            text = "Game Over! Draw."
            color = (100, 100, 100)
            
        # Create a background box for the text to make it readable
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        
        # Draw a semi-transparent black box behind the text
        box_rect = text_rect.inflate(40, 20)
        s = pygame.Surface((box_rect.width, box_rect.height))
        s.set_alpha(200)
        s.fill((0, 0, 0))
        screen.blit(s, (box_rect.x, box_rect.y))
        
        screen.blit(text_surface, text_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Live PyChess vs AI")
    
    try:
        piece_font = pygame.font.SysFont("segoeuisymbol", int(SQ_SIZE * 0.8))
    except:
        piece_font = pygame.font.Font(pygame.font.get_default_font(), int(SQ_SIZE * 0.8))
        
    text_font = pygame.font.SysFont("Arial", 48, bold=True)
        
    board = chess.Board()
    selected_square = None
    running = True

    while running:
        game_over = board.is_game_over()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # CODER Turn (White) - only allow clicks if game is not over YET.
            elif event.type == pygame.MOUSEBUTTONDOWN and board.turn == chess.WHITE and not game_over:
                pos = pygame.mouse.get_pos()
                col = pos[0] // SQ_SIZE
                row = pos[1] // SQ_SIZE
                clicked_square = chess.square(col, 7 - row)

                if selected_square is None:
                    piece = board.piece_at(clicked_square)
                    if piece and piece.color == chess.WHITE:
                        selected_square = clicked_square
                else:
                    move = chess.Move(selected_square, clicked_square)
                    if board.piece_at(selected_square) and board.piece_at(selected_square).piece_type == chess.PAWN:
                        if chess.square_rank(clicked_square) == 7:
                            move = chess.Move(selected_square, clicked_square, promotion=chess.QUEEN)

                    if move in board.legal_moves:
                        board.push(move)
                        selected_square = None
                    else:
                        piece = board.piece_at(clicked_square)
                        if piece and piece.color == chess.WHITE:
                            selected_square = clicked_square
                        else:
                            selected_square = None

        # --- DRAWING ---
        draw_board(screen)
        
        if selected_square is not None:
            col = chess.square_file(selected_square)
            row = 7 - chess.square_rank(selected_square)
            pygame.draw.rect(screen, HIGHLIGHT, pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE), 5)
            # Draw the possible legal steps
            draw_legal_moves(screen, board, selected_square)

        draw_pieces(screen, board, piece_font)
        
        # Check and draw Game Over UI
        if game_over:
            draw_game_over_text(screen, board, text_font)

        pygame.display.flip()

        # --- {AI TURN} ---
        if board.turn == chess.BLACK and not game_over:
            # Short delay so the user can see their move land before the AI starts thinking
            pygame.time.wait(100) 
            
            best_move = get_best_move(board, depth=3)
            if best_move:
                board.push(best_move)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
 # .....AI BASED CHESS GAME END.....