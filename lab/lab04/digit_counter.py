def even_digit_counter(num):
    """Return the number of even digits"""
    counter = 0
    print("DEBUG: running even_digit_counter")
    i=0
    while num > 0:
        current_digit = num % 10
        i += 1
        print(f"DEBUG: processing loop for {i} time...")
        if current_digit % 2 == 0:
            print("DEBUG: Adding 1 to counter inside if")
            counter += 1
        num = int(num / 10)
    print("DEBUG: out of the loop")
    return counter

"""ADD_TESTING_CODE"""
if __name__ == "__main__":
    num = 9986
    print(even_digit_counter(num))