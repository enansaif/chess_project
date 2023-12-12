function pieceTheme (piece) {
    return 'static/chess_app/img/chesspieces/' + piece + '.png';
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

        legal_moves = json_data['legal_moves'].split(',');
        promotions = json_data['promotions'].split(',');
        is_game_over = json_data['is_game_over'];

        if (!(is_game_over)){
            board.position(json_data['curr_board']);
        } else {
            let status = document.getElementById('status');
            status.innerText = 'Game Over';
        }
    }

    xhttp.open("POST", game_url, true); // game url sent from rendered template
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.setRequestHeader("X-CSRFToken", csrf_token);
    xhttp.send(JSON.stringify({move}));
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