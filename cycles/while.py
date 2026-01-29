amount = int(input("How much?"))
if amount<100:
    print("Number needs to be more than 100")
else:
    while amount<1000000:
        amount += 1000
        print(amount)