name = "Artyom"
age = "14"
what_age = input(f"How old is {name}?")
match what_age:
    case "14":
        print(f"Correct! {name} is 14!")
    case _:
        print("Incorrect! Try again")