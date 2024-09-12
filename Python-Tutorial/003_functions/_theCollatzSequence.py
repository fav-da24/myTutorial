def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1

    print(result)
    return result


def main():
    while True:
        try:
            # Ask the user to enter a number
            user_input = input("Enter a number: ")
            number = int(user_input)  # Convert the input to an integer

            # Validate and run the Collatz sequence
            while number != 1:
                number = collatz(number)  # Call collatz and update number

        except ValueError:
            # Handle the case where input is not a valid integer
            print("Please enter a valid integer.")


# Run the main function
if __name__ == "__main__":
    main()
