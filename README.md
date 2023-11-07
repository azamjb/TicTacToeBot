# TicTacToeBot

Intelligent tic tac toe bot, incorporates the Minimax algorithm to create a challenging AI opponent capable of strategic gameplay.

Employs depth-limiting technique to provide players with a range of difficulty levels, hardest level is devoid of any depth restrictions, ensuring the AI will never lose a game.

Minimax is a backtracking algorithm used in decision making and game theory to find the optimal move for a player. It is widely used in two player turn-based games such as Tic-Tac-Toe, Backgammon, Mancala, Chess, etc.

In Minimax, the two players are called maximizer and minimizer. The maximizer tries to get the highest score possible while the minimizer tries to do the opposite and get the lowest score possible.

Every board state has a value associated with it. In a given state if the maximizer has upper hand then, the score of the board will tend to be some positive value. If the minimizer has the upper hand in that board state then it will tend to be some negative value. The values of the board are calculated by some heuristics which are unique for every type of game.

<img width="553" alt="Screenshot 2023-08-08 at 2 01 54 PM" src="https://github.com/azamjb/TicTacToeBot/assets/85136312/22e47a92-4132-4f70-933f-0d41036e1418">
