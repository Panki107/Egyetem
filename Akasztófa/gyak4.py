from sys import argv


def apply_multiplication():
    x = [round(int(x)*float(argv[1]), 2) for x in argv[2:] if x % 2==0]
    return x

def main():
    print(";".join([str(x) for x in apply_multiplication() if x >= 0]))

if __name__ == "__main__":
    main()
