class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        def dfs(x, y, word):
            if len(word) == 0:
                return True
            #UP
            if x>0 and board[x-1][y] == word[0]:
                temp = board[x][y]
                board[x][y] = '#'
                if dfs(x-1, y, word[1:]):
                    return True
                board[x][y] = temp
            #DOWN
            if x<len(board)-1 and board[x+1][y] == word[0]:
                temp = board[x][y]
                board[x][y] = '#'
                if dfs(x+1, y, word[1:]):
                    return True
                board[x][y] = temp
            #LEFT
            if y>0 and board[x][y-1] == word[0]:
                temp = board[x][y]
                board[x][y] = '#'
                if dfs(x, y-1, word[1:]):
                    return True
                board[x][y] = temp
            #RIGHT
            if y<len(board[0])-1 and board[x][y+1] == word[0]:
                temp = board[x][y]
                board[x][y] = '#'
                if dfs(x, y+1, word[1:]):
                    return True
                board[x][y] = temp
            return False;
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, word[1:]):
                        return True
        return False
            