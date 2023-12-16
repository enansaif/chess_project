piece_weights = {"p": 200, "n": 400, "b": 500, "r": 500, "q": 1000, "k": 2000}
position_weights = {
    'p': (   0,   0,   0,   0,   0,   0,   0,   0,
            80,  85,  85,  75, 100,  85,  85,  90,
            10,  30,  20,  45,  40,  30,  45,   5,
           -15,  15,  -5,  15,  15,   0,  15, -15,
           -25,   5,  10,  10,   5,   0,   0, -25,
           -25,  10,   5, -10, -10,  -5,   5, -20,
           -30,   5,  -5, -35, -35, -15,   5, -30,
             0,   0,   0,   0,   0,   0,   0,   0),
    'n': ( -65, -55, -75, -75, -10, -55, -55, -70,
            -5,  -5, 100, -35,   5,  65,  -5, -15,
            10,  65,   0,  75,  75,  25,  60,  -5,
            25,  25,  45,  35,  35,  40,  25,  15,
            -5,   5,  30,  20,  20,  35,   0,   0,
           -20,  10,  15,  20,  20,  15,  10, -15,
           -25, -15,   5,   0,   5,   0, -25, -20,
           -75, -25, -25, -25, -20, -35, -20, -70),
    'b': ( -60, -80, -80, -75, -25,-105, -35, -50,
           -10,  20,  35, -40, -40,  30,   0, -20,
           -10,  40, -30,  40,  50, -10,  30, -15,
            25,  15,  20,  35,  25,  25,  15,  10,
            15,  10,  15,  25,  15,  15,   0,   5,
            15,  25,  25,  15,  10,  25,  20,  15,
            20,  20,  10,   5,   5,   5,  20,  15,
            -5,   5, -15, -15, -15, -15, -10, -10),
    'r': (  35,  30,  35,   5,  35,  35,  55,  50,
            55,  30,  55,  65,  55,  65,  35,  60,
            20,  35,  30,  35,  45,  25,  25,  15,
            -5,   5,  15,  15,  20,  -5, -10,  -5,
           -30, -35, -15, -20, -15, -30, -45, -30,
           -40, -30, -45, -25, -25, -35, -25, -45,
           -55, -40, -30, -25, -30, -45, -45, -55,
           -30, -25, -20,   5,  -5, -20, -30, -30),
    'q': (   5,   0, -10,-105,  70,  25,  85,  25,
            15,  35,  60, -10,  20,  75,  55,  25,
            -5,  45,  30,  60,  70,  65,  45,   5,
            -5, -15,  20,  15,  25,  20, -15,  -5,
           -15, -15,  -5,  -5,  -5, -10, -20, -25,
           -30,  -5, -15, -10, -15, -10, -15, -25,
           -35, -20,   0, -20, -15, -15, -20, -40,
           -40, -30, -30, -15, -30, -35, -35, -40),
    'k': (   5,  50,  50,-100,-100,  60,  80, -60,
           -30,  10,  55,  55,  55,  55,  10,   5,
           -60,  10, -55,  45, -65,  30,  35, -30,
           -55,  50,  10,  -5, -20,  15,   0, -50,
           -55, -45, -50, -30, -50, -50, -10, -50,
           -45, -45, -45, -80, -65, -30, -30, -30,
            -5,   5, -15, -50, -55, -20,  15,   5,
            15,  30,  -5, -15,   5,  -5,  40,  15),
}
