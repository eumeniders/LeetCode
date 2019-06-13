class Solution(object):
    def isword(self,board,word,i,j,k):
        if k==len(word):
            return True
        if i<0 or i>len(board)-1 or j<0 or j>len(board[0])-1 or board[i][j]!=word[k]:
            return False
        tmp = board[i][j]
        board[i][j]='#'
        res = self.isword(board,word,i+1,j,k+1) or self.isword(board,word,i-1,j,k+1) or self.isword(board,word,i,j+1,k+1) or self.isword(board,word,i,j-1,k+1)
        board[i][j]=tmp
        return res
            

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word)>len(board[0])*len(board):
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.isword(board,word,i,j,0):
                    return True
        return False
