# imports as needed

def uebungen():
    A = {0,1,2,3,4,5,6}
    B = {2,6,8}
    C = {'a', 'b', 'c', 'd', 'e'}
    D = {'a','c','d'}
    E = {(1, 'a'), (2, 'b'), (3, 'c')}
    F = {(1, 'a'), (3, 'c'), (4, 'd'), (6, 'f')}

    print(A.union(B))
    print(A.intersection(B))
    print(A.difference(B))

    print(C.union(D))
    print(C.intersection(D))
    print(C.difference(D))

    print(E.union(F))
    print(E.intersection(F))
    print(E.difference(F))

def main():
    uebungen()

if __name__ == '__main__':
    main()
