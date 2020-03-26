# imports as needed

def ganze_zahl(n):
    return isinstance(n, int)

def natuerliche_zahl(n):
    return isinstance(n, int) and n >= 0

def main():
    print(natuerliche_zahl(12))
    print(natuerliche_zahl(-12))
    print(ganze_zahl(12))
    print(ganze_zahl(12.5))

if __name__ == '__main__':
    main()
