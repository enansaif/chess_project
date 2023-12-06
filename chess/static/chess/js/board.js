function pieceTheme (piece) {
    return 'static/chess/img/chesspieces/' + piece + '.png'
}

var config = {
    pieceTheme: pieceTheme,
    position: 'start',
    draggable: true,
    dropOffBoard: 'snapback',
}
var board = Chessboard('board', config)
  
$('#startBtn').on('click', board.start)
$('#clearBtn').on('click', board.clear)