import numpy as np

def print_board(b):
    for row in b: print(f"|{'|'.join(row)}|")

def check_win(b, p):
    return np.any(np.all(b==p, 0)) or np.any(np.all(b==p, 1)) or np.all(np.diag(b)==p) or np.all(np.diag(np.fliplr(b))==p)

def play():
    b = np.full((3,3), ' ')
    p = 'X'
    
    while ' ' in b:
        print_board(b)
        try:
            r, c = map(int, input(f'Player {p} (row,col 0-2): ').split(','))
            if b[r,c] == ' ':
                b[r,c] = p
                if check_win(b, p):
                    print_board(b)
                    print(f'Player {p} wins!')
                    break
                p = 'O' if p == 'X' else 'X'
            else:
                print('Spot taken!')
        except:
            print('Invalid move!')

if __name__ == '__main__':
    play()
