import os

# Main menu fundtiom
def main_menu():
    print("#### MAIN MENU ####")
    print("[1]. Addition")
    print("[2]. Subtraction")
    print("[3]. Multiplication")
    print("[4]. Division")
    print("[5]. Average")
    print("[6]. All operations")

os. system('clear')
# Inputs
n1 = float(input("Emterfirst number: "))
n2 = float(input("Enter second number:"))
main_menu
opt = int(input("Enter any option: "))

if(opt == 1):
    add

elif (opt == 2):
        subs = n1 - n2
        print(f"substraction is:  {subs}")
elif (opt == 3):
     mult = n1 * n2
     print(f"Multiplication is:  {mult}")
elif (opt == 4):
        div = n1 / n2
        print(f"Division is: {div}")
