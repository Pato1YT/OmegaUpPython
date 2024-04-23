n = input()
n = int(n)

numbers = ' '.join(str(i) for i in range(1, n + 1))
print(numbers)

numbers = ' '.join(str(i) for i in range(n, 0, -1))
print(numbers)


