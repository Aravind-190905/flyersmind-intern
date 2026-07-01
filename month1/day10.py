print("welcome to contacts !!")

dic={}
while(True):
    print("""tell us what u wanna do from the following:
      /add,/view,/update/delete or enter -1 to exit """)
    s=input("give us here : ")

    match s :
        case "/add":
            print("u have chosen to add give us the contact number: ")
            n=input("give us the name :")
            d=input("give us the number :")
            def add(dic):
                dic[n]=d
            add(dic)

        case "/view":
           
            def show(dic):
                for i in dic:
                    print(f"{i} and contact is {dic[i]}\n")
                print("""these are all the contacts """)
            show(dic)

        case "/update":
            ch=input("tell us if u wanna update name or number: ")            
            if ch == "number":
                a,b=input("give us the name u wanna change and the number u want :").split()
                def update(dic,a,b):
                    for i in dic:
                        if a is i:
                            dic[i]=b
                        else:
                            print("no contact with that name !")
                update(dic,a,b)
            elif ch == "name":
                a,b=input("give me the name u wanna update and give us the name u wanna replace with : ").split()
                def updatename(dic,a):
                    for i in dict:
                        if a is i:
                            num=dic[a]
                            dic.pop(a)
                            dic[b]=num
                updatename(dic,a,b)

        case "/delete":
            a=input("tell us the name u wanna delete :")
            def delete(a,dic):
                dic.pop(a)
            delete(a,dic)
        case "-1":
            break
