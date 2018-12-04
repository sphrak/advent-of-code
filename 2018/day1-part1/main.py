

with open('freq.txt', 'r') as f:

    r = []

    for i in f:
        r.append(int(i)) 
    n = sum(r)

    print(n)
