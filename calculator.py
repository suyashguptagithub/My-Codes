# make a calculator- 

def Calculation():
    def add(n1, n2):
        return n1 + n2
    def subtract(n1, n2):
        return n1 - n2
    def divide(n1, n2):
        return n1 / n2
    def multiply(n1, n2):
        return n1 * n2
    
    old_calc = True

    op = {
            "+":add,
            "-":subtract,
            "*":multiply,
            "/":divide
    }
    first = float(input("Type your number: "))
    while old_calc:
        for sign in op:
            print(sign)
        operation = str(input("Type your operation: "))
        second = float(input(f"To which num you want to {first} {operation}: "))


        answer = op[operation](first, second)
        print(f"{first} {operation} {second} = {answer}")

        choice = str(input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation. ")).lower()

        if choice == "y":
            first = answer
            
        else:
            old_calc = False
            print("\n" * 100)
            Calculation()  

Calculation()