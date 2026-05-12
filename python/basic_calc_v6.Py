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

match opt:
    case 1:
          add = n1 + n2
def       print(f"Addition is:  {add}") 
    case 2:
          subs = n1 - n2
          print(f"substracction is: {subs}")
