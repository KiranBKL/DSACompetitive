def toh(n,a,b,c):
    if(n==1):
        print(f"Move 1 from {a} to {c}")
        return
    toh(n-1,a,c,b)
    print(f"Move {n} from {a} to {c}")
    toh(n-1,b,a,c)
toh(3,"a","b","c")