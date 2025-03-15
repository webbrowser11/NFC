# division numeric computer
Input = int(input("Enter a number: "))

def inputcell(layer, input):
    global Dump1, Dump2
    Dump1 = input / layer
    Dump2 = input / layer

def CompOut():
    Out = Dump1 % 1 + Dump2 % 1
    print(Out)
    print(f"Dump {Dump1 - Dump1 % 1+Dump2 - Dump2 % 1}")
    if Out == 1.0:
        print("Even.")

inputcell(2, Input)
CompOut()
