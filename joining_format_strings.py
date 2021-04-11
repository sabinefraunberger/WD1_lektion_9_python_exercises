str_one = "Happy"
str_two = "Day"

print(str_one + str_two)

print(str_one + " " + str_two)

print("%s %s" % (str_one, str_two))

print("{0} {1}".format(str_one, str_two))

print("{first} {second_str}".format(first=str_one, second_str=str_two))

print(f"{str_one} {str_two}")


# Practice

errno = 50159747054
name = "Bob"

# % Operator - 'old style'
print("Hello, %s" % name)

print("%x" % errno)     # %x --> konvertiert int Wert in hexadezimal

print("Hey %s, there is a 0x%x error!" % (name, errno))  # Tupel bei mehreren Argumenten

print("Hey %(name)s, there is a 0x%(errno)x error!" % {"name": name, "errno": errno})


# str.format() - 'new style'
print("Hello, {}".format(name))     # Positionsformatierung

print("Hey {name}, there is a 0x{errno:x} error!".format(name=name, errno=errno))
