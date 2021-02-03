
import random

def start_game(n):
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    return matrix

def add_new_two(mat):
    a = random.randint(0, len(mat)-1)
    b = random.randint(0, len(mat)-1)
    while(mat[a][b] != 0):
        a = random.randint(0, len(mat)-1)
        b = random.randint(0, len(mat)-1)
    mat[a][b] = 2
    return mat

def get_current_state(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 2048:
                return 'WIN'
    for i in range(len(mat)-1):
        for j in range(len(mat[0])-1):
            if mat[i][j] == mat[i+1][j] or mat[i][j+1] == mat[i][j]:
                return 'GAME NOT OVER'
            
    for i in range(len(mat)): 
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'
    for k in range(len(mat)-1): 
        if mat[len(mat)-1][k] == mat[len(mat)-1][k+1]:
            return 'GAME NOT OVER'
    for j in range(len(mat)-1):
        if mat[j][len(mat)-1] == mat[j+1][len(mat)-1]:
            return 'GAME NOT OVER'
        
    return 'LOST'


def get_reverse(mat):
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0])-j-1])
    return new



def get_transpose(mat):
    new = []
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new



def cover_numbers(mat):
    new = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    done = False
    for i in range(4):
        count = 0
        for j in range(4):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return (new, done)


def merge_numbers(mat):
    done = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                done = True
    return (mat, done)


def move_up(game):
    
  
    game = get_transpose(game)
    game, done = cover_numbers(game)
    temp = merge_numbers(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_numbers(game)[0]
    game = get_transpose(game)
    return (game, done)


def move_down(game):
    
    game = get_reverse(get_transpose(game))
    game, done = cover_numbers(game)
    temp = merge_numbers(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_numbers(game)[0]
    game = get_transpose(get_reverse(game))
    return (game, done)


def move_left(game):
    
    
    game, done = cover_numbers(game)
    temp = merge_numbers(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_numbers(game)[0]
    return (game, done)


def move_right(game):
    
    
    game = get_reverse(game)
    game, done = cover_numbers(game)
    temp = merge_numbers(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_numbers(game)[0]
    game = get_reverse(game)
    return (game, done)
