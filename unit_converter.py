'''
The program greets user and describes what's the purpose of the program.
The program asks user to enter number of kilometers.
User enters the amount of kilometers.
The program converts these kilometers into miles and prints them.
The program asks user if s/he'd want to do another conversion.
If yes, repeat the above process (except the greeting).
If not, the program says goodbye and stops.
'''

price = 50451.28
print("Euro to Bitcoin converter")

while True:
    val_eur = float(input("Euro: ").replace(",", "."))
    val_bit = val_eur / price

    print("{0} Euro = {1} Bitcoin".format(val_eur, val_bit))

    cont = input("again? (y|n): ")
    if cont.upper() == "N":
        break

