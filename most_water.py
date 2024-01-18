def most_water(height_list):
    ans, i, j = 0, 0, len(height_list) - 1
    while i < j:
        temp = 0
        if height_list[j] >= height_list[i]:
            temp = height_list[i] * (j - i)
            i += 1
        else:
            temp = height_list[j] * (j - i)
            j -= 1
        if temp > ans: ans = temp

    # for i in range(len(height_list)):
    #     tem = 0
    #     for j in range(len(height_list) - 1, 0, -1):
    #         tem = min(height_list[i], height_list[j]) * (j - i)
    #
    #         if tem > ans:
    #             ans = tem
    return ans


if __name__ == '__main__':
    height = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 8, 8]
    print(most_water(height))
