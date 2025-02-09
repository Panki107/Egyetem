from sys import argv

def apply_mult():
    return [round(int(x)*float(argv[1]),3)for x in argv[2:]]

def main():
    print(";".join([str(x) for x in apply_mult()]))

if __name__ == '__main__':
    main()