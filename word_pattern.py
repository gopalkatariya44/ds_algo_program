def wordPattern(p: str, s: str) -> bool:
    words, w_to_p = s.split(' '), dict()

    if len(p) != len(words): return False
    if len(set(p)) != len(set(words)): return False  # for the case w = ['dog', 'cat'] and p = 'aa'

    for i in range(len(words)):
        if words[i] not in w_to_p:
            w_to_p[words[i]] = p[i]
        elif w_to_p[words[i]] != p[i]:
            return False
    print(words)
    print(w_to_p)
    return True


if __name__ == '__main__':
    print(wordPattern("appa", "dog cat cat dog"))
    print(wordPattern("ap", "dog cat"))
    print(wordPattern("apc", "dog cat"))
