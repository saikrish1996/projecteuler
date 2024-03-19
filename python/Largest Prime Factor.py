import math  


def getFactors(n):
    factors = []
    for i in range(1,  int(math.sqrt(n))):
        if n % i == 0:
            if n/i == i:
                factors.append(i)
            else:
                factors.append(i)
                factors.append(int(n/i))
    return factors
      
    
factors = getFactors(600851475143)
factors.sort()

def getPrimefactors(factors):
    primeFactor = []
    for num in factors:
        factors = getFactors(num)
        if len(factors) == 2:
            primeFactor.append(num)
    return primeFactor

primeFactors = getPrimefactors(factors)

primeFactors[len(primeFactors) - 1]