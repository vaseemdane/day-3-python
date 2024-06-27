# DAY_3 PROJECT TRESURER ISLAND PROJECT
print("Welcome to Treasurer Island. your mission is to find treasurer.")
choose=input("you are at  a cross road where do you want to go left or right")
if choose=="left":
    print("you come to lake. There is an island middle of the lake")
else:
    print("game over!!")
    exit()
choose1=input("do you want to swim or wait here")
if choose1=="swim":
    print("game over!!")
    exit()
else:
    print("you arrived in the island unharmed.")
choose2=input("there is a house with 3 doors of colors red,blue,yellow.which door are you choosing")
if choose2=="yellow":
    print("you win")
else:
    print("game over!!!")
    exit()