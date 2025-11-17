def main():
    div20 = int(input("Enter an Integer divisible by 20 "))
    if float(div20) % 20 != 0:
        print(f"{div20} is not divisible by 20!")
    else:
        flt = float(input("Please enter a floating point number "))
        familymember = input("Enter a family relationship (mother, grandfather, cousin, etc.) ")
        noun = input("Enter a noun ")
        adjective = input("Enter an adjective ")

        print(f"{int(div20)//20} score and {flt:.3f} years ago, our fore{familymember}s brought forth upon this {noun} a {adjective} nation.")

if __name__ == "__main__":
    main()
    

