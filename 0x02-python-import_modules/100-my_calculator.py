#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if operator == '+':
        sum = add(a, b)
    elif operator == '-':
        sum = sub(a, b)
    elif operator == '*':
        sum = mul(a, b)
    elif operator == '/':
        sum = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, sum))
