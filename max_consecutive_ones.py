def mac_consecutive_ones(zeros_ones: list) -> int:
    count = 0
    m = 0

    for i in zeros_ones:
        if i == 1:
            count += 1
            m = max(count, m)
        else:
            count = 0

    return m


if __name__ == '__main__':
    ls = [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1]
    print(mac_consecutive_ones(ls))
