def rec(n, i=1):
    print(f"{i}.gopal")
    if i == n:
        return 1
    else:
        rec(n, i + 1)
    print(f"exit -> {i}")


arr = [1, 2, 3, 4, 5, 6]


def swap(s, e):
    # temp = 0
    # temp = arr[s]
    # arr[s] = arr[e]
    # arr[e] = temp
    arr[s], arr[e] = arr[e], arr[s]


def reverse_arr(s, e):
    global arr
    if s >= e:
        return 0
    swap(s, e)
    print(arr)
    reverse_arr(s + 1, e - 1)


def palindrome(i, s, n):
    if i >= n / 2:
        print('palindrome')
        return 0
    elif s[i] != s[n - i - 1]:
        print("not palindrome")
        return 0
    palindrome(i + 1, s, n)


def fn(n):
    if n <= 1:
        return n
    else:
        return fn(n - 1) + fn(n - 2)


def climb(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb(n - 1) + climb(n - 2)


def climb1(n):
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 2
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        print(dp[i - 1] + dp[i - 2], dp[i - 1], dp[i - 2])
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp)
    return dp[n]


def count_num():
    arr = [0 for i in range(0, 10)]

    # ar = [0, 3, 5, 7, 8, 2, 3, 6, 8]
    ar = ["a", "b", "c", "a", "d", "d"]

    for i in ar:
        arr[ord(i) - ord("a")] += 1

    print(arr)


def maxArea(height) -> int:
    ans, i, j = 0, 0, len(height) - 1
    while i < j:
        if height[i] <= height[j]:
            res = height[i] * (j - i)
            i += 1
        else:
            res = height[j] * (j - i)
            j -= 1
        if res > ans: ans = res
    return ans


def count_num_dict():
    c_map = {}
    ar = [1, 8, 8, 2, 5, 4, 8, 3, 1]

    for i in ar:
        if str(i) in c_map:
            c_map[str(i)] += 1
        else:
            c_map[str(i)] = 1
    print(c_map)


def selection_sort(arr, size):
    for i in range(size):
        print(f"step={i}")
        print(arr)
        min = i
        for j in range(i + 1, size):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]

    print(arr)


def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])
    print(array)


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    print(array)


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            print("1->", array)
            array[j + 1] = array[j]
            print("2->", array)
            j -= 1
        array[j + 1] = key
        print("done")
    print(array)


if __name__ == '__main__':
    # insertion_sort([111, 1, 0, 4, 6, -8, 3])
    # print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(fn(3))

# Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49
#
# Input: height = [1, 1]
# Output: 1
