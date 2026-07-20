from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows  = defaultdict(set)
        cols  = defaultdict(set) 
        boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == '.':
                    continue
                d = board[r][c]
                if d in rows[r] or d in cols[c] or d in boxes[(r//3, c//3)]:
                    return False
                else:
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[(r//3, c//3)].add(d)
        return True
        