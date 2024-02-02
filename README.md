# Chess Application README

This Chess Application is a web-based chess game developed using Django, the python-chess library and chessboard.js library. 
The application allows users to play chess against an AI opponent using different algorithms for move prediction.

## How it works
    1. Browser Game State:
        The browser maintains the current game state in the Forsyth-Edwards Notation (FEN) string, representing the board position, 
        active player, castling availability, en passant target square, halfmove clock, and fullmove number.
        Additionally, the browser keeps a list of the current possible legal moves available for the active player.

    2. Move Validation:
        Before the player's move is executed, the board object on the frontend checks whether the move is valid based on the current game state and the list of legal moves.

    3. AJAX Request:
        If the move is valid, the browser initiates an AJAX (Asynchronous JavaScript and XML) request to the backend.
        The request contains a JSON object with the previous FEN notation string and the move that the player is attempting to make.

    4. Backend Processing:
        The backend receives the AJAX request and extracts the FEN notation and the player's move from the JSON object.
        A new chess game object is created using the received FEN notation.
        The player's move is then executed on the chessboard, updating the game state.

    5. Backend Response:
        The backend generates an updated FEN notation string, a list of legal moves and some other info based on the new game state.
        This information is sent back to the frontend as a JSON response.

    6. Frontend Update:
        The board object on the frontend receives the new FEN notation and the list of legal moves from the backend's response.
        The game state is then updated on the browser side to reflect the changes.
        The updated FEN notation allows the frontend to visually represent the new board position, and the list of legal moves ensures that the player can only make valid moves.

Note: The backend can give different responses based on which predictor is selected.
Minimax calculates the best move based on a recursive depth first search algorithm and a static evaluation function.
ChessAI calculates the best move based on the outputs of a convolutional neural network trained on 13 million moves from [kaggle chess-games](https://www.kaggle.com/datasets/arevel/chess-games) dataset. (currently working on this)

## [Dataset pre-processing](https://github.com/enansaif/chess_project/blob/master/chess_ai_rnd/dataset-eda.ipynb)

- Kept only games terminated normally, removing cases of abandonment, rules infraction, time forfeit, and unterminated games.
- Excluded games involving players with lower ratings (both WhiteElo and BlackElo < 2000).
- Excluded games with inconclusive results (1/2-1/2) to focus on wins and losses.

## [Model development](https://github.com/enansaif/chess_project/blob/master/chess_ai_rnd/model-development.ipynb)

### Move Representation:

- Chess board states represented using Forsyth-Edwards Notation (FEN).
- Mapping function (`get_mapping`) converts FEN notation to numerical matrix representation.
- Board state converted into a tensor using the mapping function.
- Moves represented using a one-hot encoding scheme.
- Function (`move_repr`) converts a move (e.g., 'g1f3') into a tensor representation.

### Move Generation Function:

- Function (`move_gen`) generates a move based on the neural network's prediction.
- Takes neural network's prediction and current FEN notation, identifies the best move from the legal moves list, and returns it.

### Neural Network Architecture:

- Implemented using PyTorch.
- Model follows classic ResNet architecture with residual blocks.
- Model consists of convolutional layers (`Block` and `ChessNet`) for processing the board state and making move predictions.
- `Block` class defines a basic building block with convolutional layers and batch normalization.
- `ChessNet` class defines the overall architecture using multiple residual blocks for feature extraction and a final output layer for move prediction.

### Model Training:

- Model trained using a supervised learning approach.
- CrossEntropyLoss used as the loss function, considering two output heads for start and end positions of the move.
- Stochastic Gradient Descent (SGD) used as the optimizer.
- Training loop runs for a specified number of epochs, iterating over batches of data, calculating loss, and updating model parameters.

## Getting Started

### Prerequisites

Make sure you have the following dependencies installed:

- Python (>=3.6)
- Django (==4.2.7)
- python-chess (==1.10.0)

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/enansaif/chess_project.git
    cd chess_project
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Run the development server:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and navigate to [http://localhost:8000/] to access the Chess Application.

## Usage

- Access the homepage to start playing chess.
- Make moves using the interactive chessboard interface.
- Choose minimax or AI model for the opponent.
- Play against the opponent.

## Dependencies

- [Django](https://www.djangoproject.com/) (==4.2.7)
- [python-chess](https://python-chess.readthedocs.io/) (==1.10.0)

Happy gaming!
