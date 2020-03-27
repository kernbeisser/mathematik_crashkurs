# imports as needed

def potenz_menge():
    M1 = (1,2,3)
    Mp = [(),(M1),(1),(2),(3),(1,2),(1,3),(2,3)]
    Mp_set = set(Mp)

    return Mp_set

def main():
    mp = potenz_menge()
    print(f"{mp}")

    mag_mp = len(mp)
    print(f"{mag_mp}")

if __name__ == '__main__':
    main()
