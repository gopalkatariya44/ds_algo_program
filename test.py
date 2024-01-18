def candy(ratings):
    n = len(ratings)
    candies = [1] * n

    for i in range(1, n):
        if ratings[i - 1] < ratings[i]:
            candies[i] = candies[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)


if __name__ == '__main__':
    # print(candy([3, 4, 4, 3]))
    # print(candy([1, 0, 2]))
    # print(candy([1, 2, 2]))
    print(100 << 1)
