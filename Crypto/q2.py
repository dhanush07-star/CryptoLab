def check(s1,s2,s3):
    if(s1 > 0 and s2> 0 and s3>0):
        if(s1 + s2 > s3):
            return True
    else:
        return False


def is_equilateral(s1,s2,s3):
    if check(s1,s2,s3):
        if(s1 == s2 and s1 == s3 and s3 == s2):
            return True
        else:
            return False
    else:
        print("Given triangle is not a proper one")

def is_isosceles(s1,s2,s3):
    if check(s1,s2,s3):
        if(s1 == s2 or s1 == s3 or s3 == s2):
            return True
        else:
            return False
    else:
        print("Given triangle is not a proper one")


def is_scalene(s1,s2,s3):
    if check(s1,s2,s3):
        if(s1 != s2 and s1 != s3 and s3 != s2):
            return True
        else:
            return False
    else:
        print("Given triangle is not a proper one")


def is_degenerate(s1,s2,s3):
    if check(s1,s2,s3):
        if(s1+s2 == s3 or s1+s3 == s2 or s2+s3 == s1):
            return True
        else:
            return False
    else:
        print("Given triangle is not a proper one")


print(is_equilateral(10,10,10))
print(is_equilateral(3,6,7))
print(is_isosceles(2,1,3))
#print(is_scalene(1,1,3))
#print(is_degenerate(2,5,6))