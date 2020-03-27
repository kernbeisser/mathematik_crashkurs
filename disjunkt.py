# imports as needed

def disjunkt():
    M1 = {1,2,3}
    N1 = {4,5}

    # a) use isdisjoint
    ist_disjunkt = M1.isdisjoint(N1)

    # b) test intersection if empty
    s = M1.intersection(N1)
    ist_leer = len(s) == 0

    return ist_disjunkt, ist_leer

def main():
    disj, leer = disjunkt()
    print(f"{disj}, {leer}")

if __name__ == '__main__':
    main()
