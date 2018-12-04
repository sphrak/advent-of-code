#!/usr/bin/env python3


with open('data.txt', 'r') as f:

    pkgs = [pkg.strip() for pkg in f]

    for x in pkgs:
        for y in pkgs:
            diff = 0
            matched = ''
            for idx, char in enumerate(x):
                if char == y[idx]:
                    matched += char
                else:
                    diff += 1
            if diff == 1:
                print(f"Answer: {matched}")
