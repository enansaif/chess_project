function pieceTheme (piece) {
    return 'static/chess/img/chesspieces/' + piece + '.png'
}

var legal_moves = ['g1h3', 'g1f3', 'b1c3', 'b1a3', 'h2h3', 'g2g3', 'f2f3', 
                   'e2e3', 'd2d3', 'c2c3', 'b2b3', 'a2a3', 'h2h4', 'g2g4', 
                   'f2f4', 'e2e4', 'd2d4', 'c2c4', 'b2b4', 'a2a4']

function onDrop (source, target) {
    let move = source + target
    console.log(move)
    if (!(legal_moves.includes(move))) {
        return 'snapback'
    }
    // http request send the current move made
    // update game return next legal move and ai made move
    // update board with the ai made move
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        console.log(this.responseText);
    }
    xhttp.open("GET", game_url);
    xhttp.send();
}

var config = {
    pieceTheme: pieceTheme,
    onDrop: onDrop,
    position: 'start',
    draggable: true,
    dropOffBoard: 'snapback',
}
var board = Chessboard('board', config)
  
$('#startBtn').on('click', board.start)
