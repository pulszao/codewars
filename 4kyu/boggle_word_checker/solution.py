def find_word(board, word):
    def dfs(x, y, index, visited):
        if index == len(word):
            return True
        if (x < 0 or x >= rows or
            y < 0 or y >= cols or
            (x, y) in visited or
            board[x][y] != word[index]):
            return False

        visited.add((x, y))
        for dx, dy in directions:
            if dfs(x + dx, y + dy, index + 1, visited):
                return True
        visited.remove((x, y))
        return False
    
    valid = False
    # Validate rows
    for row in board:
        row_word = ''.join(row)
        if word in row_word:
            return True
    
    # Validate columns
    for col in zip(*board):
        col_word = ''.join(col)
        if word in col_word:
            return True
    

    # Check each cell for potential DFS start
    rows = len(board)
    cols = len(board[0])
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),  (1, 1)]
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0]:
                if dfs(i, j, 0, set()):
                    return True
    return False


if __name__ == '__main__':
    testBoard = [
      ["E","A","R","A"],
      ["N","L","E","C"],
      ["I","A","I","S"],
      ["B","Y","O","R"]
    ]

    print(find_word(testBoard, 'EARS'))
    print(find_word(testBoard, 'BAILER'))
    print(find_word(testBoard, 'CEREAL'))
