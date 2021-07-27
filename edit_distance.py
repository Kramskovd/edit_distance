# Uses python3

class Matrix:
    def __init__(self, n, m):
        self.matrix = [0]*(n*m)
        self.n = n
        self.m = m

    def get(self, i, j):
        return self.matrix[i*self.m +j]

    def set(self, i, j, value):
        self.matrix[i*self.m + j] = value


def edit_distance(s, t):

    n = len(s) + 1 #строки
    m = len(t) + 1 #столбцы

    matx = Matrix(n, m)

    for k in range(n*m):
        i = k//m
        j = k%m

        if i == 0:
            matx.set(i, j, j)
        elif j == 0:
            matx.set(i, j, i)
        else:
            up = matx.get(i - 1, j)
            mid = matx.get(i - 1, j - 1)
            left = matx.get(i, j - 1)

            if mid <= up and mid <= left:
                if s[i-1] == t[j-1]:
                    matx.set(i, j, mid)
                else:
                    matx.set(i, j, mid + 1)
            elif up <= left:
                matx.set(i, j, up+1)
            else:
                matx.set(i,j, left+1)

    return matx.get(n-1, m-1)


if __name__ == "__main__":
    print(edit_distance(input(), input()))
