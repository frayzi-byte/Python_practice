favorite_fruit = "Apple"
q = input("What is your favourite fruit?").lower()
match q:
    case "apple":
        print(f"Correct! {favorite_fruit} is the favorite fruit!")
    case _:
        print("Not correct! Try again")