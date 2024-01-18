def fun():
    ls = [1, 2, 3, 4, 5, 6]
    print(ls)
    for i in range(5):
        ls.insert(0, ls.pop())
        print(ls)


if __name__ == '__main__':
    fun()
