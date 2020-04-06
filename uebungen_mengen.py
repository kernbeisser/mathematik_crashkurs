# imports as needed

def uebungen():
    A = {0,1,2,3,4,5,6}
    B = {2,6,8}
    C = {'a', 'b', 'c', 'd', 'e'}
    D = {'a','c','d'}
    E = {(1, 'a'), (2, 'b'), (3, 'c')}
    F = {(1, 'a'), (3, 'c'), (4, 'd'), (6, 'f')}
    O = {(3, 'c'), 'c', 8, 2, (4, 'd'), 'b', (0, 'a'), 6, 'a', (1, 'a'), 'd', (6, 'f'), (5, 5)}

    Cp = {(), ('b',), ('a',), ('c',), ('e',), ('d',), ('b', 'a'), ('b', 'c'), ('b', 'e'), ('b', 'd'), ('a', 'c'), ('a', 'e'), ('a', 'd'), ('c', 'e'), ('c', 'd'), ('e', 'd'), ('b', 'a', 'c'), ('b', 'a', 'e'), ('b', 'a', 'd'), ('b', 'c', 'e'), ('b', 'c', 'd'), ('b', 'e', 'd'), ('a', 'c', 'e'), ('a', 'c', 'd'), ('a', 'e', 'd'), ('c', 'e', 'd'), ('b', 'a', 'c', 'e'), ('b', 'a', 'c', 'd'), ('b', 'a', 'e', 'd'), ('b', 'c', 'e', 'd'), ('a', 'c', 'e', 'd'), ('b', 'a', 'c', 'e', 'd')}

    print(A.union(B))
    print(A.intersection(B))
    print(A.difference(B))

    print()
    print(C.union(D))
    print(C.intersection(D))
    print(C.difference(D))

    print()
    print(E.union(F))
    print(E.intersection(F))
    print(E.difference(F))

    print()
    print(A.union(Cp))
    print(A.intersection(Cp))
    print(A.difference(Cp))

    print()
    print(A == A.intersection(O))
    print(B == B.intersection(O))
    print(C == C.intersection(O))
    print(D == D.intersection(O))
    print(E == E.intersection(O))
    print(F == F.intersection(O))

    print()
    print(A == A.intersection(Cp))
    print(B == B.intersection(Cp))
    print(C == C.intersection(Cp))
    print(D == D.intersection(Cp))
    print(E == E.intersection(Cp))
    print(F == F.intersection(Cp))

def main():
    uebungen()

if __name__ == '__main__':
    main()
