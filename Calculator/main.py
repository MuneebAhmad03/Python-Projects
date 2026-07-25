try:
    a = int(input("Enter the first Number: "))
    b = int(input("Enter the second number: "))

    o = input("Enter the Operation you want to perfom : \n+ for addition\n- for  subtraction\n/ for divison\n* for multiplication\n")

    match o:
        case "+":
            print(f"Addition of the above numbers are {a+b}")
        case "-":
            print(f"Subtraction of the above numbers are {a-b}")
        case "*":
            print(f"Multiplication of the above numbers are {a*b}")
        case "/":
            print(f"Divison of the above numbers are {a/b}")
        case default:
            print("Error Occur while performing operation")

except Exception as e:
    print("There is a error enter the right numbers ")


