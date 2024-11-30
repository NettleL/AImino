temp = int(input("TEMPERATURE: "))
unit = input("CELSIUS OR FAHRENHEIT (c/f): ")

if unit == 'c':
    print("TEMPERATURE (⁰F):",  ((temp * 1.8) + 32))

elif unit == 'f':
    print("TEMPERATURE (⁰C):",  ((temp-32) / 1.8))
    
print('')