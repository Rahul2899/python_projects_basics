#roll  a die?
# If user says  y generate a random number
# if any other input -> issue a warning
#if  n -> terminate a loop



import random 

inp = 'y'

while(inp == 'y' or inp == 'Y'):
    num= random.randint(1,6)

    if(num==1):
        print("[     ]\n[   0  ]\n[     ]")

    if(num==2):
        print("[0    ]\n[     ]\n[     0]")

    if(num==3):
        print("[0    ]\n[   0  ]\n[     0]")

    if(num==4):
        print("[0    0]\n[     ]\n[0     0]")

    if(num==5):
        print("[0    0]\n[   0  ]\n[0     0]")

    if(num==6):
        print("[0    0]\n[0     0]\n[0     0]")


    inp = input("roll a die? y/n")

    if(inp not in ['Y','y','N','n']):
        print("Invalid input")

    else:
        continue

print("Thanks for playing ")