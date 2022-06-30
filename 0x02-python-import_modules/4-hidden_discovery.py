#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    namez = dir(hidden_4)
    for name in namez:
        if name.startswith("__") is False:
            print("{}".format(name))
