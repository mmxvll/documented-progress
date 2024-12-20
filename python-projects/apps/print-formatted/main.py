def print_formatted(number):
    for i in range(1, number+1):
        print("{:2d} {:>8o} {:>8X} {:>8b}".format(i, i, i, i))

n = int(input())
print_formatted(n)

