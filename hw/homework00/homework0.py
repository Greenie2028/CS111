## CONSTANTS SHOULD GO BELOW THIS COMMENT ##
PI = 3.14159265
PEOPLE_PER_LARGE = 7
PEOPLE_PER_MEDIUM = 3
PEOPLE_PER_SMALL = 1
COST_LARGE = 14.68
COST_MEDIUM = 11.48
COST_SMALL = 7.28
DIAMETER_LARGE = 20
DIAMETER_MEDIUM = 16
DIAMETER_SMALL = 12

def main():
    
    remainder = 0
    numLarge = 0
    numMedium = 0
    numSmall = 0
    numPeople = int(input("Please enter how many guests to order for: "))

    numLarge =  numPeople // PEOPLE_PER_LARGE
    remainder = numPeople % PEOPLE_PER_LARGE
    numMedium = remainder // PEOPLE_PER_MEDIUM
    remainder = remainder % PEOPLE_PER_MEDIUM
    numSmall =  round(remainder // PEOPLE_PER_SMALL)
    remainder = remainder % PEOPLE_PER_SMALL
    if remainder > 0:
        numSmall += 1
    print(f"{numLarge} large pizzas, {numMedium} medium pizzas, and {numSmall} small pizzas will be needed.\n")
    pizzaArea = (numLarge * (PI * (DIAMETER_LARGE/2)**2)) + (numMedium * (PI * (DIAMETER_MEDIUM/2)**2)) + (numSmall * (PI * (DIAMETER_SMALL/2)**2))
    print(f"A total of {pizzaArea:.2f} square inches of pizza will be ordered ({pizzaArea/numPeople:.2f} per guest).\n")
    tip = int(input("Please enter the tip as a percentage (i.e. 10 means 10%): "))
    totalCost = (numLarge * COST_LARGE) + (numMedium * COST_MEDIUM) + (numSmall * COST_SMALL)
    totalCost = totalCost + (totalCost * (tip / 100))
    print(f"The total cost of the event will be: ${totalCost:.2f}.")

if __name__ == "__main__":
    main()
