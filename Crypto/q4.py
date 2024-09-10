def letter_grade(highest):
    marks = highest - 40
    split = int(marks /4)
    #rint(split)
    F = 40

    return [41 , 41 +split , 41 + (split*2) , 41 + (split *3)]


print(letter_grade(88))


