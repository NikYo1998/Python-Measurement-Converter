#Program by Nicholas Young
#April 24, 2023
#Program to convert measurements

print("What type of conversion would you like to do? ")

#take user input as desired measurement conversion type
desMeas = input("Enter temp, mass, volume, or length: ")

#use nested if statements to separate input by measurement conversion type
if desMeas == "temp":
    #ask user what temp conversion they want to do
    desConv = input("Press 1 for K to C, 2 for C to K, 3 for K to F, 4 for F to K, 5 for F to C, 6 for C to F: ")
    if desConv == '1':
        Kinp = float(input("Input Kelvin to be converted to Celsius: "))
        convResult = Kinp - 273.15
        print("The result is: ")
        print(str(convResult))
    elif desConv == '2':
        Cinp = float(input("Input Celsius to be converted to Kelvin: "))
        convResult = Cinp + 273.15
        print("The result is: ")
        print(str(convResult))
    elif desConv == '3':
        Kinp2 = float(input("Input Kelvin to be converted to Fahrenheit: "))
        convResult = (Kinp2 - 273.15)*(9/5)+32
        print("The result is: ")
        print(str(convResult))
    elif desConv == '4':
        Finp = float(input("Input Fahrenheit to be converted to Kelvin: "))
        convResult = ((Finp-32)*5)/9+273.15
        print("The result is: ")
        print(str(convResult))
    elif desConv == '5':
        Finp2 = float(input("Input Fahrenheit to be converted to Celsius: "))
        convResult = ((Finp2-32)*5)/9
        print("The result is: ")
        print(str(convResult))
    elif desConv == '6':
        Cinp2 = float(input("Input Celsius to be converted to Fahrenheit: "))
        convResult = Cinp2*(9/5)+32
        print("The result is: ")
        print(str(convResult))
    else:
        print("Invalid entry for temperature conversion")
        exit()

elif desMeas == "mass":
    desConv = input("Press 1 for kg to lb, 2 for lb to kg, 3 for oz to g, 4 for g to oz, 5 for kg to ton, 6 for ton to kg: ")
    if desConv == '1':
        KGinp = float(input("Input kg to be converted to lbs: "))
        convResult = KGinp/0.45359237
        print("The result is: ")
        print(str(convResult))
    elif desConv == '2':
        LBinp = float(input("Input lbs to be converted to kg: "))
        convResult = LBinp*0.45359237
        print("The result is: ")
        print(str(convResult))
    elif desConv == '3':
        OZinp = float(input("Input oz to be converted to g: "))
        convResult = OZinp*28.34952
        print("The result is: ")
        print(str(convResult))
    elif desConv == '4':
        Ginp = float(input("Input g to be converted to oz: "))
        convResult = Ginp/28.34952
        print("The result is: ")
        print(str(convResult))
    elif desConv == '5':
        KGinp2 = float(input("Input kg to be converted to tons: "))
        convResult = KGinp2/1000
        print("The result is: ")
        print(str(convResult))
    elif desConv == '6':
        Tinp = float(input("Input tons to be converted to kg: "))
        convResult = Tinp*1000
        print("The result is: ")
        print(str(convResult))
    else:
        print("Invalid entry for mass conversion")
        exit()

elif desMeas == "volume":
    desConv = input("Press 1 for gal to L, 2 for L to gal, 3 for fl. oz. to gal, 4 for gal to fl. oz., 5 for fl. oz. to cup, 6 for cup to fl. oz: ")
    if desConv == '1':
        ginp = float(input("Input gallons to be converted to liters: "))
        convResult = ginp*3.7854
        print("The result is: ")
        print(str(convResult))
    elif desConv == '2':
        Linp = float(input("Input liters to be converted to gallons: "))
        convResult = Linp/3.7854
        print("The result is: ")
        print(str(convResult))
    elif desConv == '3':
        FLinp = float(input("Input fl. oz. to be converted to gallons: "))
        convResult = FLinp/128
        print("The result is: ")
        print(str(convResult))
    elif desConv == '4':
        ginp2 = float(input("Input gallons to be converted to fl. oz.: "))
        convResult = ginp2*128
        print("The result is: ")
        print(str(convResult))
    elif desConv == '5':
        FLinp2 = float(input("Input fl. oz. to be converted to cups: "))
        convResult = FLinp2/8
        print("The result is: ")
        print(str(convResult))
    elif desConv == '6':
        Cinp = float(input("Input cups to be converted to fl. oz.: "))
        convResult = Cinp*8
        print("The result is: ")
        print(str(convResult))
    else:
        print("Invalid entry for volume conversion")
        exit()

elif desMeas == "length":
    desConv = input("Press 1 for ft to m, 2 for m to ft, 3 for yd to m, 4 for m to yd, 5 for m to mile, 6 for mile to m: ")
    if desConv == '1':
        ftinp = float(input("Input ft to be converted to m: "))
        convResult = ftinp*0.304
        print("The result is: ")
        print(str(convResult))
    elif desConv == '2':
        minp = float(input("Input m to be converted to ft: "))
        convResult = minp*3.28084
        print("The result is: ")
        print(str(convResult))
    elif desConv == '3':
        ydinp = float(input("Input yds to be converted to m: "))
        convResult = ydinp*0.9144
        print("The result is: ")
        print(str(convResult))
    elif desConv == '4':
        minp2 = float(input("Input m to be converted to yds: "))
        convResult = minp2*1.0936
        print("The result is: ")
        print(str(convResult))
    elif desConv == '5':
        minp3 = float(input("Input m to be converted to miles: "))
        convResult = minp3*0.00062137
        print("The result is: ")
        print(str(convResult))
    elif desConv == '6':
        MIinp = float(input("Input miles to be converted to m: "))
        convResult = MIinp*1609.344
        print("The result is: ")
        print(str(convResult))
    else:
        print("Invalid entry for length conversion")
        exit()

else:
    print("Invalid entry for desired measurement conversion type")
    exit()