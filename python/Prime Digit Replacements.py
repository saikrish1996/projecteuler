import time

startTime = time.time()
# Sieve of Eratosthenes formula
def primeNumberList(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p*p <= n:
        if prime[p] == True:
            for i in range(p*p, n+1, p):
                prime[i] = False
                
        p += 1
    for i in range(n+1): 
        if prime[i]:
            genWildcardStrings(str(i), 0)
            
    return prime

wildcards = []
searched = set()
# generate every possible wildcard strings
def genWildcardStrings(s, index):
    if index > 0: # and s not in searched:
        wildcards.append(s)
        searched.add(s)
    for x in range(index, len(s)):
        genWildcardStrings(createPlaceholder(s, x), x+1)
        
# replace a character with '*'
def createPlaceholder(s, index):
    return s[0:index] + '*' + s[index+1:]

primeList = primeNumberList(100)

for wildCardNum in wildcards:
    numOfPrimes = 0
    for i in range(0, 10):
        newNum = int(wildCardNum.replace("*", str(i)))
        if len(str(newNum)) < len(wildCardNum) or len(str(newNum)) == 1:
            continue
        if primeList[int(newNum)]:
            numOfPrimes+=1
    if numOfPrimes >= 6:
        print(time.time()-startTime)
        print(wildCardNum)
        break
    