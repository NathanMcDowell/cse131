def function_1(x):
    return x + 20
    
def function_2(x):
    return x + function_1(x)

def function_3(x):
    return x + function_2(x)

def function_4(x):
    return x + function_3(x)

def main():
    x = 100
    total = function_4(x)
    print(total)

main()