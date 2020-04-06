# https://github.com/michaelkrisper
# Compute the Powerset of a list
# items = [1, 2]
# powerset = [[], [1], [2], [1, 2]]

import itertools

def create_powerset_from_set(SET):
    powerset = [x for length in range(len(SET)+1) for x in itertools.combinations(SET, length)]

    return powerset

def main():
    C = {'a', 'b', 'c', 'd', 'e'}
    ps = create_powerset_from_set(C)
    print(f"{ps}")
    print(f"{len(ps)}")

if __name__ == '__main__':
    main()
