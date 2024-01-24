def heating_cooling(des, act):
    if des>act:
        print("Raise the heat!")
    elif des < act:
        print("Run the A/C!")
    else:
        print("Standby")

des_temp = input("enter desired temp ")
act_temp = input("enter actual temp ")
heating_cooling(des_temp, act_temp)
print()
def convert_temp(temp_celsius, target_unit):
    int(temp_celsius)
    if target_unit == "k":
        kel=temp_celsius + 273.15
        print(f"kelvin value is: {kel}")
    elif target_unit == "c":
        print("value unchanged")
    elif target_unit == "f":
        print((temp_celsius*1.8)+32)
    # match target_unit:
    #     case "k":
    #         kel=temp_celsius + 273.15
    #         print(kel)
    #     case "c":
    #         print("value unchanged")
    #     case "f":
    #         print((temp_celsius * 1.8) + 32)

cel = int(input("enter the celsius value "))
convert = input("convert celsius to which value c/f/k ".lower())
convert_temp(cel,convert)
