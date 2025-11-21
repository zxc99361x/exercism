def round_scores(student_scores):
    new=[]
    for i in student_scores:
        i=round(i,0)
        new.append(i)
    return new


def count_failed_students(student_scores):
    count=0
    for i in student_scores:
        if i<=40:
            count+=1
    return count


def above_threshold(student_scores, threshold):
    new=[]
    for i in student_scores:
        if i>=threshold:
            new.append(i)
    return new

def letter_grades(highest):
    avg=highest-40
    weg=avg/4
    new=[41,int(41+weg),int(41+2*weg),int(41+3*weg)]
    return new

def student_ranking(student_scores, student_names):
    new=[]
    for index,name in enumerate(student_names):
        new.append(f"{index+1}. {name}: {student_scores[index]}")
    return new


def perfect_score(student_info):
    new=[]
    for item in student_info:
        if item[1]==100:
            return item
    return new
            
