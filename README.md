# Chess Application README

This Chess Application is a web-based chess game developed using Django, the python-chess library and chessboard.js library. 
The application allows users to play chess against an AI opponent using different algorithms for move prediction.

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
- Choose an AI model (minimax or random, other 2 are currently under development and are set to random) for the AI opponent.
- Reset, undo, or redo moves as needed during the game.

## Dependencies

- [Django](https://www.djangoproject.com/) (==4.2.7)
- [python-chess](https://python-chess.readthedocs.io/) (==1.10.0)

Happy gaming!
