class Solution(object):
    def word(self,board,i,j,r):
        if len(r)==0:
            return True
        if 0<=i<len(board) and 0<=j<len(board[0]) and board[i][j]==r[0]:
            tmp = board[i][j]
            board[i][j]='#'
            status=self.word(board,i+1,j,r[1:]) or self.word(board,i-1,j,r[1:]) or self.word(board,i,j+1,r[1:]) or self.word(board,i,j-1,r[1:])
            board[i][j]=tmp
            return status
        else:
            return False
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for x in words:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if x[0]==board[i][j]:
                        if self.word(board,i,j,x):
                            res.append(x)
        return list(set(res))
