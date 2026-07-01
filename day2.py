try:
    a=int(input("give me the number : "))
    b=int(input("give me another number: "))
    c=input("operation u want to do")
    match c:
        case "*":
            print(f"{a+b} is the sum")
        case "+":
            print(f"{a*b} is the product")
        case "/":
            if b == 0:
                print("the denominator cant be zero")    
            print(f"{a/b} is the divison")
        
        case "%":
            print(f"{a%b} is the remainder")
        case "^":
            print(f"{a**b} is the power")
        
except ValueError:
   print("give me valid inputs")


