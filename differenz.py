# imports as needed

def differenz():
    M1 = {1,2,3}
    N1 = {4, 5}

    diff1 = M1.difference(N1)
    diff2 = N1.difference(M1)

    return diff1, diff2

def main():
     d1, d2 = differenz()
     print(f"{d1}, {d2}")

if __name__ == '__main__':
    main()
