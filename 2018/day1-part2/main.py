

freq = 0
old = [freq]
found = False

while not found: 
    with open('freq.txt', 'r') as f:
        for i in f:
            freq += int(i)
            if freq in old:
                print(freq)
                found = True
                break
            old.append(freq)
