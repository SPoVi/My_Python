'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example
    marks key:value pairs are
    'alpha':[20, 30, 40]
    'beta':[30, 50, 70]
    query_name = 'beta'


The query_name is 'beta'. beta's average score is (30+50+70)/3=50.0

.

Input Format

The first line contains the integer 'n', the number of students' records. 
The next 'n' lines contain the names and marks obtained by a student, each value separated by a space.
The final line contains query_name, the name of a student to query.

'''

print("Introduce el numero de alumnos: ")
n = int(input())

student_marks = {} # diccionario

print("\nIntrodue los nombres y notas: ")
for student in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

print("\nIntroduce el nombre del alumno cuyas notas quieres ver: ")
query_name = input()

scores_selcted_student = list(student_marks[query_name])

result = sum(scores_selcted_student)/len(scores_selcted_student)

print("\nLa media de notas del alumno "+query_name+" es: ")
print("%.2f" % result)