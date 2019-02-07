#imports
import math

#Constants
TEST_NUMBER = 41


def test_prime(number):
    if (number%2==0):
        return False
    else:
        for i in range(2, math.ceil(math.sqrt(number))):
            if(number%i==0):
                return False
        return True

print(test_prime(TEST_NUMBER))
