import json
import chess
from django.shortcuts import render
from django.http import JsonResponse
from .utils import functions
from .game import play

board = chess.Board()
prev_moves = []

def home(request):
    """
    View function for rendering the home page of the chess application.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: Rendered HTML page with the current game state.
    """
    game_state = functions.get_game_state(board)
    return render(request, 'chess_app/index.html', context=game_state)

def play_step(request):
    """
    View function for processing a player's move and updating the game state.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    JsonResponse: JSON response containing the updated game state after the player's move.
    """
    if request.method == 'POST':
        prev_moves.clear()
        move = json.loads(request.body).get('move')
        model = json.loads(request.body).get('model')
        game_state = play(move, board, model)
        return JsonResponse(game_state)

def reset_game(request):
    """
    View function for resetting the chess game to the initial state.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    JsonResponse: JSON response containing the updated game state after resetting the game.
    """
    if request.method == 'POST':
        board.reset()
        prev_moves.clear()
        game_state = functions.get_game_state(board)
        return JsonResponse(game_state)

def undo_move(request):
    """
    View function for undoing the last move in the chess game.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    JsonResponse: JSON response containing the updated game state after undoing the last move.
    """
    if request.method == 'POST':
        if board.move_stack and board.turn == chess.WHITE:
            prev_moves.append(board.pop())
        if board.move_stack and board.turn == chess.BLACK:
            prev_moves.append(board.pop())
        game_state = functions.get_game_state(board)
        return JsonResponse(game_state)

def redo_move(request):
    """
    View function for redoing the last undone moves in the chess game.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    JsonResponse: JSON response containing the updated game state after redoing the last move.
    """
    if request.method == 'POST':
        while prev_moves:
            board.push(prev_moves.pop())
        game_state = functions.get_game_state(board)
        return JsonResponse(game_state)
