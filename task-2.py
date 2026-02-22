import random 
random_num=random.randint(1,100)
count=0
while True:
    gusses_num=int(input("Enter  the gussed number:"))
    count+=1
    if gusses_num>random_num:
        print("The gussed number is Too High")
        
    elif gusses_num<random_num:
        print("The gussed number is Too Low")
        
    else:
        print("correct gusses")
        print("Number of attemptes:",count)
        break
