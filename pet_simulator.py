class Pet:
    def __init__(self, name, animal_type, hunger, happiness):
        self.name = name.capitalize()
        self.animal_type = animal_type
        self.hunger = hunger
        self.happiness = happiness

    def eat(self):
        if self.hunger == 100:
            print(f"\033[33m\n{self.name} is full. Hunger is at 100.\033[0m")
        elif (self.hunger - 10) <= 0:
            print(
                f"\033[33m\n{self.name} has died from starvation. His hunger reached 0.\033[0m"
            )
        else:
            self.hunger = self.hunger - 10
            print(
                f"\033[33m\n{self.name} has eaten. Hunger is now at {self.hunger}.\033[0m"
            )

    def play(self):
        if self.happiness == 100:
            print(f"\033[33m\n{self.name} is already at max happiness!\033[0m")
            self.hunger += 5
        elif self.happiness >= 90:
            self.happiness = 100
            self.hunger += 5
        else:
            self.happiness += 10
            self.hunger += 5
        print(
            f"\033[33m\n{self.name} has played and is happier! Happiness is now at {self.happiness} and hunger is at {self.hunger}\033[0m"
        )

    def status(self):
        print(
            f"\033[33m\n--- {self.name}'s Status ---\nType: {self.animal_type}\nHunger: {self.hunger}\nHappiness: {self.happiness}\033[0m"
        )

    def print_name(self):
        return self.name


pets = []


def create_pet():
    print("\033[31m=====================================\033[0m")
    input_name = input("Enter the pet's name: ")
    input_type = input("Enter the pet's animal type: ")
    input_hunger = int(input("Enter the pet's hunger level(0 - 100): "))
    input_happiness = int(input("Enter the pet's happiness level(0 - 100): "))
    temp = Pet(input_name, input_type, input_hunger, input_happiness)
    pets.append(temp)


def choose_pet():
    print("Choose a pet:")
    for i, pet in enumerate(pets):
        print(f"\t{i + 1}. {pet.print_name()}")
    try:
        choice = int(input("Enter the number of the pet: ")) - 1
        if 0 <= choice < len(pets):
            return pets[choice]
        else:
            print("Invalid choice")
    except ValueError:
        print("Enter a number")


num_pets = int(input("Enter the number of pets you would like to create: "))
for i in range(num_pets):
    create_pet()


while True:
    print("\033[31m\n******************************************\033[0m")
    task = input(
        f"1. Feed Pet\n2. Play with a pet\n3. Check a pet's status\n4. Exit\nPlease select the task you would like to perform: "
    )
    if task == "1":
        chosen = choose_pet()
        chosen.eat()
    elif task == "2":
        chosen = choose_pet()
        chosen.play()
    elif task == "3":
        chosen = choose_pet()
        chosen.status()
    elif task == "4":
        print("\033[33m\nYou have exited the program.\033[0m")
        break
    else:
        print("Invalid choice")
