if __name__ == '__main__':
    ls = [1, 2, 6, 5, 0, 10]

    large_num = 0
    sec_large_num = 0
    if len(ls) > 0:
        for i in range(len(ls) // 2 + 1):
            # print(ls[i])
            # print(ls[len(ls) - i - 1])
            if ls[i] > large_num:
                sec_large_num = large_num
                large_num = ls[i]
            elif ls[i] > sec_large_num:
                sec_large_num = ls[i]
            if ls[len(ls) - i - 1] > large_num:
                sec_large_num = large_num
                large_num = ls[len(ls) - i - 1]
            elif ls[len(ls) - i - 1] > sec_large_num:
                sec_large_num = ls[len(ls) - i - 1]

        print(f"large->{large_num}")
        print(f"sec_large->{sec_large_num}")

# if __name__ == '__main__':
#     uq = "UNIQUAL"
#
#     for i in range(len(uq)):
#         for j in range(len(uq)):
#             if i == 0:
#                 print(uq[j], end=' ')
#             elif i == len(uq) - 1:
#                 print(uq[len(uq) - j - 1], end=' ')
#             elif j == 0:
#                 print(uq[i], end=' ')
#             elif j == len(uq) - 1:
#                 print(uq[len(uq) - i - 1], end=' ')
#             else:
#                 print("  ", end='')
#         print('')
