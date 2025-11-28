#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    argv = sys.argv
    for i in range(1, len(argv)):
        total += int(argv[i])
    print(total)
