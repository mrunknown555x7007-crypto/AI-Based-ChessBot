# ♟️ PyChess AI: Interactive Minimax Chess

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

[![Dependencies](https://img.shields.io/badge/dependencies-pygame%20%7C%20python--chess-green.svg)]()

A fully playable, interactive desktop chess application built in Python. This project features a custom-built AI opponent powered by the **Minimax algorithm with Alpha-Beta pruning** and a clean, responsive graphical interface built with Pygame.

---

## 📖 Table of Contents
- [Features](#-features)
- [Demo / Screenshots](#-demo--screenshots)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [How to Play](#-how-to-play)
- [How the AI Works](#-how-the-ai-works)
- [Customization](#-customization)
- [License](#-license)

---

## ✨ Features

* **Interactive GUI:** A clean 2D graphical interface built with Pygame, featuring standard chess piece Unicode rendering.
* **Smart AI Opponent:** Play as White against a Black AI that evaluates material advantage and positional strategy using piece-square tables.
* **Legal Move Indicators:** Click on any of your pieces to see green highlighted dots showing all valid destination squares.
* **Strict Rule Enforcement:** Powered by the robust `python-chess` library, ensuring 100% accurate chess rules (en passant, castling, and pawn promotion are fully supported).
* **Game State Detection:** Automatically detects checkmates, stalemates, and draws, freezing the board and displaying a clean UI overlay declaring the match result.

---

## 📸 Demo / Screenshots

*(Note: Add your screenshots to an `assets` folder and link them here)*

| Start Position | Legal Moves | Checkmate Overlay |
| :---: | :---: | :---: |
| ![Start](https://via.placeholder.com/250x250.png?text=Start+Position) | ![Moves](https://via.placeholder.com/250x250.png?text=Legal+Move+Dots) | ![Checkmate](https://via.placeholder.com/250x250.png?text=Checkmate+Screen) |

---

## 🛠️ Prerequisites

To run this project, you will need **Python 3.8+** installed on your system.

The project relies on two primary external libraries:
* `pygame` - For rendering the game window and graphics.
* `python-chess` - For move generation, validation, and board state management.

---

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/pychess-ai.git](https://github.com/yourusername/pychess-ai.git)
   cd pychess-ai
