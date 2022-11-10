def cipher(text, shift):
    result=""
    for sign in text:
        if sign == " ":
            result += sign
        else:
            number = ord(sign) + shift
            if (number in range(65,91) or number in range(97,123)):
                result += chr(number)
            else:
                number -=26
                result += chr(number)    
    return result

def decipher(text, shift):
    result=""
    for sign in text:
        if sign == " ":
            result += sign
        else:
            number = ord(sign) - shift
            if ((number in range(65,91) and sign.isupper()==True) or (number in range(97,123) and sign.isupper()==False)):
                result += chr(number)
            else:
                number +=26
                result += chr(number)    
    return result
