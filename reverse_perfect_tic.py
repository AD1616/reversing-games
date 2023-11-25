import copy


def initial(board):
    initial_state = copy.deepcopy(board)
    moves = [[initial_state]]
    pos = 0
    neg = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                pos += 1
            else:
                neg += 1

    if pos > neg:
        last_moved = 1
    else:
        last_moved = -1
    
    reverse(initial_state, copy.deepcopy(initial_state), last_moved, moves, 8)

    return moves


move_dict = {
    8: set(),
    7: set(),
    6: set(),
    5: set(),
    4: set(),
    3: set(),
    2: set(),
    1: set(),
    0: set()
}


def reverse(initial_state, board, last_moved, moves, move_number):
    if move_number == -1:
        initial_state = copy.deepcopy(initial_state)
        moves.append([initial_state])
        reverse(initial_state, copy.deepcopy(initial_state), last_moved, moves, 8)
        return True

    found = False

    for i in range(len(board)):
        for j in range(len(board[i])):
            # found a square covered by the player whose turn it was
            if board[i][j] == last_moved and (i, j) not in move_dict[move_number]:
                # clearing the square
                board[i][j] = 0
                # passing in the board state without the square,
                # and seeing if the best move matches the square we cleared
                best_moves = find_best_moves(copy.deepcopy(board), last_moved, move_number)
                if (i, j) in best_moves:
                    moves[-1].append(copy.deepcopy(board))
                    move_dict[move_number].add((i, j))
                    found = True
                    # if it was the best move, then continue to the next move
                    return reverse(initial_state, copy.deepcopy(board), -1 * last_moved, moves, move_number - 1)
                    break
                board[i][j] = last_moved

    # if we ever are at a board state where we couldn't find a match,
    # then we are going to remove the last move and try to find another
    # potential board state
    if not found:
        if len(moves[-1]) == 1:
            moves.pop()
            return True
        move_dict[move_number].clear()
        moves[-1].pop()
        return reverse(initial_state, copy.deepcopy(moves[-1][-1]), -1 * last_moved, moves, move_number + 1)


def evaluate(board):
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == 1:
                return 10
            elif board[row][0] == -1:
                return -10
  
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == 1:
                return 10
            elif board[0][col] == -1:
                return -10
  
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == 1:
            return 10
        elif board[0][0] == -1:
            return -10
  
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == 1:
            return 10
        elif board[0][2] == -1:
            return -10
  
    return 0


def minimax(board, depth, max_depth, last_moved, alpha, beta):
    best = 1000 * -1 * last_moved
     
    score = evaluate(board)

    if score == 10:
        return score

    if score == -10:
        return score

    if depth == max_depth:
        return 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                # Make the move
                board[i][j] = last_moved

                # Call minimax recursively and choose
                if last_moved == 1:
                    best = max(best, minimax(copy.deepcopy(board), depth + 1, max_depth, -1 * last_moved, alpha, beta))
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
                else:
                    best = min(best, minimax(copy.deepcopy(board), depth + 1, max_depth, -1 * last_moved, alpha, beta))
                    beta = min(beta, best)
                    if beta <= alpha:
                        break

                # Undo the move
                board[i][j] = 0

    return best


def find_best_moves(board, last_moved, move_number):
    best_moves = set()
    best_val = 1000 * -1 * last_moved

    for i in range(3):
        for j in range(3):
          
            # Check if cell is empty  
            if board[i][j] == 0:
              
                # Make the move  
                board[i][j] = last_moved 
  
                max_depth = 8 - move_number
                move_val = minimax(copy.deepcopy(board), 0, max_depth, -1 * last_moved, -10000, 10000)

                if (last_moved == 1 and move_val > best_val) or (last_moved == -1 and move_val < best_val):
                    best_val = move_val
                    best_moves.clear()
                    best_moves.add((i, j))
                elif move_val == best_val:
                    best_moves.add((i, j))

                # Undo the move  
                board[i][j] = 0

    return best_moves


def tester():
    # ex1 = [
    #     [-1, 1, 1],
    #     [1, -1, -1],
    #     [-1, 1, 1]
    # ]
    # ex2 = [
    #     [1, 1, -1],
    #     [-1, -1, 1],
    #     [1, 1, -1]
    # ]
    ex3 = [
        [1, -1, 1],
        [1, -1, 1],
        [-1, 1, -1]
    ]

    games = initial(ex3)

    for game in games:
        for move in game:
            for i in range(3):
                print(move[i])
            print()


tester()

