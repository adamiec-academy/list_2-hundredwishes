def is_prime(n):
    number = True
    if n <2:
        number = False
        return number
    else:
        for i in range (2,n):
            if (n%i==0):
                number = False
        return number

def is_diabolic(n):
    devil = False
    if "666" in str(n):
        devil = True
    return devil

for i in range(1,100000):
    ile = 0
    if is_prime(i)==True: 
        if is_diabolic(i)==True:
            print(i)
            ile += 1
print("Takich liczb jest:", ile)
