#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    tot = 0
    for i in range(len(sys.argv[1:])):
        tot += int(sys.argv[i + 1])
    print("{}".format(tot))
