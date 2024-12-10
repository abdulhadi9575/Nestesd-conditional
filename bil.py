unit=int(input("Enter your Unit"))
if unit < 50 :
    amount= unit*2.60
    tax=25
elif unit <= 100 :
    amount=130+((unit-50)*3.25)
    tax=35
else :
    amount=130+162.50+((unit-100)*5.26)
    tax=35
total=amount+tax
print(total)    