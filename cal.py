while True:
    try:
        print(eval(input("Enter the numbers: ")))
    except Exception as e:
        print("Enter a valid input",e)