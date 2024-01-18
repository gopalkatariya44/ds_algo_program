n = int(input("enter digit: "))

for i in range(1, n+1):
    if n % i == 0:
        print(i)
