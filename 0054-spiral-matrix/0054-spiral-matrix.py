class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left_boundary = 0
        right_boundary = len(matrix[0]) - 1
        up_boundary = 0
        down_boundary = len(matrix) - 1
        res = []
        side = 0
        while left_boundary <= right_boundary and up_boundary <= down_boundary:
            match(side % 4):
                case 0:
                    for j in range(left_boundary, right_boundary + 1):
                        res.append(matrix[up_boundary][j])
                    up_boundary += 1
                case 1:
                    for k in range(up_boundary, down_boundary + 1):
                        res.append(matrix[k][right_boundary])
                    right_boundary -= 1
                case 2:
                    for l in range(right_boundary, left_boundary - 1, -1):
                        res.append(matrix[down_boundary][l])
                    down_boundary -= 1
                case 3:
                    for m in range(down_boundary, up_boundary - 1, -1):
                        res.append(matrix[m][left_boundary])
                    left_boundary += 1
            side += 1
        return res  