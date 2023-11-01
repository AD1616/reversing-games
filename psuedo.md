1's represent player 1, -1's represent player 2, and 0's represent empty squares on the board

```
def initial(board):
    int lastMoved // will be 1 if player 1 moved last, -1 if player 2 moved last
    List moves // sequence of moves in reversed game, 2D

    if any row, column, or diagonal adds up to 3:
        //player1 won and moved last
        lastMoved = 1
    else if any row, column, or diagonal adds up to -3:
        //player2 won and moved last
        lastMoved = -1
    else:
        if player1 covers more squares:
            //draw and player1 moved last
            lastMoved = 1
        else:
            //draw and player2 moved last
            lastMoved = -1

    moves = reverse(board, lastMoved, moves)

def reverse(board, lastMoved, moves):
    counter = 9
    for every square on board:
        if square == lastMoved:
            square = 0 // making square empty
            bestMove = findBestMove(board) // calls function which uses minimax to find the best move
            if bestMove is square:
                counter -= 1
                moves.add(square)
                reverse(board, -1 * lastMoved) // calling our function with the removed square and opposite player
            if counter == 1:
                return moves
            square = lastMoved



Function isMovesLeft(board):
    For each row i from 0 to 2:
        For each column j from 0 to 2:
            If board[i][j] is empty:
                Return True
    Return False

Function evaluate(board):
    For each row from 0 to 2:
        If all elements in the row are the same:
            If the element is '1':
                Return 10
            Else if the element is '-1':
                Return -10

    For each column from 0 to 2:
        If all elements in the column are the same:
            If the element is '1':
                Return 10
            Else if the element is '-1':
                Return -10

    If both diagonals have the same elements:
        If the element is '1':
            Return 10
        Else if the element is '-1':
            Return -10

    Return 0

Function minimax(board, depth, isMax):
    score = evaluate(board)
    
    If score is 10:
        Return 10
    Else if score is -10:
        Return -10
    Else if there are no empty cells:
        Return 0
    
    If isMax is True:
        best = -1000
        For each row i from 0 to 2:
            For each column j from 0 to 2:
                If board[i][j] is empty:
                    Make the move '1' at (i, j)
                    best = maximum of best and minimax(board, depth + 1, not isMax)
                    Undo the move at (i, j)
        Return best
    Else:
        best = 1000
        For each row i from 0 to 2:
            For each column j from 0 to 2:
                If board[i][j] is empty:
                    Make the move '-1' at (i, j)
                    best = minimum of best and minimax(board, depth + 1, not isMax)
                    Undo the move at (i, j)
        Return best

Function findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)
    
    For each row i from 0 to 2:
        For each column j from 0 to 2:
            If board[i][j] is empty:
                Make the move '1' at (i, j)
                moveVal = minimax(board, 0, False)
                Undo the move at (i, j)
                
                If moveVal is greater than bestVal:
                    Update bestMove to (i, j)
                    Update bestVal to moveVal
    
    Print "The value of the best Move is:", bestVal
    Return bestMove
