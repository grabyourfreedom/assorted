# This is a simple program that finds whether a given number is
# prime or not

# Let us define the contract for the function
# The function takes an integer as input and returns
#   True if prime and
#   False if the number if non-prime
#   False if the input is not a number


def is_prime(number):
    prime = False
    if type(number) is int and number > 1:
        if number == 2:
            return True

        for divisor in range(2, int(number)):
            if number % divisor == 0:
                return prime

        prime = True

    return prime
