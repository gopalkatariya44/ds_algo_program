class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0

        for num in num1:
            print(n1 * 10, ord(num) - 48)
            n1 = n1 * 10 + ord(num) - 48
        print(n1)

        for num in num2:
            n2 = n2 * 10 + ord(num) - 48

        return f"{n1 * n2}"


class Parent():
    def __call__(self, *args, **kwargs):
        print("hey")


class Test(Parent):
    def test1(self):
        print("test1")

    def test2(self):
        print("test2")

    def test3(self):
        print("test3")


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


    def isValidSudoku(board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    print([(i, element), (element, j), (i // 3, j // 3, element)])
                    print(res)
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
                    print(res)
        return len(res) == len(set(res))

    isValidSudoku(board)


