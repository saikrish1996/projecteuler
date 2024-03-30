from fractions import Fraction

seq = []

for i in range(1, 34):
    seq.append(1)
    seq.append(2*i)
    seq.append(1)

def getConvergents(leng):
    length = leng-2
    def getFraction(num):
        if num == length:
            return Fraction(1,seq[num])
        else:
            value = getFraction(num+1)
            return Fraction(1, seq[num] + value)
    
    return Fraction(2 + getFraction(0)).numerator

def getNumSum(num):
    strNum = [*str(num)]
    sum = 0
    for i in strNum:
        sum += int(i)
    print(sum)

getNumSum(getConvergents(100))
