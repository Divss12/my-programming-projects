#input number of boys and girls, and convert to integer
#catches exceptions and asks user to input again
while True:
    try:
        boys = int(input("Enter the number of boys: "))
    except ValueError:
        print("Please enter a numerical value")
        continue
    else:
        break

while True:
    try:
        girls = int(input("Enter the number of girls: "))
    except ValueError:
        print("Please enter a numerical value")
        continue
    else:
        break

#calculates percent of boys and girls and rounds it to 2 decimal places
boysperc = round(100 * boys/(boys+girls),2)
girlsperc = round(100 * girls/(boys+girls),2)

print(f"Boys: {boysperc}%")
print(f"Girls: {girlsperc}%")