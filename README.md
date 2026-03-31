 # ♟️ PyChess AI: Interactive Minimax Chess

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

[![Dependencies](https://img.shields.io/badge/dependencies-pygame%20%7C%20python--chess-green.svg)]()

A fully playable, interactive desktop chess application built in Python. This project features a custom-built AI opponent powered by the **Minimax algorithm with Alpha-Beta pruning** and a clean, responsive graphical interface built with Pygame.

---

##  Table of Contents
- [Features](#-features)
- [Demo / Screenshots](#-demo--screenshots)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [How to Play](#-how-to-play)
- [How the AI Works](#-how-the-ai-works)
- [Customization](#-customization)
- [License](#-license)

# Chess Game {MINIMAX Alogorithm}
## Technologies used:
Python with pygame module




## Project Description:
This is a Chess game built using python with pygame module for GUI. It has 2 playing mode either you can play against another human player or against AI. The AI was implemented using Minimax algorithm with alpha beta pruning and with the depth search of 3.

Inorder to model a chessboard within a data structure a 2D array was used with the dimensions of 8x8. The chessboard array could store 64 gametiles objects and each gametile object stored a tile number and a chess piece object.

## Abstract
​This project involves the design, development, and evaluation of an Artificial Intelligence (AI) chess engine. Because chess possesses a massive state space (the Shannon number, 10^{120}), brute-force computation is mathematically intractable. This system navigates this complexity using a depth-limited Minimax search algorithm augmented by Alpha-Beta pruning. Combined with a custom heuristic evaluation function utilizing piece-square tables, the engine achieves rapid, strategic decision-making while maintaining high computational efficiency on consumer hardware.
## Objectives
​-  Algorithmic Implementation: To build a functional Minimax decision-making engine that recursively explores future game states.
-  Computational Optimization: To integrate Alpha-Beta pruning to drastically reduce time complexity and enable deeper search depths.
-​  Heuristic Evaluation: To design a static board evaluator using material weights and positional matrices (Piece-Square Tables).
-  ​Interactive Experience: To wrap the AI in a responsive graphical user interface (GUI) for real-time human-vs-computer gameplay.
    ​Literature Review
   
## Features

​1.  **Interactive Live Board**:
A clean 2D graphical interface built with Pygame.

2. **​Smart AI Opponent**:
Play as White against a Black AI that evaluates material advantage and positional strategy using piece-square tables.
3. **​Legal Move Highlighting**:
Click on any of your pieces to see green indicator dots showing all valid squares you can move to.

4.**​Automatic Rule Enforcement**:
Powered by the python-chess library, ensuring 100% accurate chess rules (including en passant, castling, and pawn promotion).

​
5.**Game Over Detection**:
Automatically detects checkmates and stalemates, freezing the board and displaying a beautiful UI overlay declaring the winner.

## Files Description:

1.**Board Directory**: 
      - Board.py: In this file we create a class of chessBoard and initialize and declare a 2D array of gametiles with null pieces and then place all the chess pieces on the board on their respective starting positions. 
      - move.py: In this file we define some of the special cases in chess for example castling, enpassant rule, check. functions are used to check whether the the player is in check, return moves available in case the player is in check, return moves in case of castling and return moves available in case of enpassant rule.
      - Tile.py: It creates a Tile class which is placed on chessboard array. It can store a position number on the board and a chess piece object. 


2.**chess Art directory**: Contains all the images of the chess pieces.


3.**pieces directory**: Contains files in which every chess piece class is defined. Every chess piece class has alliance (indicating whether the piece is white or black) and position ( coordinates on the chessboard ) attributes. It also has legalmove method which is used to calculate the legal moves for that chess piece on the chessboard. 


4.**Player directory**:
      - AI.py: Contains the logic for AI algorithm. The AI was implemented using recursive Minimax algorithm with alpha beta pruning and with the depth search of 3. The evaluation function assigned each chess piece a value, White pieces were assigned a positive value based on their rank and black pieces were assigned negative value based on their rank as well. So the total value becomes 0 in the start of the game where each side has all the pieces. The algorithm tried to search all possible moves up to the depth of 3 and calculate which next move could allow it to have best evaluation value.


5.**Playchess.py**: Main file of the program which merges all the functionality from the other files and itself as well to implement all this on pygame GUI.
      
# Screen:
Game Screen

    1. Main Screen:
  <img width="793" height="536" alt="Screenshot 2026-03-28 211719" src="https://github.com/user-attachments/assets/41b15688-02fa-409a-b980-7e3b3c6c3c66" />
  
    2. Starting position:
  
<img width="935" height="947" alt="Screenshot 2026-03-28 184936" src="https://github.com/user-attachments/assets/cc4628fa-b808-4006-aab0-00e1ab88c2be" />

 3. The GUI guiding player which moves he can play after he clicked on his left white queen :

    <img width="946" height="965" alt="Screenshot 2026-03-28 184829" src="https://github.com/user-attachments/assets/ca7d153e-c90b-419c-93b7-03d1237ffc8f" />

 4. Game End screen:
 
<img width="1908" height="1003" alt="Screenshot 2026-03-28 184726" src="https://github.com/user-attachments/assets/05fbd45a-07da-4a67-b269-bee33354e47c" />

> **WARNING!!!**
>
> The board is rotating each turn by default! The active player always placed at the bottom!

## Built With

- [Telegraf.js](https://github.com/telegraf/telegraf) - Telegram bot framework for Node.js.
- [Node-Chess](https://github.com/brozeph/node-chess) - A simple node.js library for parsing and validating chess board position with an algebraic move parser.
- [Knex](https://github.com/tgriesser/knex) - A query builder for PostgreSQL, MySQL and SQLite3, designed to be flexible, portable, and fun to use.


## Improvements
The AI for the game could certainly be improved. An average chess player can easily beat the AI because the AI sometimes make a blunder move , the reason could be because of the evaluation function and the shallow depth of the possibilities explored by the algorithm. The evaluation function could be improved to also take into consideration the position of the chess pieces on the board along with value of the chess pieces. We can train a deep learning model and deploy it into the game if we have enough data.

## How to INSTALL and RUN

1.    


`git clone https://github.com/mrunknown555x7007-crypto/AI-Based-ChessBot.git`

`cd chess-game-AI-project`

`pip install pygame chess`

2.    In order to run the game. write the command on terminal or cmd.


`python3 playchess.py`

3.  TO RUN THE GAME BY EXICUTING PYTHON SCRIPT

    ` AI Chessbot.py`
  ##  Customization
​If you want to make the AI harder or faster, look for this line in the main() function:
  
      `best_move = get_best_move(board, depth=3)`
​
1.   Change depth=2 for a very fast, but slightly less strategic AI.

2. ​Change depth=4 for a much harder AI (Note: This will significantly increase the time it takes for the AI to make a move!).

##  Advantages & Limitations
###  ​Advantages
-  ​Highly Efficient: Memory footprint is exceptionally low compared to Neural Network approaches.
-  ​Deterministic & Explainable: Every move is mathematically traceable to specific heuristic values.
###  ​Limitations
​-  The Horizon Effect: The AI cannot "see" past its depth limit (e.g., 4 moves). It may make a move that looks good at Depth 4 but loses a piece at Depth 5.
​Lack of Deep Positional -Understanding: It relies entirely on hardcoded matrices rather than learned strategic concepts.
​Future Scope

## Future Scope
​To elevate the engine from an intermediate bot to a master-level opponent, future updates will include:
-​  Transposition Tables (Zobrist Hashing): Caching previously seen board states to avoid redundant calculation.
​-  Iterative Deepening: Searching depth 1, then 2, then 3 to improve move-ordering for the Alpha-Beta algorithm.
-​  Quiescence Search: Extending the search dynamically during volatile tactical sequences (like capture chains) to combat the horizon effect.
## ​ Conclusion
​This project successfully demonstrates the implementation of a functional and strategic chess AI. The integration of Alpha-Beta pruning proved vital, transforming an otherwise intractable mathematical problem into a highly optimized, interactive desktop application. The modular architecture developed here serves as a robust foundation for future integrations of advanced AI techniques.
##  ​References
1. ​Knuth, D. E., & Moore, R. W. (1975). An analysis of alpha-beta pruning. Artificial Intelligence, 6(4), 293-326.
2. ​Shannon, C. E. (1950). XXII. Programming a computer for playing chess. Philosophical Magazine, 41(314), 256-275.
3. ​Russell, S., & Norvig, P. (2020). Artificial Intelligence: A Modern Approach. Pearson.
    # AUTHOR : SAMRIDH MISHRA
