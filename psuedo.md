1's represent player 1, -1's represent player 2, and 0's represent empty squares on the board

```
def initial(board):
    int lastMoved // will be 1 if player 1 moved last, -1 if player 2 moved last
    List moves // sequence of moves in reversed game

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
    
    reverse(board, lastMoved, moves)

    return moves

def reverse(board, lastMoved, moves):
    for every square on board:
        if square == lastMoved:
            square = 0 // making square empty
            bestMove = findBestMove(board) // calls function which uses minimax to find the best move
            if bestMove is square:
                moves.add(square)
                reverse(board, -1 * lastMoved) // calling our function with the removed square and opposite player
            square = lastMoved

def findBestMove(board):
    //minimax

