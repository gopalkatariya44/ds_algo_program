from math import log10, log

if __name__ == '__main__':
    n = int(input("enter digit: "))
    c = 0
    re = 0
    # Approach1
    while n > 0:
        last = n % 10
        print(f"{re} * {10} + {last} = {re}")
        re = (re * 10) + last
        n = int(n/10)
        c += 1
        # print(last)
    print(re)

    # # Approach2
    # c = int(log10(n)) + 1
    # l = int(log(n))
    #
    # print(c)
    # print(l)
