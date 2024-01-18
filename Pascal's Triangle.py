def pascals_triangle(n):
    ans = []
    for i in range(1, n):
        if ans:
            temp = [1]
            for j in range(1, len(ans[-1])):
                temp.append(ans[-1][j - 1] + ans[-1][j])
            temp.append(1)
            ans.append(temp)
        else:
            pass
            temp = []
            for k in range(i):
                temp.append(1)
            ans.append(temp)
    print(ans)


if __name__ == '__main__':
    n = 7
    pascals_triangle(n)
