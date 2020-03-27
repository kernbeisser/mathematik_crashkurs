# imports as needed

def vereinigungs_menge():
    M1 = {1,2,3}
    N1 = {4, 5}

    return M1.union(N1)

def main():
    vm = vereinigungs_menge()
    print(f"{vm}")

if __name__ == '__main__':
    main()
