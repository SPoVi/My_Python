'''
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) 
having the second lowest grade.

Note: If there are multiple students with the second lowest grade,
 order their names alphabetically and print each name on a new line.
'''

print("Numero de alumnos: ")
n_alumnos = int(input())

print("Introduce nombre y nota: ")
students = [[input(), float(input())] for _ in range(n_alumnos)]
print("\nMostrando datos introducidos: ")
print(students)

print("\nSegunda peor nota: ")
s_punt = sorted(set(score for name, score in students))[1]
print(s_punt)

print('\nMostrando segundo(s) peor(es): ')
print('\n'.join(sorted(name for name, score in students if score == s_punt)))

