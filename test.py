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
    test = Test()
    test()
