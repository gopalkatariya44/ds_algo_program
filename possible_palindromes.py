def possible_palindromes(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1


if __name__ == '__main__':
    s = 'maallmaay'
    possible_palindromes(s)
