function pieceTheme (piece) {
    return 'static/chess_app/img/chesspieces/' + piece + '.png';
}

function updateGame(json_data){
    legal_moves = json_data['legal_moves'].split(',');
    promotions = json_data['promotions'].split(',');
    curr_board = json_data['curr_board'];
    is_game_over = json_data['is_game_over'];
    is_check = json_data['is_check'];
}

function onDrop (source, target) {
    let move = source + target
    if (!(legal_moves.includes(move))) {
        return'snapback';
    }

    if (promotions.includes(move)) {
        let selectedOption = document.querySelector('input[name="piece"]:checked');
        move += selectedOption.value;
    }

    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        let json_data = JSON.parse(this.responseText);
        updateGame(json_data)

        if (!(is_game_over)){
            setTimeout(() => {
                board.position(curr_board);
            }, 100);
        } else {
            let status = document.getElementById('status');
            status.innerText = 'Game Over';
        }
    }

    xhttp.open("POST", game_url, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.setRequestHeader("X-CSRFToken", csrf_token);
    xhttp.send(JSON.stringify({move}));
}

function resetGame() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        let json_data = JSON.parse(this.responseText);
        updateGame(json_data)
        board.position(curr_board);
    }

    xhttp.open("POST", reset_url, true);
    xhttp.setRequestHeader("X-CSRFToken", csrf_token);
    xhttp.send();
}

var config = {
    position: 'start',
    pieceTheme: pieceTheme,
    onDrop: onDrop,
    draggable: true,
    showNotation: false,
}
var board = Chessboard('board', config);
$(window).resize(board.resize);