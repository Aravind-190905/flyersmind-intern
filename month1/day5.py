def calc():
    exit=False
    while(exit == False):
        print("chose the operators :")
        print("enter + to add :")
        print("enter - to sub :")
        print("enter * to mul :")
        print("enter / to div :")
        try:
            op=(input("chose the operator :"))
        except ValueError:
            print("give me only numbers")
        try:
            operand1=int(input("choose the operand1 :"))
            operand2=int(input("choose the operand2 :"))
        except ValueError:
            print("give me numbers only no strings")   
            continue
            ans=0
        match op:
            case "+":
                ans=operand2+operand1+ans
            case "*":
                ans=ans+operand1*operand2
            case "/":
                ans=ans+operand1/operand2
            case "-":
                ans=ans+operand1-operand2
        try:
            val=bool(input("do u wish to exit  :"))
        except ValueError:
            print("give me string wanna start again pls press enter")
        exit=val
    return ans

c=calc()
print(f"{c} is the answer of ur calc :")
