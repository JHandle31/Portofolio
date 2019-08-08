import random, time
class Chessboard(object):
    """docstring for Chessboard"""
    global board
    board = []
    board_s = 8
    def __init__(self):
        super(Chessboard, self).__init__()
        self.generate_board(self.board_s)

    def generate_board(self, board_size):
        for i in range(board_size):
            la = []
            for j in range(board_size):
                la.append(0)
            board.append(la)

    def reset_board(self):
        for p in range(len(board)):
            for a in range(len(board[p])):
                board[p][a] = "--"

    def board_update(self, pt, pb):
        self.reset_board()
        for p in pt:
            board[p.get_position()[1]][p.get_position()[0]] = p.abbr
        for p in pb:
            board[p.get_position()[1]][p.get_position()[0]] = p.abbr

    def print_board(self):
        for a in board:
            print(a)

    def get_board(self):
        return board

class chess_piece(object): #1 = pawn, 2 = tower, 3 = knight, 4 = bishop, 5 = queen, 6 = king
    directions = []
    speed = 0
    x = 0
    y = 0
    board_side = 0
    piece = 0
    name = ""
    score = 0
    abbr = ''

    def __init__(self,board_side, x, y, piece):
        self.x = x
        self.y = y
        self.board_side = board_side
        self.piece = piece
        if(piece == 1):
            self.pawn()
        if(piece == 2):
            self.tower()
        if(piece == 3):
            self.knight()
        if(piece == 4):
            self.bishop()
        if(piece == 5):
            self.queen()
        if(piece == 6):
            self.king()

    def pawn(self):
        if(self.board_side == 0):
            self.directions = [[0,1]]
        else:
            self.directions = [[0,-1]]
        self.speed = 1
        self.name = "Pawn"
        self.score = 1
        self.abbr = "PA"

    def queen(self):
        self.directions = [[0,1], [1,0], [-1,0], [0,-1], [1,1], [-1,1], [1,-1], [-1,-1]]
        self.speed = 20
        self.name = "Queen"
        self.score = 9
        self.abbr = "QU"

    def king(self):
        self.directions = [[0,1], [1,0], [-1,0], [0,-1]]
        self.speed = 1
        self.name = "King"
        self.score = 100
        self.abbr = "KI"

    def tower(self):
        self.directions = [[0,1], [1,0], [-1,0], [0,-1],]
        self.speed = 20
        self.name = "Tower"
        self.score = 5
        self.abbr = "TO"

    def bishop(self):
        self.directions = [[1,1], [-1,1], [1,-1], [-1,-1]]
        self.speed = 20
        self.name = "Bishop"
        self.score = 3
        self.abbr = "BI"

    def knight(self):
        self.directions = [[1,2], [2,1], [-1,2], [-1,-2], [-2,1], [-2,-1], [2,-1], [1,-2]]
        self.speed = 1
        self.name = "Knight"
        self.score = 3
        self.abbr = "KN"


    def possible_moves(self, chessboard, turn):
        pos_moves = []
        if(turn < 1 and self.piece == 1):
            self.speed = 2
        for dir in self.directions:
            for sp in range(self.speed):
                new_x = self.x + (dir[0] * (sp+1))
                new_y = self.y + (dir[1] * (sp+1))
                if(new_x >= 0 and new_x < 8 and new_y >= 0 and new_y < 8):
                    if(self.check_for_collision(chessboard, new_x, new_y) and self.piece != 1):
                        piece_opponent = self.get_piece(new_x, new_y, self.board_side)
                        if(piece_opponent != 0 and piece_opponent.board_side != self.board_side):
                            pos_moves.append([new_x, new_y, piece_opponent.score])
                    else:
                        pos_moves.append([new_x, new_y, 0])

                    if(self.piece == 1):
                        hit_directions = []
                        if(self.board_side == 0):
                            hit_directions = [[1,1], [-1,1]]
                        else:
                            hit_directions = [[1,-1], [-1,-1]]
                        for hdir in hit_directions:
                            new_x = self.x+hdir[0]
                            new_y = self.y+hdir[1]
                            if(new_x >= 0 and new_x < 8 and new_y >= 0 and new_y < 8):
                                if(self.check_for_collision(chessboard, new_x, new_y)):
                                    piece_opponent = self.get_piece(new_x, new_y, self.board_side)
                                    if(piece_opponent != 0):
                                        pos_moves.append([new_x, new_y, piece_opponent.score])

        return pos_moves

    def check_for_collision(self, chessboard, x, y):
        if(chessboard[y][x] != 0):
            return True
        return False

    def get_piece(self, x, y, board_side):
        #if(board_side == 0):
        for piece in p_1:
            #print([x,y])
            if(piece.get_position() == [x,y]):
                return piece
        #else:
        for piece in p_0:
            #print([x,y])
            if(piece.get_position() == [x,y]):
                return piece
        return 0


    def get_position(self):
        return [self.x,self.y]

    def get_name(self):
        return self.name

    def get_side(self):
        return self.board_side

    def get_chess_pos(self):
        return "{}{}".format(chr(self.x+65),self.y+1)

    def get_chess_pos_coors(self,coors):
        return "{}{}".format(chr(coors[0]+65),coors[1]+1)

    def set_new_coors(self,coor, team):
        if(coor[2] > 0):
            opponent_piece = self.get_piece(coor[0], coor[1], team)
            opponent_piece.score = 0
        self.x = int(coor[0])
        self.y = int(coor[1])


board_layout = [	[2,3,4,5,6,4,3,2],
                    [1,1,1,1,1,1,1,1],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [1,1,1,1,1,1,1,1],
                    [2,3,4,6,5,4,3,2]	]



def generate_pieces(board):
    pieces_0 = []
    pieces_1 = []
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j] != 0):
                if(i < 4):
                    pieces_0.append(chess_piece(0,j,i,board[i][j]))
                    print(j,i,board[i][j])
                else:
                    pieces_1.append(chess_piece(1,j,i,board[i][j]))
    return pieces_0, pieces_1

p_0, p_1 = generate_pieces(board_layout)
turn = 0

def get_team_points(team):
    total = 0
    for piece in team:
        total += piece.score
    return total

def t_move(turn, chessb, team):
    pm_arr = []
    team_c = p_1
    if(team == 1):
        team_c = p_0

    for p in team_c: #Get all the pieces that can make a move of player1
        if(len(p.possible_moves(chessb, turn)) > 0):
            pm_arr.append(p)

    x = random.choice(pm_arr)
    random_choice = (random.choice(x.possible_moves(chessb, turn)))
    x.set_new_coors(random_choice, team)

def game_cycle(turn, chessb):
    t_move(turn, chessb, 1)
    t_move(turn, chessb, 2)
    chessboard.board_update(p_0, p_1)
    print("Team 1 has {} points \nTeam 2 has {} points".format(get_team_points(p_0), get_team_points(p_1)))
    chessboard.print_board()
    turn += 1


chessboard = Chessboard()
chessboard.board_update(p_0, p_1)
chessboard.print_board()
for i in range(50):
    game_cycle(turn, chessboard.get_board())
    #time.sleep(2)


#chessboard.board_update(p_0, p_1)
#chessboard.print_board()
#game_cycle(turn, chessboard.get_board())

#chessboard.board_update(p_0, p_1)
#chessboard.print_board()
