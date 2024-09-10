student_score = [100,99,90,84,66,53,47]
student_name = ["a","b","c","d","e","f","g"]

v = []

def student_ranking(student_score,student_name):
    for i in range(len(student_score)):
        v.append((f"{i}.{student_name[i]}-{student_score[i]}"))
    
    return v
    
print(student_ranking(student_score,student_name))