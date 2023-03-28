def tempp(temp,from_temp,to_temp):
    if from_temp == 'k' and to_temp == 'c':
        return temp - 273.15
    elif from_temp == 'c' and to_temp == 'k':
        return temp + 273.15
    elif from_temp == 'f' and to_temp == 'c':
        return (temp-32) * 5/9
    elif from_temp == 'c' and to_temp == 'f':
        return (temp * 9/5) + 32
    elif from_temp == 'f' and to_temp == 'k':
        return (temp + 459.67) * 5/9
    elif from_temp == 'k' and to_temp == 'f':
        return (temp * 9/5) - 459.67
    else:
        return temp

temp = float(input("\nEnter the temperature:\t"))

from_temp = input("\nEnter the unit you want to convert from [kelvin(k)/celcius(c)]/fahrenheit(f):\t\t").lower()

to_temp = input("\nEnter the unit you want to convert to [kelvin(k)/celcius(c)]/fahrenheit(f):\t\t").lower()

converted_temp = tempp(temp,from_temp,to_temp)

print(f" {temp}{from_temp} = {converted_temp}{to_temp}")