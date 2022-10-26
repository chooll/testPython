file = open("text.txt", 'r')

for string in file:
    temp = string.replace("\n", "")
    temp = float(temp)

    print (f"Корень числа {temp} равен {temp**2}")