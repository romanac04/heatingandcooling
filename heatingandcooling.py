actualTemp = 34
desiredTemp = 70
def cooling_system(actualTemp, desiredTemp):
    if actualTemp > desiredTemp:
        return ("Run A/C")
    elif actualTemp < desiredTemp:
        return ("Run heat")
    else:
        return ("Standby")
print(cooling_system(actualTemp, desiredTemp))

tempCelsius = 35
targetUnit = "F"

def temp_conversion(tempCelsius,targetUnit):
    if targetUnit == "C":
        convertedTemp = tempCelsius
    elif targetUnit == "F":
        convertedTemp = (tempCelsius -32) * 5/9
    elif targetUnit == "K":
        convertedTemp = tempCelsius + 273.15
    else:
        print("Invalid unit")

    return convertedTemp

print(temp_conversion(tempCelsius,targetUnit))
