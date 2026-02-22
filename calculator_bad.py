# this is the calculator program

def doStuff():
    print("Calculator")
    print("1 add")
    print("2 subtract")
    print("3 multiply")
    print("4 divide")
    c = input("Choose: ")

    if c == "1":
        x = input("num1: ")
        y = input("num2: ")
        if x.isdigit() and y.isdigit():
            print("Result is " + str(int(x) + int(y)))
        else:
            print("bad input")

    elif c == "2":
        x = input("num1: ")
        y = input("num2: ")
        if x.isdigit() and y.isdigit():
            print("Result is " + str(int(x) - int(y)))
        else:
            print("bad input")

    elif c == "3":
        x = input("num1: ")
        y = input("num2: ")
        if x.isdigit() and y.isdigit():
            print("Result is " + str(int(x) * int(y)))
        else:
            print("bad input")

    elif c == "4":
        x = input("num1: ")
        y = input("num2: ")
        if x.isdigit() and y.isdigit():
            if int(y) != 0:
                print("Result is " + str(int(x) / int(y)))
            else:
                print("can't divide")
        else:
            print("bad input")

    else:
        print("wrong choice")

def run():
    doStuff()

def start():
    run()

start()