# Game Tic Tac Toe

def print_board(mtrx):
    # Prosedur untuk print board game Tic Tac Toe
    # Input : mtrx  : array [1..3] of array [1..3] of str

    # KAMUS LOKAL
    # x, y  : int   { Untuk pengulangan }

    # ALGORITMA
    for y in range(3):
        for x in range(3):
            print(mtrx[y][x],end='')
        print('')

def check_win(mtrx):
    # Fungsi yang mengembalikan pesan "Horizontal Win" atau "Vertical Win" atau "Diagonal Win" 
    # jika sudah ada pemain yang menang (1 garis horizontal atau 1 garis vertikal atau
    # 1 garis diagonal dipenuhi oleh salah satu pemain) dan "No" jika belum ada yang menang

    # Input : mtrx  : array [1..3] of array [1..3] of str
    # Output: str

    # KAMUS LOKAL
    
    # ALGORITMA
    # Horizontal Check
    if mtrx[0][0] == mtrx[0][1] == mtrx[0][2] and mtrx[0][0] != '#':
        return 'Horizontal Win'
    elif mtrx[1][0] == mtrx[1][1] == mtrx[1][2] and mtrx[1][0] != '#':
        return 'Horizontal Win'
    elif mtrx[2][0] == mtrx[2][1] == mtrx[2][2] and mtrx[2][0] != '#':
        return 'Horizontal Win'
    
    # Vertical Checks
    elif mtrx[0][0] == mtrx[1][0] == mtrx[2][0] and mtrx[0][0] != '#':
        return 'Vertical Win'
    elif mtrx[0][1] == mtrx[1][1] == mtrx[2][1] and mtrx[0][1] != '#':
        return 'Vertical Win'
    elif mtrx[0][2] == mtrx[1][2] == mtrx[2][2] and mtrx[0][2] != '#':
        return 'Vertical Win'
    
    # Diagonal Checks
    elif mtrx[0][0] == mtrx[1][1] == mtrx[2][2] and mtrx[0][0] != '#':
        return 'Diagonal Win'
    elif mtrx[0][2] == mtrx[1][1] == mtrx[2][0] and mtrx[0][2] != '#':
        return 'Diagonal Win'
    else:
        return 'No'

def full_board(mtrx):
    # Fungsi return True jika board game sudah penuh
    # Input : mtrx      : array [1..3] of array [1..3] of str
    # Output: is_full   : bool

    # KAMUS LOKAL
    # x, y  : int   { Untuk pengulangan }

    # ALGORITMA
    is_full = True
    y = 0
    while y < 3 and is_full:
        x = 0
        while x < 3 and is_full:
            if mtrx[y][x] == '#':
                is_full = False

            x += 1

        y += 1

    return is_full


def tic_tac_toe():
    # Prosedur untuk bermain Tic Tac Toe
    
    # KAMUS LOKAL
    # is_win, is_board_full, is_input_valid, play_again, valid_response : bool
    # turn, x_pos, y_pos : int
    # constant max_turn : int
    # player, response : char

    # ALGORITMA
    
    play_again = True               # Cek players ingin bermain lagi atau tidak
    turn = 1                        # Menghitung banyak turn yang sudah lewat
    max_turn = 9                    # Variabel konstan jumlah turn maksimum

    while play_again:
        is_win = False              # Cek sudah ada yang menang atau belum
        is_board_full = False       # Cek board game sudah penuh dengan isi player

        board_mtrx = [['#' for i in range(3)] for j in range(3)]    # Insialisasi board game
        print('''\nLegends:
# Kosong
X Pemain 1
O Pemain 2 \n''')

        print('Board Status')
        print_board(board_mtrx)
        print('\nX and Y coordinate valued 1 or 2 or 3')

        while (turn <= max_turn) and (not(is_win)) and (not(is_board_full)):
            is_input_valid = False        # Cek input yang dimasukkan valid atau tidak
            while not(is_input_valid):
                if turn % 2 == 1:
                    print('Giliran Pemain \"X\"')
                    player = 'X'
                else:
                    print('Giliran Pemain \"O\"')
                    player = 'O'

                x_pos = int(input('X: '))   # Input koordinat X dari player
                y_pos = int(input('Y: '))   # Input koordinat Y dari player

                if (x_pos < 1 or x_pos > 3) or (y_pos < 1 or y_pos > 3):
                    print('\nKotak tidak valid')
                elif board_mtrx[y_pos - 1][x_pos - 1] != '#':
                    print('\nCell is filled, please choose other cells.')
                else:
                    board_mtrx[y_pos - 1][x_pos - 1] = player
                    print('Board Status')
                    print_board(board_mtrx)
                    is_input_valid = True

            if turn == max_turn:    # Cek turn sudah maksimum atau belum tapi board belum full
                print('DRAW!! No one wins.')
                is_board_full = True
            else: # Turn belum maksimum
                if check_win(board_mtrx) == 'Horizontal Win':
                    print(f'Player \"{player}\" wins horizontally. CONGRATS!')
                    is_win = True
                elif check_win(board_mtrx) == 'Vertical Win':
                    print(f'Player \"{player}\" wins vertically. CONGRATS!')
                    is_win = True
                elif check_win(board_mtrx) == 'Diagonal Win':
                    print(f'Player \"{player}\" wins diagonally. CONGRATS!')
                    is_win = True
                else:
                    turn += 1   # Incremenet jumlah turn

        # Cek player ingin bermain lagi atau tidak
        valid_response = False
        while not(valid_response):
            response = input('Do you want to play again? (y/n)').lower()
            if response == 'n' or response == 'y':
                valid_response = True
                if response == 'n':
                    print('Thank you for playing!!')
                    play_again = False
                else:
                    print('\n=============================')
                    print('Let\'s play again!!\n')
            else:
                print('Please input (y/x)!\n')
