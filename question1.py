def DecimalToBinary(n):
    if n == 0:
        return ""
    else:
        return DecimalToBinary(n // 2) + str(n % 2) 
                       

def convertDecimal(n):
    if n == 0:
        return "0"
    else:
        return DecimalToBinary(n)

print(convertDecimal(7)) 
print(convertDecimal(10)) 