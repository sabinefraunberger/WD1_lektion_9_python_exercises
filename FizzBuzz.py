# Zahl einlesen zwischen 1-100
# Programmstart - zählen  - ausgeben:
#    kommt Zahl die durch 3 teilbar ist - ausgeben fizz
#    kommt Zahl die durch 5 teilbar ist - ausgeben buzz
#    teilbar durch 3 und 5 - ausgeben fizzbuzz
# !Achtung Reihenfolge --> Doppelbedingung an erster Stelle
# Ende bei eingelesener Zahl


print("Welcome to FizzBuzz!")

user_input = int(input("Select a number between 1 and 100: "))

for x in range(1, user_input+1):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 5 == 0:
        print("buzz")
    elif x % 3 == 0:
        print("fizz")
    else:
        print(x)
