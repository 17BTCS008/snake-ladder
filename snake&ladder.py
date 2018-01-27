import random
count=0
while (count<=100):
    a=input("Enter 'r' to roll the dice:r")
    if (a=='r'):
        r=random.randint(1,6)
        count=count+r
        print("dice value=")
        print(r)
        print("count value=")
        print(count)
        
    if(count==8):
        count=37
        print ("Wow you climbed the ladder")
    elif(count==11):
        count=2
        print("snake&ladder.py bitten you")
    elif(count==13):
        count=34
        print("wow you have climbed the ladder")
    elif(count==25):
        count=4
        print("snake has bitten you")
    elif(count==38):
        count=9
    elif(count==40):
        count=68
        print("you rock")
    elif(count==52):
        count=81
        print("you rock")
    elif(count==65):
        count=46
        print("you were bitten")
    elif(count==76):
        count=97
        print("you rock")
    elif(count==89):
        count=70
        print("you were bitten")
    elif(count==93):
        count=64
        print("you were bitten")
    else:
        if count==100:
            print("you have won")
        
        
        
        
