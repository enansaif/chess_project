function pieceTheme(piece) {
  return "static/chess_app/img/chesspieces/" + piece + ".png";
}

function updateGame(json_data) {
  legal_moves = json_data["legal_moves"].split(",");
  promotions = json_data["promotions"].split(",");
  curr_board = json_data["curr_board"];
  is_game_over = json_data["is_game_over"];
  is_check = json_data["is_check"];

  let status = document.getElementById("status");
  if (is_game_over) {
    status.innerHTML =
      '<span class="bg-danger pb-1 px-2 rounded">Game Over</span>';
  } else if (is_check) {
    status.innerHTML =
      '<span class="bg-warning pb-1 px-2 rounded">Check</span>';
  } else {
    status.innerHTML =
      '<span class="bg-success pb-1 px-2 rounded">Active</span>';
  }
}

function onDrop(source, target) {
  let move = source + target;
  if (!legal_moves.includes(move)) {
    return "snapback";
  }

  if (promotions.includes(move)) {
    let selectedOption = document.querySelector('input[name="piece"]:checked');
    if (confirm("Promote pawn to " + selectedOption.id + "?") == false) {
      return "snapback";
    }
    move += selectedOption.value;
  }

  const xhttp = new XMLHttpRequest();
  xhttp.onload = function () {
    let json_data = JSON.parse(this.responseText);
    updateGame(json_data);

    setTimeout(() => {
      board.position(curr_board);
      isMoveComplete = true;
    }, 100);
  };
  isMoveComplete = false;
  let model = document.querySelector('input[name="model"]:checked').value;
  xhttp.open("POST", game_url, true);
  xhttp.setRequestHeader("Content-Type", "application/json");
  xhttp.setRequestHeader("X-CSRFToken", csrf_token);
  xhttp.send(JSON.stringify({ move, model }));
}

function hitURL(url) {
  const xhttp = new XMLHttpRequest();
  xhttp.onload = function () {
    let json_data = JSON.parse(this.responseText);
    updateGame(json_data);
    board.position(curr_board);
  };

  xhttp.open("POST", url, true);
  xhttp.setRequestHeader("X-CSRFToken", csrf_token);
  xhttp.send();
}

function resetGame() {
  if (isMoveComplete) {
    hitURL(reset_url);
  }
}

function undoMove() {
  if (isMoveComplete) {
    hitURL(undo_url);
  }
}

var config = {
  position: "start",
  pieceTheme: pieceTheme,
  onDrop: onDrop,
  draggable: true,
  showNotation: false,
};
var isMoveComplete = true;
var board = Chessboard("board", config);
$(window).resize(board.resize);
