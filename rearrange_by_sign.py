def rearrange_by_sign_ap1(arr):
    i, j = 0, (len(arr) - 1)
    count = 0
    while i <= (len(arr) - 2):
        count += 1
        if arr[i] > 0:
            i += 2
        elif arr[j] < 0:
            j -= 2
        else:
            arr[i], arr[j] = arr[j], arr[i]
    print(count)
    return arr


def rearrange_by_sign_ap2(arr):
    ans = [0] * len(arr)
    pos_index = 0
    neg_index = 1
    for i in range(len(arr)):
        if arr[i] < 0:
            ans[neg_index] = arr[i]
            neg_index += 2
        else:
            ans[pos_index] = arr[i]
            pos_index += 2
        print(ans)
    return ans


if __name__ == '__main__':
    # arr = [3, 1, -2, -5, 2, -4]
    arr = [-3, 1, -2, 5, -2, 4]
    # arr = [3, 1, 2, -5, -2, -4]
    # arr = [-3, 1]
    print(rearrange_by_sign_ap1(arr))
    # print(arr)
