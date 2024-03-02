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
    n = 10
    while True:
        ls = [int(i) for i in str(n)]
        print(ls)

        n = sum(ls)

        if n < 10:
            print(n)
            break

    print("syntext error")
