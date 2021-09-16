class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        dic = self.root
        for w in word:
            if w not in dic:
                dic[w] = {}
            dic = dic[w]
        dic['#'] = word

class Solution:
    def __init__(self):
        self.Trie = Trie()

    def findWords(self, board, words):

        for word in words:
            self.Trie.insert(word)
        
        m, n = len(board), len(board[0])
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        vis = [[False for _ in range(n)] for _ in range(m)]
        self.ans = []

        def backtrack(i, j, vis, node):
            if '#' in node:
                self.ans.append(node['#'])
            for move in moves:
                I = i + move[0]
                J = j + move[1]
                if 0 <= I < m and 0 <= J < n and vis[I][J] == False and board[I][J] in node:
                    vis[I][J] = True
                    backtrack(I, J, vis, node[board[I][J]])
                    vis[I][J] = False
            return

        self.words = set(words)
        for i in range(m):
            for j in range(n):
                if board[i][j] in self.Trie.root:
                    vis[i][j] = True
                    backtrack(i, j, vis, self.Trie.root[board[i][j]])
                    vis[i][j] = False
        return self.ans