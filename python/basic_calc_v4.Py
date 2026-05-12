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
    add = n1 + n2
    print(f"addition is: {add}")
else:
    if (opt == 2):
     subs = n1 - n2
     print(f"Subtraction is:  {subs}")
    else:
       if (opt == 3):
        mult = n1 * n2
    print(f"Multiplication is:  {mult}") 
        else:
          if (opt == 4):
        mult = n1 / n2
         print(f"Multiplication is:  {add}") 
    

