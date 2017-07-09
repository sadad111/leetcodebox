# public class Solution {
#     public char[][] updateBoard(char[][] board, int[] click) {
#         int m = board.length, n = board[0].length;
#         int row = click[0], col = click[1];
#
#         if (board[row][col] == 'M') { // Mine
#             board[row][col] = 'X';
#         }
#         else { // Empty
#             // Get number of mines first.
#             int count = 0;
#             for (int i = -1; i < 2; i++) {
#                 for (int j = -1; j < 2; j++) {
#                     if (i == 0 && j == 0) continue;
#                     int r = row + i, c = col + j;
#                     if (r < 0 || r >= m || c < 0 || c >= n) continue;
#                     if (board[r][c] == 'M' || board[r][c] == 'X') count++;
#                 }
#             }
#
#             if (count > 0) { // If it is not a 'B', stop further DFS.
#                 board[row][col] = (char)(count + '0');
#             }
#             else { // Continue DFS to adjacent cells.
#                 board[row][col] = 'B';
#                 for (int i = -1; i < 2; i++) {
#                     for (int j = -1; j < 2; j++) {
#                         if (i == 0 && j == 0) continue;
#                         int r = row + i, c = col + j;
#                         if (r < 0 || r >= m || c < 0 || c >= n) continue;
#                         if (board[r][c] == 'E') updateBoard(board, new int[] {r, c});
#                     }
#                 }
#             }
#         }
#
#         return board;
#     }
# }
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        queue = collections.deque()
        queue.append((click[0], click[1]))
        valid_neighbours = lambda (i, j): 0<=i<m and 0<=j<n

        while queue:
            x, y = queue.pop()
            if board[x][y] == 'M':
                board[x][y] = 'X'
            else:
                # Filter out the valid neighbours
                neighbours = filter(valid_neighbours, [(x-1, y), (x+1, y),
                    (x, y-1), (x, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)])
                # Count the number of mines amongst the neighbours
                mine_count = sum([board[i][j]=='M' for i, j in neighbours])
                # If at least one neighbour is a potential mine, store the mine count.
                if mine_count > 0:
                    board[x][y] = str(mine_count)
                # If no neighbour is a mine, then add all unvisited neighbours
                # to the queue for future processing
                else:
                    board[x][y] = 'B'
                    queue.extend([(i, j) for (i, j) in neighbours if board[i][j]=='E'])
        return board
