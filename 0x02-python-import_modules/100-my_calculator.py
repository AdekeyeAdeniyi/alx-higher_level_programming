#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arg = len(sys.argv) - 1
    if num_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

    op = sys.argv[2]
    if op != "+" and op != "-" and op != "/" and op != "*":
        print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result

    if op == "+":
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    if op == "-":
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
    if op == "*":
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
    if op == "/":
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
