def remove_parentheses(t):
    result=""
    is_inside= False
    for letter in t:
        if letter == "(":
            is_inside = True
        elif letter == ")":
            is_inside = False
        elif is_inside == False:
            result += letter
    return result.strip()
