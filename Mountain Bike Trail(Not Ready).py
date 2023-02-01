
## REspuesta
from itertools import accumulate
TILES = "_-‾"

def draw_trail(trail):
    hs    = [*accumulate(trail)]
    min_h = min(hs)
    base  = min_h - min_h%3
    but   = min_h//3
    up    = max(hs)//3
    
    H     = up-but+3
    blank = ' ' * (len(trail)+1)
    board = [list(blank) for _ in range(H)]
    
    for j,h in enumerate(hs):
        i = H-1 - (h-base)//3
        board[i][j] = board[i-2][j+1] = TILES[h%3]
    
    return '\n'.join(map(''.join,board))

print(draw_trail([-2, 1, 0, 0, -1, 1, 0, 0, -1, -1, 0, 0]))

#### Otra Forma#####

from itertools import accumulate

def draw_trail(trail):
    trail = [*accumulate(trail)]
    max_h = max(trail) // 3
    drawing = [[' '] * (len(trail)+1) for _ in range(max_h+3-min(trail)//3)]
    for t, height in enumerate(trail):
        for y0, x0 in ((max_h, 1), (max_h+2, 0)):
            drawing[y0-height//3][x0+t] = '_-‾'[height%3]
    return '\n'.join(map(''.join, drawing))