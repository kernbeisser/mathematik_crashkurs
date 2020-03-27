# imports as needed

def schnitt_menge():
    M1 = {1, 2, 3}
    N1 = {1, 2, 4, 5}
    return M1.intersection(N1)

def main():
    im = schnitt_menge()
    print(f"{im}")

if __name__ == '__main__':
    main()
