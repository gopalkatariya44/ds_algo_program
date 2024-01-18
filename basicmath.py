def main():
    n = int(input("enter digit: "))

    dummy = n
    rev = 0

    while dummy > 0:
        last = dummy % 10
        rev = (rev * 10) + last
        dummy = int(dummy / 10)
    print(n, rev)
    if n == rev:
        print("is palindrome")
    else:
        print("not palindrome")


if __name__ == '__main__':
    main()
