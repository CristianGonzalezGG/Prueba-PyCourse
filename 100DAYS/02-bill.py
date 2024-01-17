#Data types
#booleans = True
#floats = 3.14156
#exercise1 = input("Number to split for add: ")
#exercise1 = int(exercise1)

#digit1 = int(str(exercise1)[0])
#digit2 = int(str(exercise1)[1])

#add_result = digit1 + digit2

#print(f"The add of the number {exercise1} split - Digit 1: {digit1} Digit 2: {digit2} The add was: {add_result}")

#Create a method in where u can split the bill.
print("Welcome to the tip Calculator")
bill = float(input("What was the total Bill.?\n"))
percentage = int(input("What percentage tip would u like to give..?: 10, 12, or 15\n"))
people = int(input("How many people to plit the bill..\n"))

while True:
    if percentage == 10:
        mul = bill * percentage
        resl = mul / 100
        redounded = round(resl,2)
        print(f"Percentaje to pay: {resl}\n TOTAL: {(resl+bill)}")
        break
    elif percentage == 12:
        mul = bill * percentage
        resl = mul / 100
        redounded = round(resl,2)
        print(f"Percentaje to pay: {resl}\n TOTAL: {(resl+bill)}")
        break
    elif percentage == 15:
        mul = bill * percentage
        resl = mul / 100
        redounded = round(resl,2)
        print(f"Percentaje to pay: {resl}\n TOTAL: {(resl+bill)}")
        break
    else:
        print("no")
        break
newBill = (resl + bill) / people
print(f"The Bill for Person is: {newBill}")