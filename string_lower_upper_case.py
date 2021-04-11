# make string lowercase / uppercase

input_str = "Today Is A BeautiFul DAY"
output_str = input_str.lower()
print(output_str)

input_str2 = "HELLO, yOu looK gOOD"
output_str2 = input_str2.lower()
print(output_str2)

input_str3 = "Be HAppy"
print(input_str3)
check = input_str3.islower()                # liefert bool
print("String is lowercase? ", check)
output_str3 = input_str3.lower()
print("Now the string is lowercase:", output_str3)

input_str4 = "Today Is A BeautiFul DAY"
output_str4 = input_str4.upper()
print(output_str4)

input_str5 = "HELLO, yOu looK gOOD"
output_str5 = input_str5.upper()
print(output_str5)

input_str6 = "Be HAppy"
print(input_str6)
check6 = input_str6.isupper()
print("String is uppercase? ", check6)
output_str6 = input_str6.upper()
print("Now the string is uppercase: ", output_str6)
