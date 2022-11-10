def remove_parentheses(t):
    result=""
    is_inside= False
    for letter in range(len(t)):
        if t[letter] == "(":
            is_inside = True
        elif (t[letter-1] == ")" and t[letter] == " "):
            is_inside = False
        elif is_inside == False:
            result += t[letter]
    return result
