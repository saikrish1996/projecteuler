evenSum = 2

a , b, c = 1 , 2, 0

while c < 4000000:
    c = a+b
    a = b
    b = c
    if c % 2 == 0:
        evenSum += c
        
print(evenSum)