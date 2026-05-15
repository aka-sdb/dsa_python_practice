"""
Brute Force Solution - As matrix is concerned, so nested loops (2D) [O(n^2)].
Only thing is here, space complexity is involved, where a 1D list is needed
to store all the various elements of the input matrix.
"""
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if (m * n) != (r * c):
            return mat

        elements = []
        for i in range(0, m):
            for j in range(0, n):
                elements.append(mat[i][j])
        
        k = 0
        res = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(0, r):
            for j in range(0, c):
                res[i][j] = elements[k]
                k = k + 1

        return res