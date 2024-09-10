def removedups(str):
    p = ""
    for char in str:
        if char not in p or char == ' ' or char == '-':
            p = p +char
    
    return p


def check (str):
    if (str == removedups(str)):
        return True
    else:
        return False
    


print(check("lu,mberjac ,,k"))