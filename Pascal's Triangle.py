def pascals_triangle(n):
    ans = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(1, len(ans[-1])):
            temp.append(ans[-1][j - 1] + ans[-1][j])
        temp.append(1)
        ans.append(temp)
    print(ans)


if __name__ == '__main__':
    n = 5
    pascals_triangle(n)
