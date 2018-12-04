#!/usr/bin/env python3

data = [0, 0]

with open('data.txt', 'r') as f:
    for line in f:

        has_two = False
        has_three = False
    
        for char in line.strip():
            if not has_two and line.count(char) == 2:
                data[0] += 1
                has_two = True
            if not has_three and line.count(char) == 3:
                data[1] += 1
                has_three = True
            if has_two and has_three:
                break
    print(data[0] * data[1])
