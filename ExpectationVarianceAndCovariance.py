#imports
import random


#Constants
PROBABILITIES = [0.166667, 0.166667, 0.166667, 0.166667, 0.166667, 0.166667]
RANGE = 6
STARTING_VALUE = 1
NUMBER_OF_ITEMS = 60000

#Globals
items = [random.randint(STARTING_VALUE, RANGE) for item in range(NUMBER_OF_ITEMS)]

#Discrete Case
def discrete_expectation(probabilities = []):
    expected_value = 0
    for x in range(probabilities.__len__()):    
        val = x+1
        expected_value = expected_value + (val * (probabilities[x]))
    return expected_value


def discrete_variance(expected_value, items = []):
    summed_squared_differences = 0
    for i in items:
        summed_squared_differences = summed_squared_differences + ((items[i] - expected_value)**2)
    variance = summed_squared_differences/items.__len__()
    return variance

ev = discrete_expectation(PROBABILITIES)
variance = discrete_variance(ev, items)
print(f'Expected Value : {ev} \n Variance : {variance}')
