a=int(input("Enter a number"))
mc=str(input("Enter your medcal cause"))
if mc == "Y" :
    print("you are allowed")
else :
    if a >= 75 :
        print("allowed")
    else :
        print("not allowed")    