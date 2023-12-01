#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    fnames = dir(hidden_4)
    for fname in fnames:
        if fname[:2] != "__":
            print(fname)
