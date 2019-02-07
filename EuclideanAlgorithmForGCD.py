import math

FIRST_NUMBER = 49
SECOND_NUMBER = 42

def GCD(a, b):
    min = a if (a<b) else b
    max = b if (a<b) else a
    return min if(max%min==0) else GCD(min, (max-math.floor(max/min)*min)) 

print(GCD(FIRST_NUMBER, SECOND_NUMBER))