#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
dirlist = dir(hidden_4)
for i in range(len(dirlist)):
    if dirlist[i][0:2] != '__':
        print("{}".format((dirlist[i]))

