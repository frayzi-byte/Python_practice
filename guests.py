guests = []

class Guest:
    def __init__(self, name: str):
        self.name = name
        self.id_g = len(guests) + 1

def add_guest():
    while True:
        add = input("Do you want to add a new guest? (yes/no): ").lower()

        match add:
            case "yes":
                name = input("Guest name: ")
                new_guest = Guest(name)
                guests.append(new_guest)
                print(f"Guest {name} added with id {new_guest.id_g}")
            case "no":
                break
            case _:
                print("Please type yes or no")

add_guest()
