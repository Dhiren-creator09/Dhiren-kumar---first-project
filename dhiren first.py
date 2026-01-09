#print("finally")
# My blood report measures:
report = float(input("enter your blood report:"))
if report >= 80:
    print("you are ok")
elif report >= 75:
    print("normal")
elif report <= 45:
    print("you are in danger")
else:
    print("you^re report seems normal")    