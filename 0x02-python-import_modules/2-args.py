#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc < 2:
        print("{} argument:\n".format(argc -1))
    if argc == 1:
        print("0 arguments.\n")
    else:
        for i in range(1, argc):
            print("{} argument:\n".format(argc -1))
