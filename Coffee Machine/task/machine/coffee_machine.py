on_watter = 400
on_milk = 540
on_cofben = 120
on_cups = 9
on_money = 550

def remain():
    global on_cofben,on_milk,on_watter,on_cups,on_money
    print(f"""The coffee machine has:
{on_watter} of water
{on_milk} of milk
{on_cofben} of coffee beans
{on_cups} of disposable cups
{on_money} of money""")
    
def buy():
    global on_cofben, on_milk, on_watter, on_cups, on_money
    coffe_type = str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"))
    if coffe_type == "1":
        if on_watter < 250:
            print("Sorry, not enough water!")
        elif on_cofben < 16:
            print("Sorry, not enough coffee bean!")
        elif on_cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            on_watter = on_watter - 250
            on_cofben = on_cofben - 16
            on_money = on_money + 4
            on_cups -= 1
            print("I have enough resources, making you a coffee!")
    elif coffe_type == "2":
        if on_watter < 350:
            print("Sorry, not enough water!")
        elif on_cofben < 20:
            print("Sorry, not enough coffee bean!")
        elif on_milk < 75:
            print("Sorry, not enough milk!")
        elif on_cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            on_watter = on_watter - 350
            on_milk = on_milk - 75
            on_cofben = on_cofben - 20
            on_money = on_money + 7
            on_cups -= 1
            print("I have enough resources, making you a coffee!")
    elif coffe_type == "3":
        if on_watter < 200:
            print("Sorry, not enough water!")
        elif on_cofben < 12:
            print("Sorry, not enough coffee bean!")
        elif on_milk < 100:
            print("Sorry, not enough milk!")
        elif on_cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            on_watter = on_watter - 200
            on_milk = on_milk - 100
            on_cofben = on_cofben - 12
            on_money = on_money + 6
            on_cups -= 1
            print("I have enough resources, making you a coffee!")
    elif coffe_type == "back":
        return


def fill():
    global on_cofben, on_milk, on_watter, on_cups, on_money
    ad_water = int(input("Write how many ml of water do you want to add:"))
    on_watter += ad_water
    ad_milk = int(input("Write how many ml of milk do you want to add:"))
    on_milk += ad_milk
    ad_cofben = int(input("Write how many grams of coffee beans do you want to add:"))
    on_cofben += ad_cofben
    ad_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
    on_cups += ad_cups


def take():
    global on_money
    print(f"I gave you ${on_money}")
    on_money = 0


    
def action_selection():
    while True:
        wish = str(input("Write action (buy, fill, take, remaining, exit):"))
        if wish == "buy":
            buy()
        elif wish == "fill":
            fill()
        elif wish == "take":
            take()
        elif wish == "remaining":
            remain()
        elif wish == "exit":
            break



action_selection()