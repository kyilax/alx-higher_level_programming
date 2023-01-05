#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import calc
    a = 10
    b = 5
    print("{}".format(calc.add(a, b)))
    print("{}".format(calc.sub(a, b)))
    print("{}".format(calc.mul(a, b)))
    print("{}".format(calc.div(a, b)))
