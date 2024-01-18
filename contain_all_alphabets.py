def contain_all_alphabets(s):
    d = {}
    print(ord("a")-ord("z"))
    for i in s:
        if 96 < ord(i) < 123:
            d[ord(i)] = 1
            print(ord(i), "--", i)
    print(len(d))


if __name__ == '__main__':
    s = ("By 1st January 2027, I will have joyfully established my own MNC, and every morning, I will zealously wake "
         "up with excitement.")

    contain_all_alphabets(s.lower())
