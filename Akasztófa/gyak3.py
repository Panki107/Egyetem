def sum(n: int):
    if n == 4:
        return 8
    else:
        return (n**2 - 2*n) + sum(n-1)
def main():
    n = int(input())
    lista = []
    while n >= 0:
        lista.append(sum(n))
        n = int(input())
    print(*lista, sep=' ')
if __name__ == '__main__':
    main()