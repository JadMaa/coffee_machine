class CoffeMachine:
    water = 400
    milk = 540
    beans = 120
    disposable_cups = 9
    money = 550

    coffee_dict = {}

    coffee_dict['1'] = {}
    coffee_dict['1']['water_needed'] = 250
    coffee_dict['1']['milk_needed'] = 0
    coffee_dict['1']['beans_needed'] = 16

    coffee_dict['2'] = {}
    coffee_dict['2']['water_needed'] = 350
    coffee_dict['2']['milk_needed'] = 75
    coffee_dict['2']['beans_needed'] = 20

    coffee_dict['3'] = {}
    coffee_dict['3']['water_needed'] = 200
    coffee_dict['3']['milk_needed'] = 100
    coffee_dict['3']['beans_needed'] = 12

    def do_action(self, action):
        if action == "fill":
            self.fill()
        elif action == "buy":
            self.buy()
        elif action == "take":
            self.take()
        elif action == "remaining":
            self.print_status()

    def print_status(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.beans) + " of coffee beans")
        print(str(self.disposable_cups) + " of disposable cups")
        print(str(self.money) + " of money")
        print()

    def fill(self):
        print("Write how many ml of water do you want to add:")
        water_to_add = abs(int(input()))
        self.water += water_to_add
        print("Write how many ml of milk do you want to add:")
        milk_to_add = abs(int(input()))
        self.milk += milk_to_add
        print("Write how many grams of coffee beans do you want to add:")
        beans_to_add = abs(int(input()))
        self.beans += beans_to_add
        print("Write how many disposable cups of coffee do you want to add:")
        disposable_cups_to_add = abs(int(input()))
        self.disposable_cups += disposable_cups_to_add

    def check_resources(self, coffee_to_buy):
        if self.water < self.coffee_dict[coffee_to_buy]['water_needed']:
            return "Sorry, not enough water!"
        if self.milk < self.coffee_dict[coffee_to_buy]['milk_needed']:
            return "Sorry, not enough milk!"
        if self.beans < self.coffee_dict[coffee_to_buy]['beans_needed']:
            return "Sorry, not enough beans!"

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee_to_buy = input()
        if coffee_to_buy != 'back':
            not_enough_resource_msg = self.check_resources(coffee_to_buy)
            if not not_enough_resource_msg:
                print("I have enough resources, making you a coffee!")
                print()
                if coffee_to_buy == "1":
                    self.water -= 250
                    self.beans -= 16
                    self.money += 4
                elif coffee_to_buy == "2":
                    self.water -= 350
                    self.milk -= 75
                    self.beans -= 20
                    self.money += 7
                elif coffee_to_buy == "3":
                    self.water -= 200
                    self.milk -= 100
                    self.beans -= 12
                    self.money += 6
                self.disposable_cups -= 1
            else:
                print(not_enough_resource_msg)

    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0


coffee_machine = CoffeMachine()
action = ''
while action != "exit":
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    coffee_machine.do_action(action)
