#Define a function named heating_cooling that takes in 2 parameters: actual_temp and a desired_temp.
#Print one of these three things: Run A/C, Run heat, or Standby depending on input.
def heating_cooling(des, act):
    print(f"desired temp is {des}, actual temp is {act}" )
    if des>act:
        print("Raise the heat!")
        print()
    elif des < act:
        print("Run the A/C!")
        print()
    else:
        print("Standby")
        print()

des_temp = input("enter desired temp ")
act_temp = input("enter actual temp ")
heating_cooling(des_temp, act_temp)
heating_cooling(22, 50)
print()
"""
Define a function named convert_temp with 2 parameters: temp_celsius (a number)
and target_unit (a string, either “C”, “F”, or “K”).
Write a switch statement that checks the target_unit and returns the temperature converted to that unit.
Notes: K stands for Kelvin. C requires no conversion, return the original temp.

"""

def convert_temp(temp_celsius, target_unit):
    target_unit=target_unit.upper()
    int(temp_celsius)
    if target_unit == "K":
        kel=temp_celsius + 273.15
        print(f"kelvin value is: {kel}")
    elif target_unit == "C":
        print("value unchanged")
    elif target_unit == "F":
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
convert = input("convert celsius to which value C/F/K ")
convert_temp(cel,convert)
