Name = "Artyom"
Doing_Now = "Learning python"

what_is = input(f"What is {Name} doing now?\n").lower()

match what_is:
    case "learning python":
        print(f"{Name} is {Doing_Now} now")
    case _:
        print(f"Sorry, I need to know\nWhat is {Name} doing now")