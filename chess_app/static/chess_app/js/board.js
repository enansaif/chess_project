function pieceTheme (piece) {
    return 'static/chess_app/img/chesspieces/' + piece + '.png'
}

var legal_moves = ['g1h3', 'g1f3', 'b1c3', 'b1a3', 'h2h3', 'g2g3', 'f2f3', 
                   'e2e3', 'd2d3', 'c2c3', 'b2b3', 'a2a3', 'h2h4', 'g2g4', 
                   'f2f4', 'e2e4', 'd2d4', 'c2c4', 'b2b4', 'a2a4'];
var promotions = [];

function onDrop (source, target) {
    let move = source + target
    
    if (!(legal_moves.includes(move))) {
        return 'snapback'
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
        board.position(json_data['curr_board'], false);
    }

    xhttp.open("POST", game_url, true); // game url sent from rendered template
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.setRequestHeader("X-CSRFToken", csrf_token);
    xhttp.send(JSON.stringify({move}));
}

var config = {
    pieceTheme: pieceTheme,
    onDrop: onDrop,
    position: 'start',
    draggable: true,
    showNotation: false,
}
var board = Chessboard('board', config)
$(window).resize(board.resize)